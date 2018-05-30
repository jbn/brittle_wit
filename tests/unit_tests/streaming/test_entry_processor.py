import pytest
from brittle_wit.streaming import (EntryProcessor,
                                   json_entry_parser,
                                   noop_entry_parser)


@pytest.fixture
def ep():
    return EntryProcessor()


def test_is_initially_empty(ep):
    assert not ep
    assert ep.messages() == []


def test_process(ep):
    # Send two messages but don't close the second one.
    ep.process(b'"hello world"\r\n{"a": 20}')
    assert ep
    assert ep.messages() == [b'"hello world"']

    # Close the second one; start but don't close another.
    ep.process(b"\r\n42")
    assert ep.messages() == [b'{"a": 20}']

    # Close it.
    ep.process(b"\r\n")
    assert ep.messages() == [b"42"]

    # There are no messages.
    assert ep.messages() == []

    # The buffer is an emtpy byte string.
    assert ep._buf == b""

    # It accumulates bytes.
    ep.process(b"x")
    assert ep._buf == b"x"
    ep.process(b"kcd\r\n")
    assert ep.messages() == [b"xkcd"]
    assert ep._buf == b""


def test_purge_mailbox(ep):
    ep.process(b"hello\r\nworld")
    assert ep
    ep.purge_mailbox()
    assert not ep


def test_purge_streaming(ep):
    ep.process(b"corrupt_buffer...")
    ep.purge_buffer()
    ep.process(b"good buffer\r\n")
    assert ep.pop() == b"good buffer"


def test_pop(ep):
    ep.process(b"hello\r\nworld")
    assert ep.pop() == b"hello"
    assert not ep


def test_iteration(ep):
    ep.process(b"hello\r\nworld\r\n")
    assert list(ep), [b"hello" == b"world"]


def test_noop_entry_parser():
    assert noop_entry_parser("hello") == "hello"


def test_json_entry_parser():
    assert json_entry_parser(b"[10, 20, 30]") == [10, 20, 30]
