import json
import asyncio
import aiohttp

from brittle_wit.executors import twitter_req_to_http_req


class EntryProcessor:
    def __init__(self):
        self._buf = b""  # Use a more efficient buffer
        self._messages = []

    def append(self, text):
        self._buf += text

        # Streams are `\r\n`-separated JSON messages.
        raw_lines = self._buf.split(b"\r\n")

        if raw_lines and raw_lines[0]:
            raw_lines, self._buf = raw_lines[:-1], raw_lines[-1]
        else:
            self._buf = b""

        # Blank lines are keep-alive messages.
        lines = (l for l in raw_lines if l.strip())
        self._messages += [json.loads(line.decode('ascii')) for line in lines]

    @property
    def messages(self):
        msgs = self._messages
        self._messages = []
        return msgs

    def take_one(self):
        return self._messages.pop(0)

    def purge(self):
        self._messages = []

    def __bool__(self):
        return bool(self._messages)

    def __iter__(self):
        return self.messages()


class SimpleStream:
    def __init__(self, session, app_cred, client_cred, twitter_req):
        self._entry_processor = EntryProcessor()
        self._http_req = twitter_req_to_http_req(session,
                                                 app_cred,
                                                 client_cred,
                                                 twitter_req)

    async def __aiter__(self):
        self._resp = await self._http_req.__aenter__()  # I hate this.

        return self

    async def __anext__(self):
        # If there are no messages ready, read from the stream.
        while not self._entry_processor:
            chunk = await self._resp.content.read(4096)
            if not chunk:
                break
            self._entry_processor.append(chunk)

        # If there are no messages ready, the stream closed!
        if not self._entry_processor:
            self.close()
            raise StopAsyncIteration

        # Take one message.
        return self._entry_processor.take_one()

    def close(self):
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
