import unittest
from unittest.mock import patch, MagicMock
from brittle_wit import AppCredentials, ClientCredentials
from brittle_wit.app import App, ClientContext
from test.helpers import drive_coro_once


async def dummy_coro(*args, **kwargs):
    return 42


class TestApp(unittest.TestCase):

    def test_client_context(self):
        app_cred = AppCredentials('app', 'secret')
        client_cred = ClientCredentials(1, 'user', 'secret')
        app = App(app_cred)
        ctx = ClientContext(app, client_cred)

        with patch('brittle_wit.executors.ClientRequestProcessor.execute') as execute:
            execute.return_value = dummy_coro()
            self.assertEqual(drive_coro_once(ctx.execute('my_request')), 42)
