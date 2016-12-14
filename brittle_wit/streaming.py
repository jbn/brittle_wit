import asyncio
import json

import aiohttp
from aiohttp import web

from brittle_wit.constants import LOGGER
from brittle_wit.executors import twitter_req_to_http_req
from brittle_wit.messages import TwitterError, BrittleWitError


class EntryProcessor:
    """
    Splits a stream of bytes into CRLF-separated messages.
    """

    def __init__(self):
        self._buf = b""  # Use a more efficient buffer
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

        This connects to Twitter's servers but doesn't start reading until a
        call to __iter__.

        :param session: the aiohttp.ClientSession object
        :param app_cred: the AppCredentials
        :param client_cred: the ClientCredentials
        :param twitter_req: the TwitterRequest to initiate streaming
        :param parser: a parser which takes a byte-entry and translates it
            into a message.
        :param chunk_size: the number of bytes to asynchronously read from
            Twitter at a time
        """
        self._session = session
        self._app_cred = app_cred
        self._client_cred = client_cred
        self._twitter_req = twitter_req
        self._parser = parser
        self._chunk_size = chunk_size

        self._entry_processor = EntryProcessor()
        self._http_req = None

        self._connect()

    def _connect(self):
        """
        Connect to Twitter's servers.
        """
        # There may only be one set of credentials connected to a
        # streaming endpoint at a time. Preempting an existing
        # connection is error-prone. Complain loudly when a connection
        # already exists.
        if self.is_open:
            raise RuntimeError("Already connected. Call close() first!")

        self._http_req = twitter_req_to_http_req(self._session,
                                                 self._app_cred,
                                                 self._client_cred,
                                                 self._twitter_req)

    @property
    def is_open(self):
        """
        :return: True if their is an active connection to Twitter's servers.
        """
        return self._http_req is not None and not self._resp.connection.closed

    def reconnect(self, force_close_if_open=False, clear_prior_messages=False):
        """
        Reconnect to Twitter's servers.

        :param force_close_if_open: if True, close the prior connection, if it
            exists
        :param clear_prior_messages: if True, purges all (correct) messages
            waiting for consumption on the internal EntryProcessor from the
            prior connection
        """
        # Explicitly acknowledge that forced closure is okay.
        if force_close_if_open and self.is_open:
            self.disconnect()

        # The initiating request does not change between connection resets,
        # so old messages are consumable.
        if clear_prior_messages:
            self._entry_processor.purge_mailbox()

        # The buffer underling the entry processor should always be in
        # an initially pristine state. A broken connection virtually
        # ensures corruption.
        self._entry_processor.purge_buffer()

        self._connect()

    def disconnect(self):
        """
        Disconnect the stream from Twitter's servers.
        """
        if self._http_req is not None:
            self._http_req.close()
            self._http_req = None

    async def __aiter__(self):
        """
        Commence streaming, returning this object as an iterator.
        """
        # I hate the next line. Is there a decontextualize pattern?
        self._resp = await self._http_req.__aenter__()
        if self._resp.status != 200:
            raise TwitterError(self._client_cred,
                               self._twitter_req,
                               self._resp,
                               await self._resp.text())

        return self

    async def __anext__(self):
        # If there are no messages ready, read from the stream.
        while not self._entry_processor:
            chunk = await self._resp.content.read(self._chunk_size)
            if not chunk:
                LOGGER.error("Read zero bytes on a stream.")
                break
            self._entry_processor.process(chunk)

        # If there are no messages ready, the stream closed!
        if not self._entry_processor:
            LOGGER.error("Stream Closing (non-explicit)")
            raise StopAsyncIteration

        # Take one message.
        return self._parser(self._entry_processor.take_one())


class StreamProcessor:
    def __init__(self, twitter_stream):
        self._twitter_stream = twitter_stream
        self._subscribers = {}
        self._requires_json = False

    def subscribe(self, handler, as_json=False):
        handler_id = id(handler)

        if handler_id in self._subscribers:
            raise RuntimeError("Already subscribed!")

        if not hasattr(handler, "send"):
            raise RuntimeError("Handler must implement send(msg)")

        if as_json:
            self._requires_json = True

        self._subscribers[handler_id] = (handler, as_json)
        return handler_id

    def unsubscribe(self, handler):
        handler_id = id(handler)

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

    async def run(self):
        # Retry Strategy: https://dev.twitter.com/streaming/overview/connecting
        # TODO: More compliant!
        failures, failed = 0, False
        while True:
            try:
                if failed:
                    failures += 1
                    self._twitter_stream.reconnect(force_close_if_open=True)
                async for message in self._twitter_stream:
                    self._send_to_all(message)
                    failed = False  # TODO: FIX: This is such a waste!
            except TwitterError as e:
                # The docs only say 420. But, I suspect 429 codes, too.
                if e.status_code == 420 or e.status_code == 429:
                    sleep_time = 60 * 2**failures
                    msg = "Stream 420'd waiting {} seconds (failure {})"
                    LOGGER.error(msg.format(sleep_time, failures))
                    await asyncio.sleep(sleep_time)
                else:
                    sleep_time = min(5 * 2**failures, 320)
                    msg = "Stream {}'d waiting {} seconds (failure {})"
                    LOGGER.error(msg.format(e.status_code, sleep_time,
                                            failures))
                    print(e._http_resp)  # FIX: XXX: HACK: FUCK

                failed = True
                await asyncio.sleep(sleep_time)
            except BrittleWitError as e:
                if e.is_retryable:  # TODO FIX as is network error.
                    sleep_time = min(0.25 * failures, 16)
                    msg = "Stream {}'d waiting {} seconds (failure {})"
                    LOGGER.error(msg.format(repr(e), sleep_time, failures))
                    failed = True
                    await asyncio.sleep(sleep_time)
            except KeyboardInterrupt:
                raise
            except Exception as e:
                print(e)
                sleep_time = min(0.25 * failures, 16)
                msg = "Stream {}'d waiting {} seconds (failure {})"
                LOGGER.error(msg.format(repr(e), sleep_time, failures))
                failed = True
                await asyncio.sleep(sleep_time)


class StreamingHTTPPipe:
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
                print("Send", repr(e))
                finished_flag.set()
                removal_set.append(caller_id)
                raise e

        for k in removal_set:
            del self._clients[k]


async def save_raw_stream(session, app_cred, client_cred, twitter_req,
                          output_path, chunk_size=4096, timeout=30):
    """
    Save response headers and timeout seconds of response for a streaming req.

    I use this function to save some stream output so I can write text fixtures
    against the streaming API.

    :param session: the aiohttp ClientSession
    :param app_cred: an AppCredentials object
    :param client_cred: a ClientCredentials object
    :param twitter_req: the TwitterRequest for the streaming endpoint
    :param output_path: the output path. Technically, this is a prefix as the
        function writes two output files: prefix + '.headers.json' and
        prefix + '.content.raw'
    :param chunk_size: the number of bytes for read chunking
    :param timeout: the number of seconds to pipe response to file output
        before exiting.
    """
    header_path = output_path + ".headers.json"
    content_path = output_path + ".content.raw"

    http_req = twitter_req_to_http_req(session, app_cred,
                                       client_cred, twitter_req)

    # This uses blocking file operations. It's possible that a slow
    # disk could generate a stale warning. But, that's fine for the
    # use case of this function: debugging. A stale warning is useful
    # information to have in a saved feed as a fixture.
    with open(header_path, "w") as hp, open(content_path, "wb") as fp:
        try:
            with aiohttp.Timeout(timeout):
                async with http_req as resp:
                    # Save response headers.
                    json.dump({k: v for k, v in resp.headers.items()},
                              hp, indent=4)

                    while True:
                        chunk = await resp.content.read(chunk_size)
                        if not chunk:
                            break
                        fp.write(chunk)
        except asyncio.TimeoutError:
            pass
