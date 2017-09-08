import os
import unittest
import brittle_wit as bw
import brittle_wit.rest_api as rest_api
from test.helpers import load_fixture_txt, drive_coro_once
from brittle_wit_core import TwitterError
from brittle_wit.helpers import (parse_datetime, grouping,
                                 linear_backoff, expon_backoff, retrying,
                                 _twitter_request_html_repr)

def failure_script(ret_val, *failure_schedule):
    failure_schedule = list(failure_schedule)

    async def _f():
        if not failure_schedule:
            return ret_val
        else:
            raise failure_schedule.pop(0)
    return _f


def make_twitter_error(status_code):
    resp = unittest.mock.MagicMock()
    resp.status = status_code
    return TwitterError(None, None, resp, "none")


class TestHelpers(unittest.TestCase):

    def test_parse_datetime(self):
        s = "tue mar 29 15:40:03 +0000 2016"
        self.assertEqual(parse_datetime(s).timestamp(), 1459266003.0)

    def test_grouping(self):
        items = list(range(7))
        expected = [[0, 1, 2], [3, 4, 5], [6]]
        self.assertEqual(list(grouping(items, 3)), expected)

    def test_linear_backoff(self):
        self.assertEqual(linear_backoff(3, 60), 180)

    def test_expon_backoff(self):
        self.assertEqual(expon_backoff(3, 60), 240)

    def test_retrying_on_no_failures(self):
        coro = failure_script(True)
        self.assertTrue(drive_coro_once(retrying(coro, 1)))

    def test_retrying_non_retryable(self):
        err = make_twitter_error(1)
        coro = failure_script(True, err)
        with self.assertRaises(TwitterError):
            self.assertTrue(drive_coro_once(retrying(coro, 2)))

    def test_retrying_after_one_failure_tries_left(self):
        err = make_twitter_error(500)
        coro = failure_script(True, err)
        self.assertTrue(drive_coro_once(retrying(coro, 2, sleep_time=0)))

    def test_retrying_after_one_failure_after_all_tries(self):
        err = make_twitter_error(500)
        coro = failure_script(True, err)
        with self.assertRaises(TwitterError):
            self.assertTrue(drive_coro_once(retrying(coro, 1)))

    def test_retrying_given_known_retryable_codes(self):
        # Be overly cautious with this test. It's hard to test services!
        for code in [500, 502, 503, 504]:
            err = make_twitter_error(code)
            coro = failure_script(True, err)
            with self.assertRaises(TwitterError):
                self.assertTrue(drive_coro_once(retrying(coro, 1)))



class TestIPythonHelpers(unittest.TestCase):

    def test_twitter_request_html_repr(self):
        expected = load_fixture_txt("ipython_html.html")
        req = rest_api.direct_messages.new("hello world")
        self.assertEqual(_twitter_request_html_repr(req).strip(),
                         expected.strip())
