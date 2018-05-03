import pytest
import time
import asyncio
import random
from brittle_wit.rate_limit import RateLimit
from brittle_wit_core import (TwitterRequest, TwitterError,
                              AppCredentials, ClientCredentials)
from brittle_wit.executors import ManagedClientRequestProcessors, ANY_CREDENTIALS
from tests.helpers import async_ignore_sleep


@pytest.fixture
def alice():
    return ClientCredentials(1, "alice", "secret")


@pytest.fixture
def bob():
    return ClientCredentials(2, "bob", "secret")


@pytest.fixture
def manager():
    return ManagedClientRequestProcessors()


def test_nothing_managed_on_init(manager):
    assert not manager.is_managed(alice)


def test_managed_after_explicit_add(manager, alice):
    manager.add(alice)
    assert manager.is_managed(alice)


def test_managed_after_explicit_add_non_promiscuous(manager, alice):
    manager.add(alice, any_cred_eligible=False)
    assert manager.is_managed(alice)
    assert alice not in manager._any_cred_queue


def test_add_all(manager, alice, bob):
    manager.add_all([alice, bob])
    assert manager.is_managed(alice)
    assert manager.is_managed(bob)


def test_remove(manager, alice, bob):
    creds = [alice, bob]
    manager.add_all(creds)
    random.shuffle(creds)
    removed, kept = creds
    manager.remove(removed)
    assert kept in manager._any_cred_queue
    assert removed not in manager._any_cred_queue


def test_remove_not_any_cred(manager, alice):
    manager.add(alice, any_cred_eligible=False)
    assert alice not in manager._any_cred_queue
    manager.remove(alice)
    assert alice not in manager._any_cred_queue


def test_add_cannot_add_dup(manager, bob):
    manager.add(bob)
    with pytest.raises(RuntimeError):
        manager.add(bob)


def test__getitem__(manager, alice, bob):
    assert manager[alice]._client_cred == alice
    assert manager[bob]._client_cred == bob

    observed = {manager[ANY_CREDENTIALS]._client_cred for _ in range(10)}
    expected = {alice, bob}
    assert observed == expected


def test__getitem__anycred_exhausted(manager, bob):
    assert manager[ANY_CREDENTIALS] is None
    manager.add(bob)
    assert manager[ANY_CREDENTIALS] == bob


def test__maintain(manager, alice, bob):
    manager.add_all([alice, bob], False)

    now = time.time()
    manager[alice]._rate_limits['future'] = RateLimit(1, 1, now + 100)
    manager[bob]._rate_limits['passed'] = RateLimit(1, 1, now - 100)

    assert manager.is_managed(alice)
    assert manager.is_managed(bob)

    manager._maintain()

    assert manager.is_managed(alice)
    assert not manager.is_managed(bob)


def test__maintain_with_any_cred(manager, alice):
    manager.add_all([alice], True)
    now = time.time()
    manager[alice]._rate_limits['passed'] = RateLimit(1, 1, now - 100)
    assert manager.is_managed(alice)

    manager._maintain()
    assert manager.is_managed(alice)


@pytest.mark.asyncio
async def test_maintain_reraise_keyboard_interrupt(manager, mocker):
    path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
    _maintain = mocker.patch(path, side_effect=KeyboardInterrupt())
    with async_ignore_sleep() as sleep_times:
        with pytest.raises(KeyboardInterrupt):
            await manager.maintain()


@pytest.mark.asyncio
async def test_maintain_graceful_shutdown(manager, mocker):
    path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
    _maintain = mocker.patch(path, side_effect=asyncio.CancelledError())
    with async_ignore_sleep() as sleep_times:
        await manager.maintain()


@pytest.mark.asyncio
async def test_maintain_catches_all_else(manager, mocker):
    exceptions = [RuntimeError("test"), KeyboardInterrupt()]

    def f():
        raise exceptions.pop(0)

    path = 'brittle_wit.executors.ManagedClientRequestProcessors._maintain'
    _maintain = mocker.patch(path, side_effect=f)
    with async_ignore_sleep() as sleep_times:
        with pytest.raises(KeyboardInterrupt):
            await manager.maintain()
