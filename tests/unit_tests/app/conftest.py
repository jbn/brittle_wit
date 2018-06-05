import pytest
import asyncio

from brittle_wit.app import App
from brittle_wit import AppCredentials, ClientCredentials


@pytest.fixture
def app_cred():
    return AppCredentials('app', 'secret')


@pytest.fixture
def client_cred():
    return ClientCredentials(1, 'user', 'secret')


@pytest.fixture
def app(app_cred):
    app = App.with_defaults(app_cred)
    yield app
    asyncio.get_event_loop().run_until_complete(app._session.close())
