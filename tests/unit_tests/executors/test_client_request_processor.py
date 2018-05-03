import pytest
import asyncio
import time
from brittle_wit_core import (AppCredentials, ClientCredentials,
                              TwitterRequest, TwitterResponse, TwitterError)
from brittle_wit.executors import ClientRequestProcessor
from brittle_wit.rate_limit import RateLimit
from tests.helpers import MockHTTPReq, MockHTTPResp


app_cred = AppCredentials("key", "secret")
client_cred = ClientCredentials(2, "token-bob", "****")


@pytest.fixture
def processor():
    return ClientRequestProcessor(client_cred)


def test_properties(processor):
    assert processor.user_id == 2


def test_is_removable_after_init(processor):
    assert processor.is_removable()


def test_is_removable_when_processing(processor, mocker):
    mgr = mocker.MagicMock()
    mgr.all_chains_empty = lambda: False
    processor._chain_manager = mgr

    # It's waiting for a ticket to make a request.
    assert not processor.is_removable()


def test_is_removable_when_rate_limited(processor):
    processor._rate_limits['svc'] = RateLimit.from_initial_limit(0)
    assert not processor.is_removable()


def test_is_not_processing_on_init(processor):
    assert processor.is_not_processing()


def test_is_processing_when_waiting_for_crit_region(processor, mocker):
    mgr = mocker.MagicMock()
    mgr.all_chains_empty = lambda: False
    processor._chain_manager = mgr

    # It's waiting for a ticket to make a request.
    assert not processor.is_not_processing()


def test_is_immediately_available_for_when_no_line_and_no_limit(processor):
    assert processor.is_immediately_available_for('svc')


def test_is_immediately_available_for_when_cur_on_line(processor, mocker):
    mgr = mocker.MagicMock()
    mgr.is_chain_empty = lambda _: False
    processor._chain_manager = mgr

    assert not processor.is_immediately_available_for('svc')


def test_is_immediately_available_for_when_no_line_and_exhausted(processor):
    processor._rate_limits['svc'] = RateLimit.from_initial_limit(0)
    assert not processor.is_immediately_available_for('svc')


def test_is_immediately_available_for_when_no_line_and_not_exhaust(processor):
    processor._rate_limits['svc'] = RateLimit.from_ignorance()
    assert processor.is_immediately_available_for('svc')


def test_is_immediately_available_for_when_line_not_empty(processor, mocker):
    svc = "direct_message"
    assert processor.is_immediately_available_for(svc)

    limit = RateLimit.from_ignorance()
    limit._remaining = 0
    processor._rate_limits[svc] = limit
    assert not processor.is_immediately_available_for(svc)

    tm = mocker.MagicMock()
    tm.is_line_empty = lambda s: False
    processor._ticket_master = tm
    assert not processor.is_immediately_available_for(svc)


def test_rate_limit_for_doesnt_duplicate_on_same_service(processor):
    limit = processor._rate_limit_for("direct_messages")
    assert isinstance(limit, RateLimit)  # Sane

    assert limit is processor._rate_limit_for("direct_messages")


def test_rate_limit_for_unique_for_diff_service(processor):
    dm_limit = processor._rate_limit_for("direct_messages")
    settings_limit = processor._rate_limit_for("account/settings")

    assert isinstance(dm_limit, RateLimit)  # Sane
    assert isinstance(settings_limit, RateLimit)  # Sane.
    assert dm_limit is not settings_limit


def test_rate_limit_for_is_initially_prestine(processor):
    limit = processor._rate_limit_for("direct_messages")
    assert limit.is_pristine


def test_cleanup_with_no_rate_limits(processor):
    assert not processor._rate_limits
    processor.cleanup()
    assert not processor._rate_limits


def test_cleanup_with_stale_rate_limit(processor):
    now = time.time()
    processor._rate_limits['past'] = RateLimit(1, 1, now - 100)
    processor.cleanup(now)
    assert processor.is_removable()


def test_cleanup_with_mixed_rate_limits(processor):
    now = time.time()
    processor._rate_limits['future'] = RateLimit(1, 1, now + 100)
    processor._rate_limits['past'] = RateLimit(1, 1, now - 100)
    assert set(processor._rate_limits), {'future', 'past'}

    processor.cleanup(now)

    assert not processor.is_removable()
    assert set(processor._rate_limits), {'future'}


class RateLimitKludge:
    # XXX: TODO: REFACTOR
    # This is a kludge that lets me test the execute.
    # It's extremely implementation dependent, and generally a shit idea.

    def __init__(self, twitter_req, client_cred=None, fail_queue=None, sleep_time=None):
        self.twitter_req = twitter_req
        self.client_cred = client_cred
        self.fail_queue = fail_queue
        self.sleep_time = sleep_time

    async def comply(self):
        await asyncio.sleep(10)

    def update(self, _):
        pass

    async def comply(self):
        if self.fail_queue is not None and self.fail_queue.pop(0):
            resp = MockHTTPResp(500, {}, "")
            raise TwitterError(self.client_cred, self.twitter_req, resp, "")

        if self.sleep_time is not None:
            await asyncio.sleep(self.sleep_time)


@pytest.mark.asyncio
async def test__execute_prestine(processor, mocker):
    rate_limit = RateLimit.from_ignorance()
    processor = ClientRequestProcessor(client_cred)
    http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))

    twitter_req = TwitterRequest("method", "url", "family", "service")
    coro = processor._execute('session', app_cred, twitter_req)
    func_path = 'brittle_wit.executors.twitter_req_to_http_req'
    req_to_http_req = mocker.patch(func_path, return_value=http_req)

    resp = await coro

    req_to_http_req.assert_called_with('session',
                                       app_cred,
                                       client_cred,
                                       twitter_req)

    assert type(resp) is TwitterResponse
    assert resp.body['count'] == 100


@pytest.mark.asyncio
async def test__execute_timeout_thrown(processor):
    twitter_req = TwitterRequest("method", "url", "family", "service")
    coro = processor._execute('session', app_cred, twitter_req, 0.01)
    processor._rate_limits['service'] = RateLimitKludge(twitter_req, client_cred, sleep_time=1)

    with pytest.raises(asyncio.TimeoutError):
        await coro


@pytest.mark.asyncio
async def test_execute_retrying(processor, mocker):
    twitter_req = TwitterRequest("method", "url", "family", "service")
    http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))
    fail_queue = [True, False]

    processor._rate_limits['service'] = RateLimitKludge(twitter_req, client_cred, fail_queue)
    func_path = 'brittle_wit.executors.twitter_req_to_http_req'
    coro = processor.execute('session', app_cred, twitter_req, sleep_time=0.01)
    req_to_http_req = mocker.patch(func_path, return_value=http_req)
    resp = await coro
    assert type(resp) is TwitterResponse
    assert resp.body['count'] == 100
    assert fail_queue == []


@pytest.mark.asyncio
async def test_execute_retrying_too_many_failures(processor, mocker):
    twitter_req = TwitterRequest("method", "url", "family", "service")
    http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))
    fail_queue = [True] * 6

    processor._rate_limits['service'] = RateLimitKludge(twitter_req, client_cred, fail_queue)
    func_path = 'brittle_wit.executors.twitter_req_to_http_req'
    coro = processor.execute('session', app_cred, twitter_req, sleep_time=0.01)
    req_to_http_req = mocker.patch(func_path, return_value=http_req)
    with pytest.raises(TwitterError):
        resp = await coro
