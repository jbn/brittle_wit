import asyncio
import json
import aiohttp
import bz2

from aiohttp import web
from brittle_wit.rate_limit import RateLimit
from brittle_wit_core import TwitterError, BrittleWitError
from brittle_wit.executors import twitter_req_to_http_req, LOGGER
import brittle_wit.connection_props as DEFAULTS


class EntryProcessor:
    """
    Splits a stream of bytes into CRLF-separated messages.
    """

    def __init__(self):
        # Note: I tried using a bytearray instead of a byte string but it
        # ended up being slower and having greater jitter than byte strings.
        self._buf = b""
        self._mailbox = []

    def process(self, chunk):
        """
        Translate received bytes into messages in a mailbox.

        :param chunk: a chunk of bytes received from the HTTP connection
        """
        self._buf += chunk

        # Streams are `\r\n`-separated JSON messages.
        raw_lines = self._buf.split(b"\r\n")

        # If only one element in the split, then there wasn't a CRLF.
        if len(raw_lines) > 1:
            # The last element may be a b'', which is perfectly fine.
            self._buf = raw_lines[-1]

            # Blank lines are keep-alive messages.
            self._mailbox.extend(l for l in raw_lines[:-1] if l.strip())

    def messages(self):
        """
        Return the messages then reset the mailbox

        :return: the enqueued messages
        """
        msgs = self._mailbox
        self._mailbox = []
        return msgs

    def __bool__(self):
        """
        :return: True if there are any messages available
        """
        return bool(self._mailbox)

    def take_one(self):
        """
        :return: the first message removed from the mailbox
        """
        return self._mailbox.pop(0)

    def purge_buffer(self):
        """
        Reset the internal buffer.

        This is useful when restarting a stream. When the old stream
        terminates, the buffer is incomplete. Appending to it will produce a
        corrupt entry.
        """
        self._buf = b''

    def purge_mailbox(self):
        """
        Resets the mailbox so there are no messages
        """
        self._mailbox = []

    def __iter__(self):
        """
        :return: an iterator which pops messages of the mailbox until fully
            consumed
        """
        return self._entry_consumer()

    def _entry_consumer(self):
        while self._mailbox:
            yield self.take_one()


def noop_entry_parser(entry):
    """
    :return: the entry string without further processing.
    """
    return entry


def json_entry_parser(entry):
    """
    :return: the entry parsed as a JSON object
    """
    return json.loads(entry.decode('ascii'))


class TwitterStream:

    def __init__(self, session, app_cred, client_cred, twitter_req,
                 parser=noop_entry_parser, chunk_size=4096):
        """
        Initialize a Twitter stream.

        There is no initial connection, since Twitter doesn't like idle
        reader hands.

        :param session: the aiohttp.ClientSession object
        :param app_cred: the AppCredentials
        :param client_cred: the ClientCredentials
        :param twitter_req: the TwitterRequest to initiate streaming
        :param parser: a parser which takes a byte-entry and translates it
            into a message.
        :param chunk_size: the number of bytes to asynchronously read from
            Twitter for each receive
        """
        self._session = session
        self._app_cred = app_cred
        self._client_cred = client_cred
        self._twitter_req = twitter_req
        self._parser = parser
        self._chunk_size = chunk_size

        self._entry_processor = EntryProcessor()
        self._http_req = None
        self._resp = None

    def is_open(self):
        """
        :return: True if their is an active connection to Twitter's servers.
        """
        return (self._http_req is not None and
                self._resp.connection and not self._resp.connection.closed)

    def _connect(self):
        """
        Connect to Twitter's servers.
        """
        # There may only be one set of credentials connected to a streaming
        # endpoint at a time. Preempting an existing connection is
        # error-prone. Complain loudly when a connection already exists.
        if self.is_open():
            raise RuntimeError("Already connected. Call close() first!")

        self._http_req = twitter_req_to_http_req(self._session,
                                                 self._app_cred,
                                                 self._client_cred,
                                                 self._twitter_req,
                                                 timeout=None)

    def disconnect(self):
        """
        Disconnect the stream from Twitter's servers.
        """
        if self._http_req is not None:
            self._http_req.close()
            self._http_req = None
            self._resp = None

    def reconnect(self, force_close_if_open=True, clear_prior_messages=False):
        """
        Reconnect to Twitter's servers.

        :param force_close_if_open: if True, close the prior connection, if it
            exists; if false, raise error if it is open
        :param clear_prior_messages: if True, purges all (correct) messages
            waiting for consumption on the internal EntryProcessor from the
            prior connection
        """
        # Twitter wants one IP per connection.
        if self.is_open():
            if force_close_if_open:
                self.disconnect()
            else:
                raise RuntimeError("Trying to reconnect on open stream.")

        # The initiating request does not change between connection resets,
        # so old messages are consumable.
        if clear_prior_messages:
            self._entry_processor.purge_mailbox()

        # The buffer underling the entry processor should always be in
        # an initially pristine state. A broken connection virtually
        # ensures corruption.
        self._entry_processor.purge_buffer()

        self._connect()

    async def __aiter__(self):
        """
        Commence streaming, returning this object as an iterator.
        """
        if not self.is_open():
            self._connect()
        elif self._resp is not None:
            return self  # Stream processor depends on this behavior.

        # XXX. I hate the next line. Is there a decontextualize pattern?
        self._resp = await self._http_req.__aenter__()

        if self._resp.status != 200:
            raise TwitterError(self._client_cred,
                               self._twitter_req,
                               self._resp,
                               await self._resp.text())

        return self

    async def __anext__(self):
        """
        This reads one message from the stream.
        """
        # If there are no messages ready, read from the stream.
        while not self._entry_processor:
            chunk = await self._resp.content.read(self._chunk_size)
            if not chunk:
                LOGGER.error("Read zero bytes on a stream.")
                break
            self._entry_processor.process(chunk)

        # If there are no messages ready, the stream closed!
        # XXX: TODO: When does this occur. StopAsycIteration is scary.
        if not self._entry_processor:
            LOGGER.error("Stream Closing (non-explicit)")
            raise StopAsyncIteration

        # Take one message.
        return self._parser(self._entry_processor.take_one())


class StreamReceiver:

    def close(self):
        pass


class FeedSerializer(StreamReceiver):
    """
    Write each message to a bz2 file, *syncronously*.

    """

    def __init__(self, output_file, overwrite_existing=False, as_bz2=False):
        """
        :param as_bz2: if true, saves the file with BZ2 copression.
            BZ2 is useful for Spark/Hadoop analytics as it's splittable and
            compression rate is high. However, it's CPU intensive, which could
            be a problem.
        """
        mode = 'a' if overwrite_existing else 'w'
        if not as_bz2:
            mode += 'b'

        open_file = bz2.open if as_bz2 else open
        self._output_stream = open_file(output_file, mode)

    def send(self, message):
        self._output_stream.write(json.dumps(message).encode() + b"\n")

    def close(self):
        self._output_stream.close()


class LambdaStreamHandler(StreamReceiver):
    """
    Stream receiver that wraps a lambda (mostly for testing)
    """

    def __init__(self, underlying_func):
        """
        :param underlying_func: function to invoke for each message received
            by ``#send(msg)``
        """
        self._underlying_func = underlying_func

    def send(self, msg):
        return self._underlying_func(msg)


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

        self._headers = {**StreamingHTTPPipe.DEFAULT_HEADERS, **resp_headers}

    async def handle(self, req):
        caller_id = id(req)
        resp = web.StreamResponse(status=200, headers=self._headers)

        try:
            # Start the FSM.
            await resp.prepare(req)

            # The send method signals handle when it processing finishes.
            finished_flag = asyncio.Event()
            self._clients[caller_id] = (resp, finished_flag)
            await finished_flag.wait()

        except asyncio.CancelledError:
            # Generally, this means the client disconnected.
            if caller_id in self._clients:
                del self._clients[caller_id]

        return resp

    def send(self, message):
        removal_set = []

        for caller_id, (resp, finished_flag) in self._clients.items():
            try:
                resp.write(message)  # I don't think draining is nessessary.
            except Exception as e:
                # This is a sloppy catch all for now. I'm not sure if
                # asyncio guarantees a cancel to handle prior to a
                # possible write. But, I do know it would be quite
                # wrong for a write to one client to cause failures
                # in other clients.
                finished_flag.set()
                removal_set.append(caller_id)

        for k in removal_set:
            del self._clients[k]


class StreamProcessor:
    """
    Sends TwitterResponses from a Stream to subscribers.
    """

    def __init__(self, twitter_stream):
        self._twitter_stream = twitter_stream
        self._subscribers = {}
        self._requires_json = False
        self._n_failures = False

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
        # Take one. If it's successful, this lets us reset the failure count.
        # One assignment for each send is a waste of cycles!
        async for message in self._twitter_stream:
            self._send_to_all(message)
            self._n_failures = 0
            break

        async for message in self._twitter_stream:
            self._send_to_all(message)

    async def run(self):
        """
        Run the StreamProcessor, parsing the stream and sending responses.

        Retry Strategy: https://dev.twitter.com/streaming/overview/connecting
        """
        sleep_time = 0

        while True:
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

            self._n_failures += 1
            # You have to completely disconnect!
            self._twitter_stream.disconnect()
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
    handler = LambdaStreamHandler(callback)

    opts = DEFAULTS.SESSION_OPTS.copy()
    opts['connector'] = aiohttp.TCPConnector(**DEFAULTS.TCP_CONN_STREAMING)

    with aiohttp.ClientSession(**opts) as sess:
        stream = TwitterStream(sess, app_cred, client_cred, twitter_req)
        processor = StreamProcessor(stream)
        processor.subscribe(handler, as_json)

        await processor.run()
