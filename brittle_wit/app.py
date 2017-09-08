import asyncio
import aiohttp
import os
from contextlib import contextmanager
from brittle_wit_core import AppCredentials, ClientCredentials
from brittle_wit.executors import ManagedClientRequestProcessors


class ClientContext:
    """
    Safely-encapsulates ``App``-associated ``ClientCredentials``.
    """
    __slots__ = ('_app', '_client_cred')

    def __init__(self, app, client_cred):
        """
        :param app: The ``App`` these credentials belong to
        :param client_cred: The client's credentials.
        """
        self._app = app
        self._client_cred = client_cred

    async def execute(self, req):
        """
        Execute the given request in the context of the associated client.

        :param req: a ``TwitterRequest``
        :return: A ``TwitterResponse``
        """
        # Client credentials may change -- they are just oauth key-pairs.
        processor = self._app.manager[self._client_cred]

        return await processor.execute(self._app.session, self._app.app_cred,
                                       req)


class App:

    def __init__(self, app_cred, loop=None, session=None, tcp_conn=None):
        self._app_cred = app_cred
        self._manager = ManagedClientRequestProcessors()

        if loop is None:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self._loop = loop

        tcp_conn = aiohttp.TCPConnector()
        self._session = session or aiohttp.ClientSession(connector=tcp_conn)

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

    def client_context(self, client_cred):
        return ClientContext(self, client_cred)

    @staticmethod
    @contextmanager
    def reactor(app_cred, **tcp_connect_args):
        with self._session as session:
            yield self

    def run_until_complete(self, coro):
        return self._loop.run_until_complete(coro)
