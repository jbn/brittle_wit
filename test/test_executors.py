import unittest
import random
from unittest.mock import MagicMock, patch

from brittle_wit_core import (TwitterRequest, TwitterError,
                              AppCredentials, ClientCredentials)
from brittle_wit.executors import *
from test.helpers import *


class TestTwitterReqToHTTPRequest(unittest.TestCase):
    # This is a dumb test but it should help prevent dumb regressions.

    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.client_cred = ClientCredentials(1, "token-alice", "****")

    def test_twitter_req_to_http_req_get(self):
        app_cred, client_cred = self.app_cred, self.client_cred
        tr = TwitterRequest("GET", "http://url.com/", "service", "family")
        with aiohttp.ClientSession() as session:
            req = twitter_req_to_http_req(session, app_cred, client_cred, tr)
            self.assertEqual(type(req), aiohttp.client._RequestContextManager)

    def test_twitter_req_to_http_req_post(self):
        app_cred, client_cred = self.app_cred, self.client_cred
        tr = TwitterRequest("POST", "http://url.com/", "service", "family")
        with aiohttp.ClientSession() as session:
            req = twitter_req_to_http_req(session, app_cred, client_cred, tr)
            self.assertEqual(type(req), aiohttp.client._RequestContextManager)


class TestExecuteRequest(AsyncSafeTestCase):

    def setUp(self):
        self.cred = ClientCredentials(1, "token-alice", "****")
        self.twitter_req = TwitterRequest("method", "url", "family", "service")

    async def test_good_resp_and_json_body(self):
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))

        res = await execute_req(self.cred, self.twitter_req, http_req,
                                rate_limit)

        self.assertIs(type(res), TwitterResponse)
        self.assertEqual(res.body['count'], 100)

    async def test_good_resp_and_text_body(self):
        self.twitter_req.parse_as = 'text'
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(200, {}, "hello world"))

        coro = execute_req(self.cred, self.twitter_req, http_req, rate_limit)
        res = await coro
        self.assertIs(type(res), TwitterResponse)
        self.assertEqual(res.body, "hello world")

    async def test_bad_resp(self):
        self.twitter_req.parse_as = 'text'
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(403, {}, "Forbidden"))

        coro = execute_req(self.cred, self.twitter_req, http_req, rate_limit)
        with self.assertRaises(TwitterError):
            await coro


class TestClientRequestProcessor(unittest.TestCase):

    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.credentials = ClientCredentials(2, "token-bob", "****")
        self.processor = ClientRequestProcessor(self.credentials)

    def test_properties(self):
        self.assertEqual(self.processor.user_id, 2)

    def test_is_removable_after_init(self):
        self.assertTrue(self.processor.is_removable())

    def test_is_removable_when_processing(self):
        tm = MagicMock()
        tm.all_lines_empty = lambda: False
        self.processor._ticket_master = tm

        # It's waiting for a ticket to make a request.
        self.assertFalse(self.processor.is_removable())

    def test_is_removable_when_rate_limited(self):
        self.processor._rate_limits['svc'] = RateLimit.from_initial_limit(0)
        self.assertFalse(self.processor.is_removable())

    def test_is_not_processing_on_init(self):
        self.assertTrue(self.processor.is_not_processing())

    def test_is_processing_when_waiting_for_ticket(self):
        tm = MagicMock()
        tm.all_lines_empty = lambda: False
        self.processor._ticket_master = tm

        # It's waiting for a ticket to make a request.
        self.assertFalse(self.processor.is_not_processing())

    def test_is_immediately_available_for_when_no_line_and_no_limit(self):
        self.assertTrue(self.processor.is_immediately_available_for('svc'))

    def test_is_immediately_available_for_when_currently_on_line(self):
        tm = MagicMock()
        tm.is_line_empty = lambda _: False
        self.processor._ticket_master = tm

        self.assertFalse(self.processor.is_immediately_available_for('svc'))

    def test_is_immediately_available_for_when_no_line_and_exhausted(self):
        self.processor._rate_limits['svc'] = RateLimit.from_initial_limit(0)
        self.assertFalse(self.processor.is_immediately_available_for('svc'))

    def test_is_immediately_available_for_when_no_line_and_not_exhausted(self):
        self.processor._rate_limits['svc'] = RateLimit.from_ignorance()
        self.assertTrue(self.processor.is_immediately_available_for('svc'))

    def test_is_immediately_available_for_when_line_not_empty(self):
        svc = "direct_message"
        self.assertTrue(self.processor.is_immediately_available_for(svc))

        limit = RateLimit.from_ignorance()
        limit._remaining = 0
        self.processor._rate_limits[svc] = limit
        self.assertFalse(self.processor.is_immediately_available_for(svc))

        tm = MagicMock()
        tm.is_line_empty = lambda s: False
        self.processor._ticket_master = tm
        self.assertFalse(self.processor.is_immediately_available_for(svc))

    def test_rate_limit_for_doesnt_duplicate_on_same_service(self):
        limit = self.processor._rate_limit_for("direct_messages")
        self.assertTrue(isinstance(limit, RateLimit))  # Sane.

        self.assertIs(limit, self.processor._rate_limit_for("direct_messages"))

    def test_rate_limit_for_unique_for_diff_service(self):
        dm_limit = self.processor._rate_limit_for("direct_messages")
        settings_limit = self.processor._rate_limit_for("account/settings")

        self.assertTrue(isinstance(dm_limit, RateLimit))        # Sane.
        self.assertTrue(isinstance(settings_limit, RateLimit))  # Sane.
        self.assertIsNot(dm_limit, settings_limit)

    def test_rate_limit_for_is_initially_prestine(self):
        limit = self.processor._rate_limit_for("direct_messages")
        self.assertTrue(limit.is_pristine)

    def test_cleanup_with_no_rate_limits(self):
        self.assertFalse(self.processor._rate_limits)
        self.processor.cleanup()
        self.assertFalse(self.processor._rate_limits)

    def test_cleanup_with_stale_rate_limit(self):
        now = time.time()
        self.processor._rate_limits['past'] = RateLimit(1, 1, now - 100)
        self.processor.cleanup(now)
        self.assertTrue(self.processor.is_removable())

    def test_cleanup_with_mixed_rate_limits(self):
        now = time.time()
        self.processor._rate_limits['future'] = RateLimit(1, 1, now + 100)
        self.processor._rate_limits['past'] = RateLimit(1, 1, now - 100)
        self.assertEqual(set(self.processor._rate_limits), {'future', 'past'})

        self.processor.cleanup(now)

        self.assertFalse(self.processor.is_removable())
        self.assertEqual(set(self.processor._rate_limits), {'future'})


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


class TestClientRequestProcessorExecution(AsyncSafeTestCase):

    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.client_cred = ClientCredentials(1, "token-alice", "****")
        self.rate_limit = RateLimit.from_ignorance()
        self.processor = ClientRequestProcessor(self.client_cred)
        self.http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))
        self.twitter_req = TwitterRequest("method", "url", "family", "service")

    async def test__execute_prestine(self):
        coro = self.processor._execute('session', self.app_cred, self.twitter_req)
        func_path = 'brittle_wit.executors.twitter_req_to_http_req'
        with patch(func_path, return_value=self.http_req) as req_to_http_req:
            resp = await coro

            req_to_http_req.assert_called_with('session',
                                               self.app_cred,
                                               self.client_cred,
                                               self.twitter_req)

            self.assertIs(type(resp), TwitterResponse)
            self.assertEqual(resp.body['count'], 100)

    async def test__execute_timeout_thrown(self):
        coro = self.processor._execute('session', self.app_cred, self.twitter_req, 0.01)
        self.processor._rate_limits['service'] = RateLimitKludge(self.twitter_req, self.client_cred, sleep_time=1)

        with self.assertRaises(asyncio.TimeoutError):
            await coro

    async def test_execute_retrying(self):
        fail_queue = [True, False]
        client_cred = self.client_cred

        self.processor._rate_limits['service'] = RateLimitKludge(self.twitter_req, self.client_cred, fail_queue)
        func_path = 'brittle_wit.executors.twitter_req_to_http_req'
        coro = self.processor.execute('session', self.app_cred, self.twitter_req,
                                      sleep_time=0.01)
        with patch(func_path, return_value=self.http_req) as req_to_http_req:
            resp = await coro
            self.assertIs(type(resp), TwitterResponse)
            self.assertEqual(resp.body['count'], 100)
            self.assertEqual(fail_queue, [])

    async def test_execute_retrying_too_many_failures(self):
        http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))
        fail_queue = [True] * 6
        client_cred = self.client_cred

        self.processor._rate_limits['service'] = RateLimitKludge(self.twitter_req, self.client_cred, fail_queue)
        func_path = 'brittle_wit.executors.twitter_req_to_http_req'
        coro = self.processor.execute('session', self.app_cred, self.twitter_req,
                                      sleep_time=0.01)
        with patch(func_path, return_value=self.http_req) as req_to_http_req:
            with self.assertRaises(TwitterError):
                resp = await coro


class TestManagedClientRequestProcessors(AsyncSafeTestCase):

    def setUp(self):
        self.manager = ManagedClientRequestProcessors()
        self.alice = ClientCredentials(1, "alice", "secret")
        self.bob = ClientCredentials(2, "bob", "secret")

    def test_nothing_managed_on_init(self):
        self.assertFalse(self.manager.is_managed(self.alice))

    def test_managed_after_explicit_add(self):
        self.manager.add(self.alice)
        self.assertTrue(self.manager.is_managed(self.alice))

    def test_managed_after_explicit_add_non_promiscuous(self):
        self.manager.add(self.alice, any_cred_eligible=False)
        self.assertTrue(self.manager.is_managed(self.alice))
        self.assertNotIn(self.alice, self.manager._any_cred_queue)

    def test_add_all(self):
        self.manager.add_all([self.alice, self.bob])
        self.assertTrue(self.manager.is_managed(self.alice))
        self.assertTrue(self.manager.is_managed(self.bob))

    def test_remove(self):
        creds = [self.alice, self.bob]
        self.manager.add_all(creds)
        random.shuffle(creds)
        removed, kept = creds
        self.manager.remove(removed)
        self.assertIn(kept, self.manager._any_cred_queue)
        self.assertNotIn(removed, self.manager._any_cred_queue)

    def test_remove_not_any_cred(self):
        self.manager.add(self.alice, any_cred_eligible=False)
        self.assertNotIn(self.alice, self.manager._any_cred_queue)
        self.manager.remove(self.alice)
        self.assertNotIn(self.alice, self.manager._any_cred_queue)

    def test_add_cannot_add_dup(self):
        self.manager.add(self.bob)
        with self.assertRaises(RuntimeError):
            self.manager.add(self.bob)

    def test__getitem__(self):
        self.assertEqual(self.manager[self.alice]._client_cred, self.alice)
        self.assertEqual(self.manager[self.bob]._client_cred, self.bob)

        self.assertEqual({self.manager[ANY_CREDENTIALS]._client_cred
                          for _ in range(10)},
                         {self.alice, self.bob})

    def test__getitem__anycred_exhausted(self):
        self.assertIsNone(self.manager[ANY_CREDENTIALS])
        self.manager.add(self.bob)
        self.assertEqual(self.manager[ANY_CREDENTIALS], self.bob)

    def test__maintain(self):
        self.manager.add_all([self.alice, self.bob])

        now = time.time()
        self.manager[self.alice]._rate_limits['future'] = RateLimit(1, 1, now + 100)
        self.manager[self.bob]._rate_limits['passed'] = RateLimit(1, 1, now - 100)

        self.assertTrue(self.manager.is_managed(self.alice))
        self.assertTrue(self.manager.is_managed(self.bob))

        self.manager._maintain()

        self.assertTrue(self.manager.is_managed(self.alice))
        self.assertFalse(self.manager.is_managed(self.bob))

    async def test_maintain_reraise_keyboard_interrupt(self):
        path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
        with patch(path, side_effect=KeyboardInterrupt()) as _maintain:
            with async_ignore_sleep() as sleep_times:
                with self.assertRaises(KeyboardInterrupt):
                    await self.manager.maintain()

    async def test_maintain_graceful_shutdown(self):
        path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
        with patch(path, side_effect=asyncio.CancelledError()) as _maintain:
            with async_ignore_sleep() as sleep_times:
                await self.manager.maintain()

    async def test_maintain_catches_all_else(self):
        exceptions = [RuntimeError("test"), KeyboardInterrupt()]

        def f():
            raise exceptions.pop(0)

        path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
        with patch(path, side_effect=f) as _maintain:
            with async_ignore_sleep() as sleep_times:
                with self.assertRaises(KeyboardInterrupt):
                    await self.manager.maintain()


class TestDebugBlockingRequest(unittest.TestCase):

    def test_debug_blocking_request(self):
        app_cred = AppCredentials("key", "secret")
        client_cred = ClientCredentials(1, "token-alice", "****")
        twitter_req = TwitterRequest("method", "url", "family", "service")

        with patch('requests.request', return_value=42) as f:
            res = debug_blocking_request(app_cred,
                                         client_cred,
                                         twitter_req)
            self.assertEqual(res, 42)
