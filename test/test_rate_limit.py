import time
import unittest
from brittle_wit.oauth import ClientCredentials, AppCredentials
from brittle_wit.rate_limit import RateLimit, RateLimitError
from brittle_wit.twitter_request import TwitterRequest
from test.helpers import *


class TestRateLimitError(unittest.TestCase):

    def test_rate_limit_error_for_client_cred(self):
        client_cred = ClientCredentials(1, "token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM")

        err = RateLimitError(client_cred, twitter_req, {}, "response")
        expected = "RateLimitError(user_id=1, url=REQ-URL, msg=response)"
        self.assertEqual(str(err), expected)
        self.assertEqual(str(err), repr(err))
        
        self.assertTrue(err.is_client_cred)
        self.assertFalse(err.is_app_cred)

    def test_rate_limit_error_for_app_cred(self):
        client_cred = AppCredentials("token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM")

        err = RateLimitError(client_cred, twitter_req, {}, "response")
        expected = "RateLimitError(app_key=token, url=REQ-URL, msg=response)"
        self.assertEqual(str(err), expected)
        self.assertEqual(str(err), repr(err))

        self.assertFalse(err.is_client_cred)
        self.assertTrue(err.is_app_cred)



class TestRateLimit(unittest.TestCase):

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
                                    'X-RATE-LIMIT-RESET': time.time() + 0.1}))
        self.assertTrue(rate_limit.is_exhausted)
        drive_coro_once(rate_limit.comply())
        self.assertFalse(rate_limit.is_exhausted)

