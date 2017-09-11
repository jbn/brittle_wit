import time
import unittest
from unittest.mock import patch
from datetime import datetime
from brittle_wit.rate_limit import RateLimit, TimingRateLimiter
from test.helpers import *


class TestRateLimit(AsyncSafeTestCase):

    def test_from_ignorance(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

    def test_from_initial_limit(self):
        rate_limit = RateLimit.from_initial_limit(10)
        self.assertEqual(rate_limit._remaining, 10)

    def test_from_response(self):
        resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                          'X-RATE-LIMIT-REMAINING': 99,
                          'X-RATE-LIMIT-RESET': 9999})
        rate_limit = RateLimit.from_response(resp)
        local_dt = datetime.fromtimestamp(9999).strftime("%H:%M:%S")
        expected = "RateLimit(limit=100, remaining=99, reset_time={})"
        expected = expected.format(local_dt)

        self.assertEqual(rate_limit.reset_time, 9999)
        self.assertEqual(rate_limit.__repr__(), expected)
        self.assertEqual(str(rate_limit), expected)

    def test_is_pristine(self):
        resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                          'X-RATE-LIMIT-REMAINING': 100,
                          'X-RATE-LIMIT-RESET': 9999})
        rate_limit = RateLimit.from_response(resp)
        self.assertTrue(rate_limit.is_pristine)

        resp = mock_resp({'X-RATE-LIMIT-REMAINING': 99})
        rate_limit.update(resp)
        self.assertFalse(rate_limit.is_pristine)

    def test_is_exhausted(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

        resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                          'X-RATE-LIMIT-REMAINING': 0,
                          'X-RATE-LIMIT-RESET': 9999})

        rate_limit.update(resp)
        self.assertTrue(rate_limit.is_exhausted)

    def test_bad_request_update(self):
        orig_resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                               'X-RATE-LIMIT-REMAINING': 99,
                               'X-RATE-LIMIT-RESET': 9999})

        rate_limit = RateLimit.from_response(orig_resp)
        self.assertFalse(rate_limit.is_exhausted)
        rate_limit.update(mock_resp({}))

    def test_mark_exhausted(self):
        orig_resp = mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                               'X-RATE-LIMIT-REMAINING': 99,
                               'X-RATE-LIMIT-RESET': 9999})

        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)
        rate_limit.mark_exhausted(orig_resp)
        self.assertTrue(rate_limit.is_exhausted)

    async def test_comply_without_sleeping(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)
        await rate_limit.comply()
        self.assertTrue(rate_limit.is_exhausted)

        rate_limit.update(mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                                     'X-RATE-LIMIT-REMAINING': 0,
                                     'X-RATE-LIMIT-RESET': time.time() + 0.1}))
        self.assertTrue(rate_limit.is_exhausted)
        await rate_limit.comply()
        self.assertFalse(rate_limit.is_exhausted)

    async def test_comply_with_sleeping(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

        await rate_limit.comply()
        self.assertTrue(rate_limit.is_exhausted)

        rate_limit.update(mock_resp({'X-RATE-LIMIT-LIMIT': 100,
                                     'X-RATE-LIMIT-REMAINING': 0,
                                     'X-RATE-LIMIT-RESET': time.time() + 360}))
        self.assertTrue(rate_limit.is_exhausted)

        with async_patch('asyncio.sleep') as f:
            await rate_limit.comply()
        time_slept = f.call_args[0][0]
        self.assertLess(time_slept, 360 + 5)
        self.assertGreater(time_slept, 360 - 5)
        self.assertFalse(rate_limit.is_exhausted)


class TestTimingRateLimiter(unittest.TestCase):

    def test_timing_rate_limiter(self):
        limiter = TimingRateLimiter(60)
        self.assertTrue(limiter.can_proceed())
        self.assertFalse(limiter.can_proceed())

        limiter._start_time -= 61
        self.assertTrue(limiter.can_proceed())


if __name__ == '__main__':
    unittest.main()
