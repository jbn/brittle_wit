import json
import asyncio
import aiohttp

from brittle_wit.executors import twitter_req_to_http_req


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


class SimpleStream:
    def __init__(self, session, app_cred, client_cred, twitter_req,
                 parser=json_entry_parser):
        self._entry_processor = EntryProcessor()
        self._http_req = twitter_req_to_http_req(session,
                                                 app_cred,
                                                 client_cred,
                                                 twitter_req)
        self._parser = parser

    async def __aiter__(self):
        self._resp = await self._http_req.__aenter__()  # I hate this.

        return self

    async def __anext__(self):
        # If there are no messages ready, read from the stream.
        while not self._entry_processor:
            chunk = await self._resp.content.read(4096)
            if not chunk:
                break
            self._entry_processor.process(chunk)

        # If there are no messages ready, the stream closed!
        if not self._entry_processor:
            self.close()
            raise StopAsyncIteration

        # Take one message.
        return self._parser(self._entry_processor.take_one())

    def close(self):
        # Signal end.
        self._resp.close()


async def save_stream(session, app_cred, client_cred, twitter_req,
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
