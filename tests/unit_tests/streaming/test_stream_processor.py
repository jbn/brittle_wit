import pytest
import bz2
from unittest.mock import Mock, MagicMock, patch
import json
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit_core import TwitterError
from brittle_wit.streaming import (StreamReceiver,
                                   FeedSerializer,
                                   CallableStreamHandler,
                                   StreamProcessor,
                                   StreamingHTTPPipe,
                                   basic_streamer)
from tests.helpers import mock_stream, async_ignore_sleep, MockHTTPResp


def test_subscribe_raw():
    sp = StreamProcessor(None)

    sp.subscribe(CallableStreamHandler(lambda m: -1), as_json=False)

    assert not sp.requires_json


def test_subscribe_json():
    sp = StreamProcessor(None)

    sp.subscribe(CallableStreamHandler(lambda m: -1), as_json=True)

    assert sp.requires_json


def test_subscribe_receiver_must_implement_send():
    sp = StreamProcessor(None)
    with pytest.raises(AttributeError):
        sp.subscribe(None, True)


def test_no_duplicate_subscriptions():
    sp = StreamProcessor(None)
    handler = CallableStreamHandler(lambda m: -1)

    sp.subscribe(handler, True)
    with pytest.raises(RuntimeError):
        sp.subscribe(handler, True)


def test_unsubscribe_tracks_need_for_json():
    sp = StreamProcessor(None)

    json_handler = CallableStreamHandler(lambda m: -1)
    byte_handler = CallableStreamHandler(lambda m: -1)

    sp.subscribe(json_handler, True)
    sp.subscribe(byte_handler, False)

    assert sp.requires_json
    sp.unsubscribe(json_handler)
    assert not sp.requires_json


def test_no_unsubscribe_twice():
    sp = StreamProcessor(None)

    json_handler = CallableStreamHandler(lambda m: -1)
    byte_handler = CallableStreamHandler(lambda m: -1)

    sp.subscribe(json_handler, True)
    sp.unsubscribe(json_handler)

    with pytest.raises(RuntimeError):
        sp.unsubscribe(json_handler)


def test_receiving_multi():
    sp = StreamProcessor(None)

    byte_msgs, json_msgs = [], []
    json_handler = CallableStreamHandler(lambda m: json_msgs.append(m))
    byte_handler = CallableStreamHandler(lambda m: byte_msgs.append(m))
    sp.subscribe(byte_handler, False)
    sp.subscribe(json_handler, True)

    messages = [[1, 2, 3], [4, 5, 6]]
    for msg in messages:
        sp._send_to_all(json.dumps(msg).encode())

    assert json_msgs == messages
    assert byte_msgs, [json.dumps(m).encode() for m in messages]


@pytest.mark.asyncio
async def test_stream_to_subscribers():
    expected = [b"a", b"b"]

    sp = StreamProcessor(None)
    byte_msgs = []
    byte_handler = CallableStreamHandler(lambda m: byte_msgs.append(m))
    sp._twitter_stream = mock_stream(expected)
    sp.subscribe(byte_handler, False)
    await sp._stream_to_subscribers()
    assert byte_msgs == expected


@pytest.mark.asyncio
async def test_run_aborts_on_keyboard_interrupt():
    sp = StreamProcessor(None)
    sp._twitter_stream = mock_stream([KeyboardInterrupt()])
    with pytest.raises(KeyboardInterrupt):
        await sp.run()


@pytest.mark.asyncio
async def test_run_reraises_unguarded_exception():
    sp = StreamProcessor(None)
    sp._twitter_stream = mock_stream([AttributeError()])
    with pytest.raises(AttributeError):
        await sp.run()


async def _assert_run_expectations(expected, messages, **overrides):
    sp = StreamProcessor(mock_stream(messages))
    for k, v in overrides.items():
        setattr(sp, k, v)

    with async_ignore_sleep() as sleep_times:
        with patch.object(sp._twitter_stream, 'disconnect') as disconnect:
            with pytest.raises(RuntimeError) as e:
                await sp.run()
            assert "Sentinel" in str(e)

        assert len(disconnect.call_args_list) == len(expected)
        assert sleep_times() == expected


@pytest.mark.asyncio
async def test_run_on_timeout_error():
    import asyncio
    expected = [min(0.25 * i, 16.0) for i in range(1, 66)]
    messages = ([asyncio.TimeoutError()] * len(expected) +
                [RuntimeError("Sentinel")])
    await _assert_run_expectations(expected, messages)


@pytest.mark.asyncio
async def test_run_on_client_error():
    import aiohttp
    expected = [min(0.25 * i, 16.0) for i in range(1, 66)]
    messages = ([aiohttp.ClientError()] * len(expected) +
                [RuntimeError("Sentinel")])
    await _assert_run_expectations(expected, messages)


@pytest.mark.asyncio
async def test_run_on_420_error():
    err = TwitterError(None, None, MockHTTPResp(420, [], None), '')
    expected = [60, 120, 240, 480, 960, 960]
    messages = ([err] * len(expected) + [RuntimeError("Sentinel")])
    await _assert_run_expectations(expected, messages)


@pytest.mark.asyncio
async def test_run_on_other_twitter_error():
    err = TwitterError(None, None, MockHTTPResp(500, [], None), '')
    expected = [5, 10, 20, 40, 80, 160, 320, 320]
    messages = ([err] * len(expected) + [RuntimeError("Sentinel")])
    await _assert_run_expectations(expected, messages)


@pytest.mark.asyncio
async def test_run_on_rate_limit():
    err = TwitterError(None, None, MockHTTPResp(429, [], None), '')
    expected = [42] * 3
    messages = ([err] * len(expected) + [RuntimeError("Sentinel")])

    mock_limit = Mock()
    mock_limit.sleep_time_remaining = 42
    with patch('brittle_wit.rate_limit.RateLimit.from_response', return_value=mock_limit):
        await _assert_run_expectations(expected, messages, _resp=None)
