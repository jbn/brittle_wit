import time
import unittest
from brittle_wit.rate_limit import RateLimit, TimingRateLimiter
from test.helpers import *


class TestRateLimit(unittest.TestCase):

    def test_from_ignorance(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

    def test_from_initial_limit(self):
        rate_limit = RateLimit.from_initial_limit(10)
        self.assertEqual(rate_limit._remaining, 10)

    def test_from_response(self):
        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 99,
                         'X-RATE-LIMIT-RESET': 9999})
        rate_limit = RateLimit.from_response(resp)
        expected = "RateLimit(limit=100, remaining=99, reset_time=21:46:39)"

        self.assertEqual(str(rate_limit), expected)
        self.assertEqual(rate_limit.__repr__(), expected)
        self.assertEqual(rate_limit.reset_time, 9999)

    def test_is_pristine(self):
        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 100,
                         'X-RATE-LIMIT-RESET': 9999})
        rate_limit = RateLimit.from_response(resp)
        self.assertTrue(rate_limit.is_pristine)

        resp = MockResp({'X-RATE-LIMIT-REMAINING': 99})
        rate_limit.update(resp)
        self.assertFalse(rate_limit.is_pristine)

    def test_is_exhausted(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 0,
                         'X-RATE-LIMIT-RESET': 9999})

        rate_limit.update(resp)
        self.assertTrue(rate_limit.is_exhausted)

    def test_bad_request_update(self):
        orig_resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                              'X-RATE-LIMIT-REMAINING': 99,
                              'X-RATE-LIMIT-RESET': 9999})

        rate_limit = RateLimit.from_response(orig_resp)
        self.assertFalse(rate_limit.is_exhausted)
        rate_limit.update(MockResp({}))

    def test_mark_exhausted(self):
        orig_resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                              'X-RATE-LIMIT-REMAINING': 99,
                              'X-RATE-LIMIT-RESET': 9999})

        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)
        rate_limit.mark_exhausted(orig_resp)
        self.assertTrue(rate_limit.is_exhausted)

    def test_comply_without_sleeping(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)
        drive_coro_once(rate_limit.comply())
        self.assertTrue(rate_limit.is_exhausted)

        rate_limit.update(MockResp({'X-RATE-LIMIT-LIMIT': 100,
                                    'X-RATE-LIMIT-REMAINING': 0,
                                    'X-RATE-LIMIT-RESET': time.time() + 0.1}))
        self.assertTrue(rate_limit.is_exhausted)
        drive_coro_once(rate_limit.comply())
        self.assertFalse(rate_limit.is_exhausted)


class TestTimingRateLimiter(unittest.TestCase):
    def test_timing_rate_limiter(self):
        limiter = TimingRateLimiter(60)
        self.assertTrue(limiter.can_proceed())
        self.assertFalse(limiter.can_proceed())

        limiter._start_time -= 61
        self.assertTrue(limiter.can_proceed())
