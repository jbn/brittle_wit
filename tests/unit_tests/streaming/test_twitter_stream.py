import pytest
from asyncio import TimeoutError
from brittle_wit_core import (AppCredentials,
                              ClientCredentials, TwitterRequest,
                              TwitterError)
from brittle_wit.streaming.twitter_stream import TwitterStream
from tests.helpers import mock_http_req, mock_content_reader


pytestmark = pytest.mark.asyncio
app_cred = AppCredentials("app", "secret")
client_cred = ClientCredentials(1, "client", "secret")


@pytest.fixture
def stream(mocker):
    return TwitterStream(mocker.MagicMock(),
                         app_cred,
                         client_cred,
                         mocker.MagicMock())


async def test_is_not_open_after_instantiation(stream, mocker):
    assert not stream.is_open()


async def test_no_double_connecting(stream, mocker):
    mocker.patch.object(stream, 'is_open', return_value=True)
    with pytest.raises(RuntimeError):
        stream._connect()


async def test_disconnect_closes_underlying_http_req(stream, mocker):
    http_req = mocker.MagicMock()
    stream._http_req = http_req
    stream._resp = 42

    stream.disconnect()

    assert http_req.close.called
    assert stream._http_req is None
    assert stream._resp is None


async def test_reconnect_purges_buffer_and_mailbox(stream, mocker):
    connect = mocker.patch.object(stream, '_connect')
    stream._entry_processor = mocker.MagicMock()

    stream.reconnect(clear_prior_messages=True)

    assert stream._entry_processor.purge_mailbox.called
    assert stream._entry_processor.purge_buffer.called


async def test_reconnect_forces_closure(stream, mocker):
    connect = mocker.patch.object(stream, '_connect')

    http_req = mocker.MagicMock()
    stream._http_req = http_req
    stream._resp = mocker.MagicMock()
    stream._resp.connection.closed = False

    stream.reconnect()

    assert http_req.close.called
    assert stream._http_req is None
    assert stream._resp is None

    connect.assert_called_once_with()


async def test_reconnect_errs_if_open(stream, mocker):
    connect = mocker.patch.object(stream, 'is_open', return_value=True)

    with pytest.raises(RuntimeError) as e:
        stream.reconnect(force_close_if_open=False)

    assert 'Already connected' in str(e)


async def test__aiter__connects_if_closed(stream, mocker):
    stream._resp = mocker.MagicMock()
    stream._resp.connection.closed = True
    stream._connect = mocker.MagicMock()
    stream._http_req = mock_http_req(200, False)

    await stream.__aiter__()
    stream._connect.assert_called_once_with()


async def test__aiter__gets_resp_if_none(stream, mocker):
    stream._resp = mocker.MagicMock()
    stream._resp.connection.closed = True
    stream._connect = mocker.MagicMock()
    stream._http_req = mock_http_req(200, False)

    await stream.__aiter__()
    stream._connect.assert_called_once_with()

    stream._resp = None
    assert await stream.__aiter__() is stream
    assert stream._resp is not None


async def test__aiter__300_status(stream, mocker):
    pred = mocker.patch.object(stream, 'is_open', return_value=True)

    stream._http_req = mock_http_req(500, True, 'mock text')

    with pytest.raises(TwitterError):
        await stream.__aiter__()

    pred.assert_called_once_with()


async def test__anext__(stream, mocker):
    messages = [b"this is a message\r\nthis is another\r\n"]

    stream._resp = mock_content_reader(messages)
    msg = await stream.__anext__()
    assert msg == b"this is a message"

    msg = await stream.__anext__()
    assert msg == b"this is another"

    with pytest.raises(StopAsyncIteration):
        msg = await stream.__anext__()


async def test_read_hang_timeout_for__anext__(stream):
    stream._read_hang_timeout = 0.001
    messages = [b"this is a message\r\nthis is another\r\n"]

    stream._resp = mock_content_reader(messages, delay=0.05)
    with pytest.raises(TimeoutError):
        msg = await stream.__anext__()
