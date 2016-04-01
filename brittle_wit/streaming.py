import json
import aiohttp
import asyncio

from brittle_wit.executors import twitter_req_to_http_req


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
