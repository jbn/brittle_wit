import pytest
import aiohttp
import asyncio
from unittest.mock import patch, MagicMock
from brittle_wit import AppCredentials, ClientCredentials
from brittle_wit.app import App, ClientContext, RUNNING, PRESTINE, FINISHED
from brittle_wit.executors import ManagedClientRequestProcessors


pytestmark = pytest.mark.asyncio


# XXX: This simplifies things a lot.
def async_return(result):
    f = asyncio.Future()
    f.set_result(result)
    return f


async def test_client_context(app, client_cred, mocker):
    ctx = ClientContext(app, client_cred)

    execute_path = 'brittle_wit.executors.ClientRequestProcessor.execute'
    with mocker.patch(execute_path, return_value=async_return(42)) as execute:
        assert await ctx.execute('my_request') == 42


async def test_properties(app, app_cred, client_cred):
    # =========================================================================
    # These are silly tests meant for boosting coverage. They protect very
    # little. But, people care about coverage badges. At least at first,
    # possibly fragile tests that don't indicate true failures is worth the
    # possibility of greater adoption due to high coverage.
    # =========================================================================
    assert app.app_cred == app_cred
    assert isinstance(app.session, aiohttp.ClientSession)
    assert isinstance(app.manager, ManagedClientRequestProcessors)
    assert app.client_context(client_cred)._client_cred == client_cred


async def the_answer_coro():
    return 42


async def test_schedule_when_prestine(app):
    assert len(app._initial_coros) == 0
    c = the_answer_coro()
    assert app.schedule(c) is None  # Not running so no returned task.
    assert len(app._initial_coros) == 1
    await c  # To clear warnings about failured to run coro.


async def test_schedule_when_finished(app):
    app._state = FINISHED  # I.e. not in {RUNNING, PRESTINE}
    c = the_answer_coro()
    with pytest.raises(RuntimeError) as e:
        app.schedule(c)
    assert "state finished" in str(e)
    await c  # To clear warnings about failured to run coro.


async def test_schedule_when_running(app):
    app._state = RUNNING
    task = app.schedule(the_answer_coro())
    assert isinstance(task, asyncio.Task)
    assert await task == 42


async def test_schedule_maintenance_when_prestine(app):
    app._state = PRESTINE
    c = the_answer_coro()
    app.schedule_maintenance(c, True)
    assert c in app._maintenance_coros
    assert app._maintenance_coros[c]  # i.e. requires cancelation
    await c  # To clear warnings about failured to run coro.


async def test_schedule_maintenance_when_running(app):
    app._state = RUNNING
    c = the_answer_coro()
    task = app.schedule_maintenance(c, True)

    assert isinstance(task, asyncio.Task)
    assert c in app._maintenance_coros
    assert app._maintenance_coros[c]  # i.e. requires cancelation
    assert await task == 42


async def test_schedule_maintenance_when_finished(app):
    app._state = FINISHED
    c = the_answer_coro()
    with pytest.raises(RuntimeError) as e:
        app.schedule_maintenance(c, True)
    assert "state finished" in str(e)
    await c  # To clear warnings about failured to run coro.


# XXX: Add tests for no send cancel.


async def test_run_async_after_finished(app):
    app._state = FINISHED
    with pytest.raises(RuntimeError) as e:
        await app.run_async()
    assert 'already finished' in str(e)


async def test_run_async_when_running(app):
    app._state = 'running'
    with pytest.raises(RuntimeError) as e:
        await app.run_async()
    assert 'already running' in str(e)
