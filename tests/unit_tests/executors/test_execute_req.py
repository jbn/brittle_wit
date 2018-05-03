import pytest
import random
from unittest.mock import MagicMock, patch

from brittle_wit_core import (TwitterRequest, TwitterError, TwitterResponse,
                              AppCredentials, ClientCredentials)
from brittle_wit.rate_limit import RateLimit
from brittle_wit.executors import execute_req
from tests.helpers import MockHTTPReq, MockHTTPResp


pytestmark = pytest.mark.asyncio
client_cred = ClientCredentials(1, "client", "secret")


@pytest.fixture
def twitter_req():
    return TwitterRequest("method", "url", "family", "service")


async def test_good_resp_and_json_body(twitter_req):
    rate_limit = RateLimit.from_ignorance()
    http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))

    res = await execute_req(client_cred, twitter_req, http_req, rate_limit)

    assert isinstance(res, TwitterResponse)
    assert res.body['count'] == 100


async def test_good_resp_and_text_body():
    twitter_req.parse_as = 'text'
    rate_limit = RateLimit.from_ignorance()
    http_req = MockHTTPReq(MockHTTPResp(200, {}, "hello world"))

    coro = execute_req(client_cred, twitter_req, http_req, rate_limit)
    res = await coro
    assert isinstance(res, TwitterResponse)
    assert res.body == "hello world"


async def test_bad_resp():
    twitter_req.parse_as = 'text'
    rate_limit = RateLimit.from_ignorance()
    http_req = MockHTTPReq(MockHTTPResp(403, {}, "Forbidden"))

    coro = execute_req(client_cred, twitter_req, http_req, rate_limit)
    with pytest.raises(TwitterError):
        await coro
