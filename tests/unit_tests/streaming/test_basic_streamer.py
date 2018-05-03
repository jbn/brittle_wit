import pytest
from brittle_wit.streaming import basic_streamer
from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from tests.helpers import mock_stream, async_ignore_sleep, MockHTTPResp
import brittle_wit.streaming_api


app_cred = AppCredentials("app", "secret")
client_cred = ClientCredentials(1, "client", "secret")


@pytest.mark.asyncio
async def test_basic_streamer(mocker):
    twitter_req = brittle_wit.streaming_api.statuses.sample()
    callback = mocker.Mock()
    expected = [b'{"status": "a"}',
                b'{"status": "b"}',
                RuntimeError('Sentinel')]
    stream = mock_stream(expected)

    mocker.patch('brittle_wit.streaming.TwitterStream', return_value=stream)

    with pytest.raises(RuntimeError) as e:
        await basic_streamer(app_cred, client_cred, twitter_req, callback)
    assert 'Sentinel' in str(e)
    callbacks = [call[0][0] for call in callback.call_args_list]
    assert [{'status': "a"}, {'status': "b"}] == callbacks
