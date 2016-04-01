import asyncio
import time
import unittest
from brittle_wit import ClientCredentials
from brittle_wit.oauth import AppCredentials
from brittle_wit.rate_limit import RateLimit
from brittle_wit.executors import (AnyCredentials, RequestProcessor)
from test.helpers import *


class TestRequestProcessor(unittest.TestCase):
    def setUp(self):
        self.app_cred = AppCredentials("key", "secret")
        self.credentials = [ClientCredentials(1, "token-alice", "****"),
                            ClientCredentials(2, "token-bob", "****"),
                            ClientCredentials(3, "token-carol", "****")]

    def test_init(self):
        #processor = RequestProcessor(self.app_cred, self.credentials)
        pass
