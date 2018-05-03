import os
import pytest
import brittle_wit as bw
import brittle_wit.rest_api as rest_api
from tests.helpers import load_fixture_txt, AsyncSafeTestCase
from brittle_wit_core import TwitterError
from brittle_wit.helpers import (parse_datetime, grouping, running_task_names,
                                 linear_backoff, expon_backoff, retrying,
                                 _twitter_request_html_repr, CircularQueue)


def failure_script(ret_val, *failure_schedule):
    failure_schedule = list(failure_schedule)

    async def _f():
        if not failure_schedule:
            return ret_val
        else:
            raise failure_schedule.pop(0)
    return _f


def make_twitter_error(status_code, mocker):
    resp = mocker.MagicMock()
    resp.status = status_code
    return TwitterError(None, None, resp, "none")


def test_parse_datetime():
    s = "tue mar 29 15:40:03 +0000 2016"
    assert parse_datetime(s).timestamp() == 1459266003.0


def test_grouping():
    items = list(range(7))
    expected = [[0, 1, 2], [3, 4, 5], [6]]
    assert list(grouping(items, 3)) == expected


def test_linear_backoff():
    assert linear_backoff(3, 60) == 180


def test_expon_backoff():
    assert expon_backoff(3, 60) == 240


@pytest.mark.asyncio
async def test_retrying_on_no_failures():
    coro = failure_script(True)
    assert await retrying(coro, 1)


@pytest.mark.asyncio
async def test_retrying_non_retryable(mocker):
    err = make_twitter_error(1, mocker)
    coro = failure_script(True, err)
    with pytest.raises(TwitterError):
        assert await retrying(coro, 2)


@pytest.mark.asyncio
async def test_retrying_after_one_failure_tries_left(mocker):
    err = make_twitter_error(500, mocker)
    coro = failure_script(True, err)
    assert await retrying(coro, 2, sleep_time=0)


@pytest.mark.asyncio
async def test_retrying_after_one_failure_after_all_tries(mocker):
    err = make_twitter_error(500, mocker)
    coro = failure_script(True, err)
    with pytest.raises(TwitterError):
        assert await retrying(coro, 1)


@pytest.mark.asyncio
async def test_retrying_given_known_retryable_codes(mocker):
    # Be overly cautious with this test. It's hard to test services!
    for code in [500, 502, 503, 504]:
        err = make_twitter_error(code, mocker)
        coro = failure_script(True, err)
        with pytest.raises(TwitterError):
            assert await retrying(coro, 1)


@pytest.mark.asyncio
async def test_running_task_names():
    assert ['test_running_task_names'] == running_task_names()
