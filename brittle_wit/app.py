import asyncio
import aiohttp
import os
from contextlib import contextmanager
from brittle_wit.oauth import AppCredentials, ClientCredentials
from brittle_wit.executors import ManagedClientRequestProcessors


def load_app_cred():
    return AppCredentials(os.environ['TWITTER_APP_KEY'],
                          os.environ['TWITTER_APP_SECRET'])


def load_single_user_cred():
    return ClientCredentials(os.environ['TWITTER_USER_ID'],
                             os.environ['TWITTER_USER_TOKEN'],
                             os.environ['TWITTER_USER_SECRET'])


class ClientContext:

    def __init__(self, app, client_cred):
        self._app = app
        self._client_cred = client_cred

    async def execute(self, req):
        processor = self._app.manager[self._client_cred]  # ALWAYS CALL!
        return await processor.execute(self._app.session, self._app.app_cred,
                                       req)


class App:

    def __init__(self, loop, session, app_cred):
        self._loop = loop
        self._app_cred = app_cred
        self._session = session
        self._manager = ManagedClientRequestProcessors()

    @property
    def loop(self):
        return self._loop

    @property
    def app_cred(self):
        return self._app_cred

    @property
    def session(self):
        return self._session

    @property
    def manager(self):
        return self._manager

    def client_context(self, client_crede):
        return ClientContext(self, client_crede)

    @staticmethod
    @contextmanager
    def reactor(app_cred, **tcp_connect_args):
        loop = asyncio.get_event_loop()
        tcp_conn = aiohttp.TCPConnector(**tcp_connect_args)
        with aiohttp.ClientSession(connector=tcp_conn) as session:
            yield App(loop, session, app_cred)

        loop.close()
        asyncio.set_event_loop(asyncio.new_event_loop())

    def run_until_complete(self, coro):
        return self._loop.run_until_complete(coro)
