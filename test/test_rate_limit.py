import time
import unittest
from unittest.mock import MagicMock
from brittle_wit.oauth import ClientCredentials, AppCredentials
from brittle_wit.rate_limit import (RateLimit, RateLimitError,
                                    CredentialContext, RateLimitEnforcer)
from brittle_wit.twitter_request import TwitterRequest
from test.helpers import *


class TestRateLimitError(unittest.TestCase):

    def test_rate_limit_error_for_client_cred(self):
        client_cred = ClientCredentials(1, "token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM", "SVC")

        err = RateLimitError(client_cred, twitter_req, {}, "response")
        expected = "RateLimitError(user_id=1, url=REQ-URL, msg=response)"
        self.assertEqual(str(err), expected)
        self.assertEqual(str(err), repr(err))

        self.assertTrue(err.is_client_cred)
        self.assertFalse(err.is_app_cred)

    def test_rate_limit_error_for_app_cred(self):
        client_cred = AppCredentials("token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM", "SVC")

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


class TestCredentialContext(unittest.TestCase):

    def test_comply_without_sleeping(self):
        credentials = ClientCredentials(1, "a", "b")
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

        ctx = CredentialContext(None, credentials, rate_limit)
        self.assertEqual(drive_coro_once(ctx.use_credentials()), credentials)
        self.assertTrue(rate_limit.is_exhausted)

        with self.assertRaises(RuntimeError):
            drive_coro_once(ctx.use_credentials())  # Didn't update yet!

        response = MockResp({'X-RATE-LIMIT-REMAINING': 1})  # Not exhausted
        ctx.update_limits_from_response(response)
        self.assertEqual(drive_coro_once(ctx.use_credentials()), credentials)

    def test_context_does_release(self):
        enforcer = MagicMock()
        credentials = ClientCredentials(1, "a", "b")
        rate_limit = RateLimit.from_ignorance()
        with CredentialContext(enforcer, credentials, rate_limit) as ctx:
            pass
        enforcer.release.assert_called_with(credentials)


async def mock_acquire_and_release(name, resource_family, cred):
    print(name)
    await resource_family.acquire(cred)
    await asyncio.sleep(0.1)
    resource_family.release(cred)
    return name


class TestRateLimitEnforcer(unittest.TestCase):
    def setUp(self):
        self.credentials = [ClientCredentials(1, "token-alice", "****"),
                            ClientCredentials(2, "token-bob", "****"),
                            ClientCredentials(3, "token-carol", "****")]

    def test_release_when_exhausted(self):
        enforcer = RateLimitEnforcer(wait_queue_sleep_time=0.1)
        alice_cred = self.credentials[0]
        enforcer._rate_limit[alice_cred]._remaining = 0  # Exhausted
        enforcer.release(alice_cred)
        self.assertEqual(enforcer.current_status(alice_cred), 'waiting')

    def test_release_when_not_exhausted(self):
        enforcer = RateLimitEnforcer(wait_queue_sleep_time=0.1)
        alice_cred = self.credentials[0]
        enforcer._rate_limit[alice_cred]._remaining = 1  # Not Exhausted
        enforcer.release(alice_cred)
        self.assertEqual(enforcer.current_status(alice_cred), 'ready')

    def test_maintain_queues(self):
        enforcer = RateLimitEnforcer(wait_queue_sleep_time=0.1)
        alice_cred = self.credentials[0]

        # Return the credentials as stale with 10th of a second wait time.
        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 0,
                         'X-RATE-LIMIT-RESET': time.time() + 0.1})
        enforcer._rate_limit[alice_cred].update(resp)
        enforcer.release(alice_cred)
        self.assertEqual(enforcer.current_status(alice_cred), 'waiting')

        drive_coro_once(enforcer.maintain_queues(), timeout=0.15)
        self.assertEqual(enforcer.current_status(alice_cred), 'ready')

    def test_acquire_enforces_fifo_for_requests(self):
        enforcer = RateLimitEnforcer(wait_queue_sleep_time=0.1)
        bob_cred = self.credentials[1]

        xs = [42, 11, 19]
        tasks = [mock_acquire_and_release(i, enforcer, bob_cred) for i in xs]
        self.assertEqual(drive_all(tasks), xs)
