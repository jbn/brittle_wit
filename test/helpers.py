import asyncio
import json
import os
import unittest
from collections import namedtuple
from functools import wraps


SELF_DIR = os.path.dirname(os.path.realpath(__file__))
FIXTURES_DIR = os.path.join(SELF_DIR, "fixtures")


def load_fixture_txt(file_name):
    with open(os.path.join(FIXTURES_DIR, file_name)) as fp:
        return fp.read()


def load_fixture_json(file_name):
    with open(os.path.join(FIXTURES_DIR, file_name)) as fp:
        return json.load(fp)


def mock_resp(headers):
    mock = unittest.mock.MagicMock()
    mock.headers = headers
    return mock


class MockHTTPResp:

    def __init__(self, status, headers, body, delay=0):
        self.status, self.headers, self.body = status, headers, body
        self.delay = delay

    async def json(self):
        if self.delay > 0:
            await asyncio.sleep(self.delay)
        return self.body

    async def text(self):
        if self.delay > 0:
            await asyncio.sleep(self.delay)
        return self.body


class MockHTTPReq:

    def __init__(self, resp):
        self._resp = resp

    async def __aenter__(self):
        return self._resp

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


def pristine_looped(f):
    @wraps(f)
    def _f():
        old_loop = asyncio.get_event_loop()
        new_loop = asyncio.new_event_loop()
        try:
            asyncio.set_event_loop(new_loop)
            f()
        finally:
            new_loop.close()
            asyncio.set_event_loop(old_loop)
    return f


@pristine_looped
def drive_coro_once(coro, timeout=None, swallow_timeout_error=False):
    loop = asyncio.get_event_loop()
    try:
        return loop.run_until_complete(asyncio.wait_for(coro, timeout))
    except asyncio.TimeoutError as e:
        if not swallow_timeout_error:
            raise e


@pristine_looped
def drive_all(coros, timeout=None, swallow_timeout_error=True, interval=0.01):
    loop = asyncio.get_event_loop()

    async def _collector():
        tasks = []

        for coro in coros:
            tasks.append(loop.create_task(coro))
            # Loosely enforce ordering using sleep.
            # XXX: This is a FUCKING fragile test.
            await asyncio.sleep(interval)

        results = []
        for task in asyncio.as_completed(tasks):
            results.append(await task)
        return results

    return loop.run_until_complete(_collector())
