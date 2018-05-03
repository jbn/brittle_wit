import aiohttp
import asyncio
import bz2
import json
import pytest
from unittest.mock import Mock, MagicMock, patch
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit_core import TwitterError
from brittle_wit.streaming import (StreamReceiver,
                                   FeedSerializer,
                                   PartitioningFeedSerializer,
                                   LambdaStreamHandler,
                                   StreamProcessor,
                                   StreamingHTTPPipe,
                                   basic_streamer)
from tests.helpers import mock_stream, async_ignore_sleep, MockHTTPResp

# XXX: WEAKREF?


def test_stream_receiver_close_does_nothing_for_base():
    StreamReceiver().close()


# -----------------------------------------------------------------------------

def test_feed_serializer(tmpdir):
    output_path = str(tmpdir.join("feed.jsonl"))
    messages = [[1, 2], [3, 4]]

    feed_serializer = FeedSerializer(output_path, True, False)

    for msg in messages:
        feed_serializer.send(msg)

    feed_serializer.close()

    with open(output_path, 'rb') as fp:
        res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
        assert res == messages


def test_feed_serializer_bz2(tmpdir):
    output_path = tmpdir.join("feed.jsonl.bz2")

    feed_serializer = FeedSerializer(str(output_path), as_bz2=True)

    messages = [[1, 2], [3, 4]]

    for msg in messages:
        feed_serializer.send(msg)

    feed_serializer.close()

    with bz2.open(str(output_path)) as fp:
        res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
        assert res == messages


def test_partitioning_feed_serializer(tmpdir):
    path = tmpdir.join("{}.jsonl")
    serializer = PartitioningFeedSerializer(5, str(path))
    for i in range(11):
        serializer.send({"i": i})

    files = tmpdir.listdir()
    assert len(files) == 3


# -----------------------------------------------------------------------------

def test_lambda_stream_handler():
    received = []
    rcvr = LambdaStreamHandler(lambda msg: received.append(msg))

    messages = [[1, 2], [3, 4]]
    for msg in messages:
        rcvr.send(msg)

    assert received == messages


# -----------------------------------------------------------------------------


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
