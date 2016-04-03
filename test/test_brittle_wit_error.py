import aiohttp
import unittest

from unittest.mock import MagicMock
from brittle_wit.brittle_wit_error import *
from brittle_wit.oauth import ClientCredentials
from brittle_wit.twitter_request import TwitterRequest


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

    def test_internal_server_error(self):
        client_cred = ClientCredentials(1, "token", "secret")
        twitter_req = TwitterRequest('POST', "REQ-URL", "FAM", "SVC")
        resp = MagicMock()
        resp.status = 500

        err = TwitterError(client_cred, twitter_req, resp, "m")
        self.assertEqual(str(err), "TwitterError(code=500, msg=m)")
        self.assertEqual(str(err), repr(err))
        self.assertTrue(err.is_retryable)


class TestWrappedException(unittest.TestCase):
    def test_client_os_error(self):
        err = WrappedException(aiohttp.errors.ClientOSError())
        self.assertTrue(err.is_retryable)

    def test_keyboard_interrupt(self):
        err = WrappedException(KeyboardInterrupt())
        self.assertFalse(err.is_retryable)
