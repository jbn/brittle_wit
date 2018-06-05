import aiohttp
import pytest
from brittle_wit_core import TwitterRequest, AppCredentials, ClientCredentials
from brittle_wit.executors import twitter_req_to_http_req
from tests.helpers import *


app_cred = AppCredentials("app", "secret")
client_cred = ClientCredentials(1, "client", "secret")


# -----------------------------------------------------------------------------
# This are weak tests but they should help prevent trivial regressions.
# -----------------------------------------------------------------------------


@pytest.mark.asyncio
@pytest.mark.usefixtures('ignore_unawaited_request')
async def test_twitter_req_to_http_req_get():
    tr = TwitterRequest("GET", "http://url.com/", "service", "family")
    async with aiohttp.ClientSession() as session:
        req = twitter_req_to_http_req(session, app_cred, client_cred, tr)
        assert isinstance(req, aiohttp.client._RequestContextManager)


@pytest.mark.asyncio
@pytest.mark.usefixtures('ignore_unawaited_request')
async def test_twitter_req_to_http_req_post():
    tr = TwitterRequest("POST", "http://url.com/", "service", "family")
    async with aiohttp.ClientSession() as session:
        req = twitter_req_to_http_req(session, app_cred, client_cred, tr)
        assert isinstance(req, aiohttp.client._RequestContextManager)
