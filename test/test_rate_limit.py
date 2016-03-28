import time
import unittest
import asyncio
from collections import namedtuple
from brittle_wit.rate_limit import RateLimit


MockResp = namedtuple("MockResp", "headers")


def drive_coro_once(coro):
    # XXX: Make this prettier. Create a new loop or something.
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(coro)


class TestOAuth(unittest.TestCase):

    def test_from_ignorance(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

    def test_from_response(self):
        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 99,
                         'X-RATE-LIMIT-RESET': 9999})
        rate_limit = RateLimit.from_response(resp)
        expected = "RateLimit(limit=100, remaining=99, reset_time=21:46:39)"

        self.assertEqual(str(rate_limit), expected)
        self.assertEqual(rate_limit.__repr__(), expected)
        self.assertEqual(rate_limit.reset_time, 9999)

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

    def test_comply_without_sleeping(self):
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)
        drive_coro_once(rate_limit.comply())
        self.assertTrue(rate_limit.is_exhausted)

        rate_limit.update(MockResp({'X-RATE-LIMIT-LIMIT': 100,
                                    'X-RATE-LIMIT-REMAINING': 0,
                                    'X-RATE-LIMIT-RESET': time.time() + 2}))
        self.assertTrue(rate_limit.is_exhausted)
        drive_coro_once(rate_limit.comply())
        self.assertFalse(rate_limit.is_exhausted)

