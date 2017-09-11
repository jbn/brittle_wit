import unittest
import aiohttp
import asyncio
from unittest.mock import patch, MagicMock
from brittle_wit import AppCredentials, ClientCredentials
from brittle_wit.app import App, ClientContext
from brittle_wit.executors import ManagedClientRequestProcessors
from test.helpers import AsyncSafeTestCase, async_patch


class TestApp(AsyncSafeTestCase):

    def setUp(self):
        self.app_cred = AppCredentials('app', 'secret')
        self.client_cred = ClientCredentials(1, 'user', 'secret')

    async def test_client_context(self):
        app = App(self.app_cred)
        ctx = ClientContext(app, self.client_cred)

        execute_path = 'brittle_wit.executors.ClientRequestProcessor.execute'
        with async_patch(execute_path, return_value=42) as execute:
            self.assertEqual(await ctx.execute('my_request'), 42)

    async def test_properties(self):
        app = App(self.app_cred)

        # These are silly tests meant for boosting coverage.
        # They protect very little. But, people care about coverage
        # badges. At least at first, possibly fragile tests that don't
        # indicate true failures is worth the possibility of greater
        # adoption due to high coverage.
        self.assertEqual(app.app_cred, self.app_cred)
        self.assertIsInstance(app.session, aiohttp.ClientSession)
        self.assertIsInstance(app.manager, ManagedClientRequestProcessors)

        ctx = app.client_context(self.client_cred)
        self.assertEqual(ctx._client_cred, self.client_cred)

    async def test_schedule_when_prestine(self):
        async def coro():
            pass

        app = App(self.app_cred)
        self.assertEqual(len(app._initial_coros), 0)
        c = coro()
        app.schedule(c)
        self.assertEqual(len(app._initial_coros), 1)
        await c  # To clear warnings about failured to run coro.

    async def test_schedule_when_finished(self):
        async def coro():
            pass

        app = App(self.app_cred)
        app._state = 'finished'
        c = coro()
        with self.assertRaisesRegexp(RuntimeError, "state finished"):
            app.schedule(c)
        await c  # To clear warnings about failured to run coro.

    async def test_schedule_when_running(self):
        async def coro():
            return 42

        app = App(self.app_cred)
        app._state = 'running'
        done, _ = await asyncio.wait([app.schedule(coro())])
        self.assertEqual(list(done)[0].result(), 42)

    async def test_schedule_maintenance_when_prestine(self):
        async def coro():
            return 42

        app = App(self.app_cred)
        app._state = 'prestine'
        c = coro()
        app.schedule_maintenance(c, True)
        self.assertIn(c, app._maintenance_coros)
        self.assertTrue(app._maintenance_coros[c])
        await c  # To clear warnings about failured to run coro.

    async def test_schedule_maintenance_when_running(self):
        async def coro():
            return 42

        app = App(self.app_cred)
        app._state = 'running'
        c = coro()
        task = app.schedule_maintenance(c, True)
        done, _ = await asyncio.wait([task])
        self.assertEqual(list(done)[0].result(), 42)
        self.assertIn(c, app._maintenance_coros)
        self.assertTrue(app._maintenance_coros[c])

    async def test_schedule_maintenance_when_finished(self):
        async def coro():
            return 42

        app = App(self.app_cred)
        app._state = 'finished'
        c = coro()
        with self.assertRaisesRegexp(RuntimeError, "state finished"):
            app.schedule_maintenance(c, True)
        await c

    async def test_run_async_after_finished(self):
        app = App(self.app_cred)
        app._state = 'finished'
        with self.assertRaisesRegexp(RuntimeError, 'already finished'):
            await app.run_async()

    async def test_run_async_when_running(self):
        app = App(self.app_cred)
        app._state = 'running'
        with self.assertRaisesRegexp(RuntimeError, 'already running'):
            await app.run_async()

    def test_run_no_tasks(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        app = App(self.app_cred)
        app.run()
        self.assertEqual(app._state, 'finished')

    def test_run_maintenance_gets_canceled(self):
        asyncio.set_event_loop(asyncio.new_event_loop())

        res = []

        async def maintenance():
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                res.append(42)

        app = App(self.app_cred)
        app.schedule_maintenance(maintenance(), True)
        app.run()
        self.assertEqual(app._state, 'finished')

    def test_setup_and_run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        res = []

        async def f():
            res.append(42)

        with App(self.app_cred).setup_and_run() as app:
            app.schedule(f())

        self.assertEqual(res, [42])
