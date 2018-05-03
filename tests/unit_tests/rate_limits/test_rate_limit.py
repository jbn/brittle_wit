import time
import pytest
from datetime import datetime
from brittle_wit.rate_limit import RateLimit, TimingRateLimiter
from tests.helpers import mock_resp, async_patch


def test_from_ignorance():
    rate_limit = RateLimit.from_ignorance()
    assert not rate_limit.is_exhausted


def test_from_initial_limit():
    rate_limit = RateLimit.from_initial_limit(10)
    assert rate_limit._remaining == 10


def test_from_response():
    resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                      'X-RATE-LIMIT-REMAINING': 99,
                      'X-RATE-LIMIT-RESET': 9999})
    rate_limit = RateLimit.from_response(resp)
    local_dt = datetime.fromtimestamp(9999).strftime("%H:%M:%S")
    expected = "RateLimit(limit=100, remaining=99, reset_time={})"
    expected = expected.format(local_dt)

    assert rate_limit.reset_time == 9999
    assert rate_limit.__repr__() == expected
    assert str(rate_limit) == expected


def test_is_pristine():
    resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                      'X-RATE-LIMIT-REMAINING': 100,
                      'X-RATE-LIMIT-RESET': 9999})
    rate_limit = RateLimit.from_response(resp)
    assert rate_limit.is_pristine

    resp = mock_resp({'X-RATE-LIMIT-REMAINING': 99})
    rate_limit.update(resp)
    assert not rate_limit.is_pristine


def test_is_exhausted():
    rate_limit = RateLimit.from_ignorance()
    assert not rate_limit.is_exhausted

    resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                      'X-RATE-LIMIT-REMAINING': 0,
                      'X-RATE-LIMIT-RESET': 9999})

    rate_limit.update(resp)
    assert rate_limit.is_exhausted


def test_bad_request_update():
    orig_resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                           'X-RATE-LIMIT-REMAINING': 99,
                           'X-RATE-LIMIT-RESET': 9999})

    rate_limit = RateLimit.from_response(orig_resp)
    assert not rate_limit.is_exhausted
    rate_limit.update(mock_resp({}))


def test_mark_exhausted():
    orig_resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                           'X-RATE-LIMIT-REMAINING': 99,
                           'X-RATE-LIMIT-RESET': 9999})

    rate_limit = RateLimit.from_ignorance()
    assert not rate_limit.is_exhausted
    rate_limit.mark_exhausted(orig_resp)
    assert rate_limit.is_exhausted


@pytest.mark.asyncio
async def test_comply_without_sleeping():
    rate_limit = RateLimit.from_ignorance()
    assert not rate_limit.is_exhausted
    await rate_limit.comply()
    assert rate_limit.is_exhausted

    rate_limit.update(mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                                 'X-RATE-LIMIT-REMAINING': 0,
                                 'X-RATE-LIMIT-RESET': time.time() + 0.1}))
    assert rate_limit.is_exhausted
    await rate_limit.comply()
    assert not rate_limit.is_exhausted


@pytest.mark.asyncio
async def test_comply_with_sleeping():
    rate_limit = RateLimit.from_ignorance()
    assert not rate_limit.is_exhausted

    await rate_limit.comply()
    assert rate_limit.is_exhausted

    rate_limit.update(mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                                 'X-RATE-LIMIT-REMAINING': 0,
                                 'X-RATE-LIMIT-RESET': time.time() + 360}))
    assert rate_limit.is_exhausted

    with async_patch('asyncio.sleep') as f:
        await rate_limit.comply()
    time_slept = f.call_args[0][0]
    assert time_slept < 360 + 5
    assert time_slept > 360 - 5
    assert not rate_limit.is_exhausted
