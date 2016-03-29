import asyncio
import time
import unittest
from brittle_wit import ClientCredentials
from brittle_wit.oauth import AppCredentials
from brittle_wit.rate_limit import RateLimit
from brittle_wit.scheduling import (Requestor, ResourceFamily, AnyCredentials,
                                    RequestProcessor)
from test.helpers import *


async def mock_acquire_and_release(name, resource_family, cred):
    print(name)
    await resource_family.acquire(cred)
    await asyncio.sleep(0.1)
    resource_family.release(cred)
    return name


class TestRequestor(unittest.TestCase):

    def test_comply_without_sleeping(self):
        credentials = ClientCredentials(1, "a", "b")
        rate_limit = RateLimit.from_ignorance()
        self.assertFalse(rate_limit.is_exhausted)

        requestor = Requestor(credentials, rate_limit)
        self.assertEqual(drive_coro_once(requestor.use_credentials()),
                         credentials)
        self.assertTrue(rate_limit.is_exhausted)

        with self.assertRaises(RuntimeError):
            drive_coro_once(requestor.use_credentials())  # Didn't update yet!

        response = MockResp({'X-RATE-LIMIT-REMAINING': 1})  # Not exhausted
        requestor.update_limits_from_response(response)
        self.assertEqual(drive_coro_once(requestor.use_credentials()),
                         credentials)


class TestResourceFamily(unittest.TestCase):
    def setUp(self):
        self.credentials = [ClientCredentials(1, "token-alice", "****"),
                            ClientCredentials(2, "token-bob", "****"),
                            ClientCredentials(3, "token-carol", "****")]

    def test_manage_all(self):
        resource_family = ResourceFamily(0.1)

        for cred in self.credentials:
            self.assertFalse(resource_family.is_managed(cred))

        resource_family.manage_all(self.credentials)
        for cred in self.credentials:
            self.assertTrue(resource_family.is_managed(cred))

        with self.assertRaises(ValueError):
            resource_family.manage(self.credentials[0])

    def test_release_unmanaged(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials[:-1])
        self.assertFalse(resource_family.is_managed(self.credentials[-1]))
        with self.assertRaises(LookupError):
            resource_family.release(self.credentials[-1])

    def test_release_when_exhausted(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials)
        alice_cred = self.credentials[0]
        resource_family._rate_limit[alice_cred]._remaining = 0  # Exhausted
        resource_family.release(alice_cred)
        self.assertEqual(resource_family.current_status(alice_cred), 'waiting')

    def test_release_when_not_exhausted(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials)
        alice_cred = self.credentials[0]
        resource_family._rate_limit[alice_cred]._remaining = 1  # Not Exhausted
        resource_family.release(alice_cred)
        self.assertEqual(resource_family.current_status(alice_cred), 'ready')

    def test_maintain_queues(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials)
        alice_cred = self.credentials[0]

        # Return the credentials as stale with 10th of a second wait time.
        resp = MockResp({'X-RATE-LIMIT-LIMIT': 100,
                         'X-RATE-LIMIT-REMAINING': 0,
                         'X-RATE-LIMIT-RESET': time.time() + 0.1})
        resource_family._rate_limit[alice_cred].update(resp)
        resource_family.release(alice_cred)
        self.assertEqual(resource_family.current_status(alice_cred), 'waiting')

        drive_coro_once(resource_family.maintain_queues(), timeout=0.15)
        self.assertEqual(resource_family.current_status(alice_cred), 'ready')

    def test_acquire_enforces_fifo_for_requests(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials)
        bob_cred = self.credentials[1]

        tasks = [mock_acquire_and_release(i, resource_family, bob_cred)
                 for i in range(3)]
        self.assertEqual(drive_all(tasks), [0, 1, 2])

    def test_acquire_any(self):
        resource_family = ResourceFamily(0.1).manage_all(self.credentials)
        contexts = drive_all(resource_family.acquire(AnyCredentials)
                             for _ in range(3))

        async def extract_cred(context):
            with context as requestor:
                return await requestor.use_credentials()

        collected = set(drive_all(extract_cred(ctx) for ctx in contexts))
        self.assertEqual(collected, set(self.credentials))


class TestRequestProcessor(unittest.TestCase):
    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.credentials = [ClientCredentials(1, "token-alice", "****"),
                            ClientCredentials(2, "token-bob", "****"),
                            ClientCredentials(3, "token-carol", "****")]

    def test_init(self):
        processor = RequestProcessor(self.app_cred, self.credentials)
