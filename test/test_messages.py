import unittest
from unittest.mock import MagicMock

import aiohttp

from brittle_wit import (TwitterRequest, Cursor, TwitterResponse,
                         BrittleWitError)
from brittle_wit.messages import TwitterError, WrappedException
from brittle_wit.oauth import ClientCredentials


class TestBrittleWitError(unittest.TestCase):
    def test_brittle_wit_error(self):
        self.assertFalse(BrittleWitError().is_retryable)


class TestTwitterError(unittest.TestCase):

    def test_rate_limit_error(self):
        client_cred = ClientCredentials(1, "token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM", "SVC")
        resp = MagicMock()
        resp.status = 429

        err = TwitterError(client_cred, twitter_req, resp, "m")
        self.assertEqual(str(err), "TwitterError(code=429, msg=m)")
        self.assertEqual(str(err), repr(err))
        self.assertFalse(err.is_retryable)
        self.assertIs(err.twitter_req, twitter_req)
        self.assertIs(err.credentials, client_cred)

    def test_internal_server_error(self):
        client_cred = ClientCredentials(1, "token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM", "SVC")
        resp = MagicMock()
        resp.status = 500

        err = TwitterError(client_cred, twitter_req, resp, "m")
        self.assertEqual(str(err), "TwitterError(code=500, msg=m)")
        self.assertEqual(str(err), repr(err))
        self.assertTrue(err.is_retryable)
        self.assertEqual(err.message, "m")


class TestWrappedException(unittest.TestCase):
    def test_client_os_error(self):
        e = aiohttp.errors.ClientOSError()
        err = WrappedException(e)
        self.assertTrue(err.is_retryable)
        self.assertIs(err.underlying_exception, e)

    def test_keyboard_interrupt(self):
        err = WrappedException(KeyboardInterrupt())
        self.assertFalse(err.is_retryable)
        self.assertEqual(repr(err), "WrappedException(KeyboardInterrupt())")


class TestTwitterRequest(unittest.TestCase):
    def test_twitter_request(self):
        req = TwitterRequest("GET", "http://twitter.com/faux/service",
                             "faux", "faux/service", parse_as="json",
                             timeout=1000)
        req.parse_as = "raw"
        self.assertEqual(req.parse_as, "raw")
        self.assertEqual(str(req),
                         "TwitterRequest(url=http://twitter.com/faux/service)")

        dup = req.clone_and_merge({'timeout': 0})
        self.assertEqual(dup.params["timeout"], 0)
        self.assertEqual(req.params["timeout"], 1000)


class TestCursor(unittest.TestCase):
    def test_cursor(self):
        req = TwitterRequest("GET", "http://twitter.com/f/s", "f", "f/s")

        cursor = iter(Cursor(req))
        self.assertIs(req, next(cursor))
        with self.assertRaises(RuntimeError):
            next(cursor)

        cursor.update(TwitterResponse(None, None, {'next_cursor': 0}))
        with self.assertRaises(StopIteration):
            next(cursor)

        cursor = iter(Cursor(req))
        cursor.update(TwitterResponse(None, None, {}))
        with self.assertRaises(StopIteration):
            next(cursor)

        cursor = iter(Cursor(req))
        cursor.update(TwitterResponse(None, None, {'next_cursor': 100}))
        req = next(cursor)
        self.assertEqual(req.params['cursor'], 100)
