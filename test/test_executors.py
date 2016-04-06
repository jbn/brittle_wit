import unittest
from unittest.mock import MagicMock

from brittle_wit import TwitterRequest
from brittle_wit.executors import *
from brittle_wit.messages import TwitterError
from brittle_wit.oauth import AppCredentials, ClientCredentials
from test.helpers import *


class MockHTTPResp:
    def __init__(self, status, headers, body):
        self.status, self.headers, self.body = status, headers, body

    async def json(self):
        return self.body

    async def text(self):
        return self.body


class MockHTTPReq:
    def __init__(self, resp):
        self._resp = resp

    async def __aenter__(self):
        return self._resp

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


class TestTwitterReqToHTTPRequest(unittest.TestCase):
    def test_twitter_req_to_http_req(self):
        # This is a dumb test but it should help prevent dumb regressions.
        app_cred = AppCredentials("key", "secret")
        client_cred = ClientCredentials(1, "token-alice", "****")
        tr = TwitterRequest("POST", "http://url.com/", "service", "family")
        with aiohttp.ClientSession() as session:
            req = twitter_req_to_http_req(session, app_cred, client_cred, tr)
            self.assertEqual(type(req), aiohttp.client._RequestContextManager)


class TestExecuteRequest(unittest.TestCase):
    def test_good_resp_and_json_body(self):
        cred = ClientCredentials(1, "token-alice", "****")
        twitter_req = TwitterRequest("method", "url", "family", "service")
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))

        coro = execute_req(cred, twitter_req, http_req, rate_limit, 1000)
        res = drive_coro_once(coro)
        self.assertIs(type(res), TwitterResponse)
        self.assertEqual(res.body['count'], 100)

    def test_good_resp_and_text_body(self):
        cred = ClientCredentials(1, "token-alice", "****")
        twitter_req = TwitterRequest("method", "url", "family", "service",
                                     parse_as='text')
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(200, {}, {'count': 100}))

        coro = execute_req(cred, twitter_req, http_req, rate_limit, 1000)
        res = drive_coro_once(coro)
        self.assertIs(type(res), TwitterResponse)
        self.assertEqual(res.body['count'], 100)

    def test_bad_resp(self):
        cred = ClientCredentials(1, "token-alice", "****")
        twitter_req = TwitterRequest("method", "url", "family", "service",
                                     parse_as='text')
        rate_limit = RateLimit.from_ignorance()
        http_req = MockHTTPReq(MockHTTPResp(403, {}, "Forbidden"))

        with self.assertRaises(TwitterError):
            coro = execute_req(cred, twitter_req, http_req, rate_limit, 1000)
            res = drive_coro_once(coro)


class TestClientRequestProcessor(unittest.TestCase):
    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.credentials = [ClientCredentials(1, "token-alice", "****"),
                            ClientCredentials(2, "token-bob", "****"),
                            ClientCredentials(3, "token-carol", "****")]
        self.processor = ClientRequestProcessor(self.credentials)

    def test_init(self):
       self.assertTrue(self.processor.is_not_processing())

       tm = MagicMock()
       tm.all_lines_empty = lambda: False
       self.processor._ticket_master = tm

       self.assertFalse(self.processor.is_not_processing())

    def test_rate_limit_for(self):
        limit = self.processor._rate_limit_for("direct_messages")
        self.assertTrue(limit.is_pristine)
        self.assertIs(limit, self.processor._rate_limit_for("direct_messages"))

        self.assertIsNot(limit,
                         self.processor._rate_limit_for("account/settings"))

    def test_is_immediately_available_for(self):
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

    def test_cleanup(self):
        self.assertTrue(self.processor.is_removable())
        self.assertFalse(self.processor._rate_limits)
        self.processor.cleanup()
        self.assertFalse(self.processor._rate_limits)

        now = time.time()
        self.processor._rate_limits['future'] = RateLimit(1, 1, now+100)
        self.processor._rate_limits['past'] = RateLimit(1, 1, now-100)
        self.assertEqual(set(self.processor._rate_limits), {'future', 'past'})
        self.processor.cleanup(now)
        self.assertFalse(self.processor.is_removable())
        self.assertEqual(set(self.processor._rate_limits), {'future'})
        self.assertFalse(self.processor.is_removable())


class TestManagedClientRequestProcessors(unittest.TestCase):
    def test_add_and_remove(self):
        alice = ClientCredentials(1, "alice", "secret")
        bob = ClientCredentials(2, "bob", "secret")
        processors = ManagedClientRequestProcessors()

        self.assertFalse(processors.is_managed(alice))
        self.assertFalse(processors.is_managed(bob))

        processors.add(alice)
        self.assertTrue(processors.is_managed(alice))
        self.assertFalse(processors.is_managed(bob))

        processors.remove(alice)
        self.assertFalse(processors.is_managed(alice))
        self.assertFalse(processors.is_managed(bob))

        processors.add(bob)
        self.assertFalse(processors.is_managed(alice))
        self.assertTrue(processors.is_managed(bob))

        with self.assertRaises(AssertionError):
            processors.add(bob)

    def test_get_item(self):
        alice = ClientCredentials(1, "alice", "secret")
        bob = ClientCredentials(2, "bob", "secret")
        processors = ManagedClientRequestProcessors()

        self.assertEqual(processors[alice]._client_credentials, alice)
        self.assertEqual(processors[bob]._client_credentials, bob)

        self.assertEqual({processors[ANY_CREDENTIALS]._client_credentials
                          for _ in range(10)},
                         {alice, bob})

    def test_maintain(self):
        alice = ClientCredentials(1, "alice", "secret")
        bob = ClientCredentials(2, "bob", "secret")
        processors = ManagedClientRequestProcessors()

        now = time.time()
        processors[alice]._rate_limits['future'] = RateLimit(1, 1, now+100)
        processors[bob]._rate_limits['passed'] = RateLimit(1, 1, now-100)

        self.assertTrue(processors.is_managed(alice))
        self.assertTrue(processors.is_managed(bob))

        processors.maintain()

        self.assertTrue(processors.is_managed(alice))
        self.assertFalse(processors.is_managed(bob))

