import aiohttp
import asyncio
import bz2
import json
import pytest
import os
from unittest.mock import Mock, MagicMock, patch
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit_core import TwitterError
from brittle_wit.streaming import (StreamProcessor,
                                   StreamingHTTPPipe,
                                   basic_streamer)
from brittle_wit.streaming.receivers import (StreamReceiver,
                                             flexible_open,
                                             FeedSerializer,
                                             PartitioningFeedSerializer,
                                             CallableStreamHandler)
from tests.helpers import mock_stream, async_ignore_sleep, MockHTTPResp


@pytest.mark.asyncio
async def test_streaming_http_pipe(event_loop, unused_tcp_port_factory):

    port = unused_tcp_port_factory()
    pipe = StreamingHTTPPipe()
    httpd = aiohttp.web.Application()
    httpd.router.add_get('/', pipe.handle)
    msgs = [b'abcdefghij', b'klmnopqrst', b'ABCDEFGHIJ', b'KLMNOPQRST']

    async def dispatch_msgs():
        for msg in msgs:
            pipe.send(msg)

    async def client(n_reads):
        collected = []

        async with aiohttp.ClientSession() as sess:
            async with sess.get('http://localhost:{}'.format(port)) as resp:
                assert resp.status == 200

                for i in range(n_reads):
                    collected.append(await resp.content.read(10))

                resp.close()

        return collected

    await event_loop.create_server(httpd.make_handler(), "localhost", port)

    alice = event_loop.create_task(client(3))
    bob = event_loop.create_task(client(4))

    await asyncio.sleep(0.1)  # XXX: Better way to make sure alice and bob run.

    await dispatch_msgs()

    assert await asyncio.wait_for(alice, 1) == msgs[:3]
    assert await asyncio.wait_for(bob, 1) == msgs[:4]


@pytest.mark.asyncio
async def test_streaming_http_pipe_onerr(event_loop, unused_tcp_port_factory):
    port = unused_tcp_port_factory()
    pipe = StreamingHTTPPipe()
    httpd = aiohttp.web.Application()
    httpd.router.add_get('/', pipe.handle)

    msgs = [b'abcdefghij', b'klmnopqrst', b'ABCDEFGHIJ', b'KLMNOPQRST']

    async def send_disconnects():
        for resp, _ in pipe._clients.values():
            await resp.write_eof()  # You can't do this. It will err.

    async def dispatch_msgs():
        for msg in msgs:
            pipe.send(msg)

    async def client(n_reads):
        collected = []

        async with aiohttp.ClientSession() as sess:
            async with sess.get('http://localhost:{}'.format(port)) as resp:
                assert resp.status == 200

                for i in range(n_reads):
                    data = await resp.content.read(10)
                    if data:
                        collected.append(data)

                resp.close()

        return collected

    await event_loop.create_server(httpd.make_handler(), "localhost", port)

    alice = event_loop.create_task(client(4))

    await asyncio.sleep(0.1)  # XXX: Better way to make sure alice and bob run.

    await send_disconnects()
    await dispatch_msgs()

    assert await asyncio.wait_for(alice, 9) == []

    # Try a new client and make sure it works!

    bob = event_loop.create_task(client(4))

    await asyncio.sleep(0.1)  # XXX: Better way to make sure alice and bob run.
    await dispatch_msgs()
    assert await asyncio.wait_for(bob, 9) == msgs[:4]
