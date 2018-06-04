from aiohttp import Timeout
from brittle_wit_core import TwitterError
from brittle_wit.executors import twitter_req_to_http_req
from brittle_wit.helpers import LOGGER
from brittle_wit.streaming.entry_processor import (EntryProcessor,
                                                   noop_entry_parser)


class TwitterStream:

    def __init__(self, session, app_cred, client_cred, twitter_req,
                 parser=noop_entry_parser, chunk_size=4096,
                 read_hang_timeout=60):
        """
        Initialize a Twitter stream.

        There is no initial connection; Twitter doesn't like idle reader hands.

        :param session: the aiohttp.ClientSession object
        :param app_cred: the AppCredentials
        :param client_cred: the ClientCredentials
        :param twitter_req: the TwitterRequest to initiate streaming
        :param parser: a parser which takes a byte-entry and translates it
            into a message.
        :param chunk_size: the number of bytes to asynchronously read from
            Twitter for each receive
        :param read_hang_timeout: the number of seconds to wait while waiting
            for the *next* read before raising a Timeout
        """
        self._session = session
        self._app_cred = app_cred
        self._client_cred = client_cred
        self._twitter_req = twitter_req
        self._parser = parser
        self._chunk_size = chunk_size
        self._read_hang_timeout = read_hang_timeout

        self._entry_processor = EntryProcessor()
        self._http_req, self._resp = None, None

    def is_open(self):
        """
        :return: True if their is an active connection to Twitter's servers.
        """
        return (self._http_req is not None and self._resp is not None and
                self._resp.connection and not self._resp.connection.closed)

    def _connect(self):
        """
        Connect to Twitter's servers.
        """
        LOGGER.info("Connecting to twitter.")

        # =====================================================================
        # There may only be one set of credentials connected to a streaming
        # endpoint at a time. Preempting an existing connection is
        # error-prone. Complain loudly when a connection already exists.
        # =====================================================================
        if self.is_open():
            LOGGER.critical("Trying to connect an already open stream!")
            raise RuntimeError("Already connected. Call close() first!")

        # =====================================================================
        # Twitter streams should not read timeout since they poll forever.
        # aiohttp implements it such that reads time is cumulative, not
        # episodic, which is wrong for long-polling semantics. Instead, the
        # read_hang_timeout constructor arg controls the amount of time
        # to wait *between* reads.
        # =====================================================================
        self._http_req = twitter_req_to_http_req(self._session,
                                                 self._app_cred,
                                                 self._client_cred,
                                                 self._twitter_req)

    def disconnect(self):
        """
        Disconnect the stream from Twitter's servers.
        """
        LOGGER.info("Disconnecting stream from twitter's server")

        if self._http_req is not None:
            self._http_req.close()  # Force close.
            self._http_req = None

        if self._resp is not None:
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
        LOGGER.info("Reconnecting stream.")

        # Twitter wants one IP per connection.
        if self.is_open() and force_close_if_open:
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

    async def __aiter__(self):
        """
        Commence streaming, returning this object as an iterator.
        """
        LOGGER.info("Creating async iterator.")

        if not self.is_open():
            self.reconnect()  # Ensure an open connection.

        if self._resp is None:
            self._resp = await self._http_req.__aenter__()

            if self._resp.status != 200:
                resp, self._resp = self._resp, None
                LOGGER.error("Response error: {}".format(resp))
                raise TwitterError(self._client_cred,
                                   self._twitter_req,
                                   resp,
                                   await resp.text())

        return self

    async def __anext__(self):
        """
        This reads one message from the stream.
        """
        # If there are no messages ready, read from the stream.
        while not self._entry_processor:
            with Timeout(self._read_hang_timeout):
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
        return self._parser(self._entry_processor.pop())
