import pytest
import aiohttp
import asyncio
from unittest.mock import patch, MagicMock
from brittle_wit import AppCredentials, ClientCredentials
from brittle_wit.app import App, ClientContext, RUNNING, PRESTINE, FINISHED
from brittle_wit.executors import ManagedClientRequestProcessors
from tests.helpers import AsyncSafeTestCase, async_patch


def test_run_no_tasks(app):
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.run()
    assert app._state == FINISHED


def test_run_maintenance_gets_canceled(app):
    asyncio.set_event_loop(asyncio.new_event_loop())

    res = []

    async def maintenance():
        try:
            await asyncio.sleep(10)
        except asyncio.CancelledError:
            res.append(42)

    app.schedule_maintenance(maintenance(), True)
    app.run()
    assert app._state == FINISHED


def test_setup_and_run(app_cred):
    asyncio.set_event_loop(asyncio.new_event_loop())
    res = []

    async def f():
        res.append(42)

    with App.with_defaults(app_cred).setup_and_run() as app:
        app.schedule(f())

    assert res == [42]
