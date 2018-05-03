from brittle_wit_core import AppCredentials, ClientCredentials, TwitterRequest
from brittle_wit.executors import debug_blocking_request


def test_debug_blocking_request(mocker):
    app_cred = AppCredentials("key", "secret")
    client_cred = ClientCredentials(1, "token-alice", "****")
    twitter_req = TwitterRequest("method", "url", "family", "service")

    f = mocker.patch('requests.request', return_value=42)
    res = debug_blocking_request(app_cred, client_cred, twitter_req)
    assert res == 42
