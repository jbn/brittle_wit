import aiohttp
import asyncio
import bz2
import json
import time

from aiohttp import web
from itertools import compress
from brittle_wit.rate_limit import RateLimit
from brittle_wit.helpers import LOGGER
from brittle_wit_core import TwitterError, BrittleWitError
from brittle_wit.executors import twitter_req_to_http_req, LOGGER
import brittle_wit.connection_props as DEFAULTS


from brittle_wit.streaming.entry_processor import (EntryProcessor,
                                                   noop_entry_parser,
                                                   json_entry_parser)
from brittle_wit.streaming.receivers import (StreamReceiver,
                                             FeedSerializer,
                                             CallableStreamHandler,
                                             PartitioningFeedSerializer)
from brittle_wit.streaming.twitter_stream import TwitterStream


class StreamingHTTPPipe(StreamReceiver):
    """
    Utility StreamReceiver which pipes messages to streaming HTTP clients.

    Example
    -------
    > pipe = StreamingHTTPPipe()
    > stream_processor.subscribe(pipe, False)
    > app = aiohttp.web.Application()
    > app.router.add_get('/', pipe.handle())
    > server = loop.create_server(httpd.make_handler(), "0.0.0.0", 8394)
    > loop.run_until_complete(server)
    """
    DEFAULT_HEADERS = {'Content-Type': 'application/json'}

    def __init__(self, **resp_headers):
        # The _clients dict maps a unique identifier -- via id(obj) -- to a
        # pair of (StreamResponse, Event).
        self._clients = {}

        self._headers = {**self.DEFAULT_HEADERS, **resp_headers}

    async def handle(self, req):
        caller_id = id(req)
        resp = web.StreamResponse(status=200, headers=self._headers)

        try:
            # Start the FSM.
            await resp.prepare(req)

            # The send method signals handle when its processing finishes.
            finished_flag = asyncio.Event()
            self._clients[caller_id] = (resp, finished_flag)
            await finished_flag.wait()

        except asyncio.CancelledError:
            # Generally, this means the client disconnected.
            if caller_id in self._clients:
                del self._clients[caller_id]

        return resp

    async def _send_to(self, message, caller_id, resp, finished_flag):
        try:
            await resp.write(message)
        except Exception as e:
            # This is a sloppy catch all for now. I'm not sure if
            # asyncio guarantees a cancel to handle prior to a
            # possible write. But, I do know it would be quite
            # wrong for a write to one client to cause failures
            # in other clients.
            finished_flag.set()
            return True
        return False

    async def send_to_all(self, message):
        tasks = [self._send_to(message, caller_id, resp, finished_flag)
                 for caller_id, (resp, finished_flag) in self._clients.items()]

        finished = await asyncio.gather(*tasks)

        for client in compress(self._clients.keys(), finished):
            del self._clients[client]

    def send(self, message):
        # XXX: Sloppy refactoring
        asyncio.ensure_future(self.send_to_all(message))

class StreamProcessor:
    """
    Sends TwitterResponses from a Stream to subscribers.
    """

    def __init__(self, twitter_stream):
        self._twitter_stream = twitter_stream
        self._subscribers = {}
        self._requires_json = False
        self._n_failures = False

    @property
    def requires_json(self):
        return self._requires_json

    def subscribe(self, receiver, as_json=False):
        """
        Subscribe a given receiver to the stream.

        :param receiver: a StreamReceiver object
        :param as_json: json parsing is relatively expensive. if a subscriber
            requires json, json parsing occurs, but only once for all the
            subscribers requiring json. Otherwise, there is no json parsing
        """
        # It's preferable to derive a class from StreamReceiver, but sometimes
        # it adds complexity. Send is the duck-type-required method.
        if not hasattr(receiver, "send"):
            raise AttributeError("Handler must implement send(msg)")

        handler_id = id(receiver)

        if handler_id in self._subscribers:
            raise RuntimeError("Already subscribed!")

        if as_json:
            self._requires_json = True

        self._subscribers[handler_id] = (receiver, as_json)
        return handler_id

    def unsubscribe(self, receiver):
        """
        Unsubscribe the given receiver from stream processing.

        :param receiver: an already subscribed receiver
        """
        handler_id = id(receiver)

        if handler_id not in self._subscribers:
            msg = "Either never subscribed or already unsubscribed!"
            raise RuntimeError(msg)

        required_json = self._subscribers[handler_id][1]

        del self._subscribers[handler_id]

        if required_json and not any(p[1] for p in self._subscribers.values()):
            self._requires_json = False

    def _send_to_all(self, message):
        # JSON parsing is expensive. If the application only pipes the
        # Twitter Stream to HTTP clients, it's dead time. The pattern
        # would be: BYTES -> JSON -> BYTES
        if self._requires_json:
            json_message = json_entry_parser(message)

        for subscriber, as_json in self._subscribers.values():
            subscriber.send(json_message if as_json else message)

    async def _stream_to_subscribers(self):
        LOGGER.info("Taking one for reset failures.")

        # Take one. If it's successful, this lets us reset the failure count.
        # One assignment for each send is a waste of cycles!
        async for message in self._twitter_stream:
            self._send_to_all(message)
            self._n_failures = 0
            break

        LOGGER.info("Streaming to subscribers.")

        async for message in self._twitter_stream:
            self._send_to_all(message)

    async def run(self):
        """
        Run the StreamProcessor, parsing the stream and sending responses.

        Retry Strategy: https://dev.twitter.com/streaming/overview/connecting
        """
        sleep_time = 0

        while True:
            LOGGER.info("Running StreamProcessor.")
            try:
                await self._stream_to_subscribers()
            except KeyboardInterrupt:
                LOGGER.error("User requested termination (KeyboardInterrupt)!")
                raise  # You're debugging, and want things to stop.
            except TwitterError as e:
                if e.status_code == 420:
                    # > Back off exponentially for HTTP 420 errors.
                    # > Start with a 1 minute wait and double each attempt.
                    sleep_time = min(2**self._n_failures, 16) * 60
                elif e.status_code == 429:
                    # You've been rate limited.
                    rate_limit = RateLimit.from_response(self._resp)
                    sleep_time = rate_limit.sleep_time_remaining
                else:
                    # > Back off exponentially for HTTP errors for which
                    # > reconnecting would be appropriate. Start with a 5
                    # > second wait, doubling each attempt, up to 320 seconds.
                    sleep_time = min(2**self._n_failures * 5, 320)

                msg = "Stream %s'd waiting a %d seconds (failure #%d)"
                LOGGER.error(msg, e, sleep_time, self._n_failures)
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                # > These problems are generally temporary and tend to clear
                # > quickly. Increase the delay in reconnects by 250ms each
                # > attempt, up to 16 seconds.
                sleep_time = min(0.25 * (self._n_failures + 1), 16.0)

                msg = "Stream %s'd waiting a %d seconds (failure #%d)"
                LOGGER.error(msg, e, sleep_time, self._n_failures)
            except Exception as e:
                LOGGER.error("Aborting on %s", e)
                raise

            # You have to completely disconnect!
            self._twitter_stream.disconnect()
            self._n_failures += 1
            await asyncio.sleep(sleep_time)


async def basic_streamer(app_cred, client_cred, twitter_req, callback,
                         as_json=True):
    """
    Process a simple stream with a callback.

    :param app_cred: the AppCredentials
    :param client_cred: the ClientCredentials
    :param twitter_req: the TwitterRequest to initiate streaming
    :param callback: a callback in the form of ``f(tweet_obj)``
    :param as_json: if True (default) parse each message as json
    """
    handler = CallableStreamHandler(callback)

    opts = DEFAULTS.SESSION_OPTS.copy()
    opts['connector'] = aiohttp.TCPConnector(**DEFAULTS.TCP_CONN_STREAMING)

    async with aiohttp.ClientSession(**opts) as sess:
        stream = TwitterStream(sess, app_cred, client_cred, twitter_req)
        processor = StreamProcessor(stream)
        processor.subscribe(handler, as_json)

        await processor.run()
