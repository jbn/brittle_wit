import asyncio
import aiohttp
import os
from collections import deque
from contextlib import contextmanager
from brittle_wit_core import AppCredentials, ClientCredentials
from brittle_wit.executors import ManagedClientRequestProcessors
from brittle_wit.helpers import running_task_names
import brittle_wit.connection_props as DEFAULTS


class ClientContext:
    """
    Safely-encapsulates ``App``-associated ``ClientCredentials``.
    """
    __slots__ = ('_app', '_client_cred', '__weakref__')

    def __init__(self, app, client_cred):
        """
        :param app: The ``App`` these credentials belong to
        :param client_cred: The client's credentials.
        """
        self._app = app
        self._client_cred = client_cred

    async def execute(self, req, timeout=120, n_retries=5, sleep_time=60):
        """
        Execute the given request in the context of the associated client.

        :param req: a ``TwitterRequest``
        :return: A ``TwitterResponse``
        """
        # Client credentials may change -- they are just oauth key-pairs.
        # XXX: This violates the hash pattern so I thin the API needs a change.
        # I.E "REFRESH".
        # XXX: Figure out weakref pattern.
        processor = self._app.manager[self._client_cred]

        return await processor.execute(self._app.session,
                                       self._app.app_cred,
                                       req,
                                       timeout=timeout,
                                       n_retries=n_retries,
                                       sleep_time=sleep_time)


PRESTINE = 'prestine'
RUNNING = 'running'
FINISHED = 'finished'


class App:
    """
    A simple interface for building a Twitter App.
    """

    @classmethod
    def with_defaults(cls, app_cred, loop=None, session_overrides=None,
                      tcp_conn_overrides=None):
        """
        Create an application with sensible defaults for transports.

        :param app_cred: an `AppCredentials` object
        :param loop: the ``asyncio`` event loop.
        :param session_overrides: overrides for ``aiohttp.ClientSession``
            instantiation.
        :param tcp_conn_overrides``: overrides for ``aiohttp.TCPConnector``
            instantiation.
        """
        tcp_opts = {**DEFAULTS.TCP_CONN_REST, **(tcp_conn_overrides or {})}
        tcp_opts['loop'] = loop
        tcp_connector = aiohttp.TCPConnector(**tcp_opts)

        session_opts = {**DEFAULTS.SESSION_OPTS, **(session_overrides or {})}
        session_opts['connector'] = tcp_connector
        session_opts['loop'] = loop

        session = aiohttp.ClientSession(**session_opts)
        return App(app_cred, session)

    def __init__(self, app_cred, client_session):
        """
        Create a twitter app.

        :param app_cred: an `AppCredentials` object
        :param client_session: a aiohttp ClientSession
        """
        self._app_cred = app_cred
        self._session = client_session

        self._manager = ManagedClientRequestProcessors()
        self._initial_coros = deque()
        self._maintenance_coros = {}
        self._state = PRESTINE

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

    def run(self):
        """
        Run this app (blocking)
        """
        return asyncio.get_event_loop().run_until_complete(self.run_async())

    def schedule(self, coro):
        """
        Add a coroutine to the loop.

        :param coro: the coroutine to add. If the app is running, it is
            immediately added as a task to the event loop. If the app is not
            yet running, it is added to the initial task queue. If the app
            is no longer running, it is an error.
        :return: the task if and only if the app is running, otherwise None
        """
        if self._state == RUNNING:
            return asyncio.get_event_loop().create_task(coro)
        elif self._state == PRESTINE:
            self._initial_coros.append(coro)
        else:
            raise RuntimeError("Scheduled in state {}".format(self._state))

    def schedule_maintenance(self, coro, send_cancel=True):
        """
        Add a coroutine to the loop that does maintenance.

        An app with only maintance functions running may exit.

        :param coro: A coroutine that does maintenance.
        :param send_cancel: if True, the App will cancel this coro
            if it's still running when only maintenance tasks are running
        :return: the task if and only if the app is running, otherwise None
        """
        self._maintenance_coros[coro] = send_cancel

        if self._state == RUNNING:
            return asyncio.get_event_loop().create_task(coro)
        elif self._state == PRESTINE:
            pass  # Only need it in maintenance funcs.
        else:
            raise RuntimeError("Scheduled in state {}".format(self._state))

    def _prepare_for_run(self):
        if self._state == FINISHED:
            raise RuntimeError("This app has already finished! Can't rerun!")
        elif self._state == RUNNING:
            raise RuntimeError("This app is already running!")
        else:
            self._state = RUNNING  # XXX: WAIT WHAT?

    async def run_async(self):
        self._prepare_for_run()

        loop = asyncio.get_event_loop()
        self._maintenance_coros[self._manager.maintain()] = True

        async with self._session as session:

            # Add all initial tasks ------------------------------------------

            while self._initial_coros:
                loop.create_task(self._initial_coros.popleft())

            for coro in self._maintenance_coros:
                loop.create_task(coro)

            # Run until only simple maintenance tasks exist ------------------

            while True:
                pending = []

                for task in asyncio.Task.all_tasks():
                    # We can ignore a task if it's already done.
                    if task.done():
                        continue

                    # Obviously, this coro is running.
                    if task._coro.__qualname__ == 'App.run_async':
                        continue

                    # Tasks that are neither done nor a background maintenance
                    # task must be gathered before completion.
                    if task._coro not in self._maintenance_coros:
                        pending.append(task)

                if pending:
                    await asyncio.gather(*pending, return_exceptions=True)
                else:
                    break

        # End all maintenance tasks ------------------------------------------

        tasks_to_cancel = [task for task in asyncio.Task.all_tasks()
                           if not task.done() and
                           task._coro.__qualname__ != 'App.run_async' and
                           self._maintenance_coros.get(task._coro)]

        for task in tasks_to_cancel:
            task.cancel()

        await asyncio.gather(*tasks_to_cancel, return_exceptions=True)

        self._state = 'finished'

    @contextmanager
    def setup_and_run(self):
        yield self
        self.run()
