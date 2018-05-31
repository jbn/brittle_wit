import json
import pytest
import os
from brittle_wit.streaming.receivers import (StreamReceiver,
                                             flexible_open,
                                             FeedSerializer,
                                             PartitioningFeedSerializer,
                                             CallableStreamHandler)


def test_stream_receiver_send_does_nothing_for_base():
    StreamReceiver().send(b"asdf")


def test_stream_receiver_close_does_nothing_for_base():
    StreamReceiver().close()


@pytest.mark.parametrize('extension', ['bz2', 'gz', 'xz', 'txt'])
def test_flexible_open(tmpdir, extension):
    output_path = str(tmpdir.join("hello." + extension))

    # Open.
    with flexible_open(output_path) as fp:
        fp.write(b"hello world")
    size = os.path.getsize(output_path)
    assert size > 0

    # Append.
    with flexible_open(output_path) as fp:
        fp.write(b"hello world")
    assert os.path.getsize(output_path) > size

    # Overwrite.
    with flexible_open(output_path, append=False) as fp:
        fp.write(b"hello")
    assert os.path.getsize(output_path) < size


def test_feed_serializer(tmpdir):
    output_path = str(tmpdir.join("feed.jsonl"))
    messages = [[1, 2], [3, 4]]

    feed_serializer = FeedSerializer(output_path)

    for msg in messages:
        feed_serializer.send(msg)

    feed_serializer.close()

    with open(output_path, 'rb') as fp:
        res = [json.loads(s.decode('utf8')) for s in fp.readlines()]
        assert res == messages


def test_partitioning_feed_serializer(tmpdir):
    path = tmpdir.join("{}.jsonl")
    serializer = PartitioningFeedSerializer(5, str(path))
    for i in range(11):
        serializer.send({"i": i})

    files = tmpdir.listdir()
    assert len(files) == 3


def test_callable_stream_handler():
    received = []
    rcvr = CallableStreamHandler(lambda msg: received.append(msg))

    messages = [[1, 2], [3, 4]]
    for msg in messages:
        rcvr.send(msg)

    assert received == messages
