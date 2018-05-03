import asyncio
import json
import logging
import os
import unittest
from unittest.mock import Mock, patch
from contextlib import contextmanager
from collections import namedtuple
from functools import wraps
from inspect import iscoroutinefunction


SELF_DIR = os.path.dirname(os.path.realpath(__file__))

FIXTURES_DIR = os.path.join(SELF_DIR, "fixtures")

SERIALIZATION_DIR = os.path.join(SELF_DIR, "tmp")


def load_fixture_txt(file_name):
    print(FIXTURES_DIR)
    with open(os.path.join(FIXTURES_DIR, file_name)) as fp:
        return fp.read()


def load_fixture_json(file_name):
    with open(os.path.join(FIXTURES_DIR, file_name)) as fp:
        return json.load(fp)


@contextmanager
def async_patch(*args, **kwargs):
    value = kwargs.get('return_value')
    if 'return_value' in kwargs:
        del kwargs['return_value']

    async def basic_coro():
        return value

    def side_effect(*args, **kwargs):
        return basic_coro()  # Make a new coroutine for each call.

    kwargs['side_effect'] = side_effect

    with unittest.mock.patch(*args, **kwargs) as f:
        yield f


@contextmanager
def async_ignore_sleep():
    with async_patch('asyncio.sleep') as f:
        def sleep_times():
            return [call[0][0] for call in f.call_args_list]
        yield sleep_times


def mock_http_req(status, closed, body_as_text=''):

    async def text():
        return body_as_text

    resp = Mock()
    resp.connection.closed = closed
    resp.status = status
    resp.text = lambda: text()

    class MockReq:
        async def __aenter__(self):
            return resp

    return MockReq()


def ensure_deleted(file_path):
    try:
        os.unlink(file_path)
    except FileNotFoundError:
        pass


def mock_content_reader(messages, delay=0):
    messages = messages[:]

    async def read(n):
        if delay != 0:
            await asyncio.sleep(delay)
        return messages.pop(0) if messages else ''

    resp = Mock()
    resp.content.read = lambda n: read(n)
    return resp


def mock_stream(messages):
    messages = messages[:]

    class MockStream:

        async def __aiter__(self):
            return self

        async def __anext__(self):
            if not messages:
                raise StopAsyncIteration

            msg = messages.pop(0)

            if isinstance(msg, BaseException):
                raise msg
            else:
                return msg

        def disconnect(self):
            pass

    return MockStream()


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


def make_coro_runner(f):

    @wraps(f)
    def coro_runner_test(self):
        # Create a new event loop.
        loop = asyncio.new_event_loop()
        loop.set_debug(True)
        logging.getLogger('asyncio').setLevel(logging.WARNING)
        asyncio.set_event_loop(loop)

        # Run it.
        loop.run_until_complete(f(self))

        # Close it.
        loop.close()

    return coro_runner_test


class AsyncSafeTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        updates = {}
        for k, f in vars(cls).items():
            if k.startswith('test') and iscoroutinefunction(f):
                setattr(cls, k, make_coro_runner(f))


# https://blog.miguelgrinberg.com/post/unit-testing-asyncio-code
def AsyncMock(*args, **kwargs):
    m = mock.MagicMock(*args, **kwargs)

    async def mock_coro(*args, **kwargs):
        return m(*args, **kwargs)

    mock_coro.mock = m
    return mock_coro
