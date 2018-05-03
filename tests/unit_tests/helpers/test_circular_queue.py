import pytest
from brittle_wit.helpers import CircularQueue


@pytest.fixture
def q():
    return CircularQueue()


def test_contains(q):
    assert 'a' not in q
    q.add('a')
    assert 'a' in q


def test_bool(q):
    assert not q
    q.add('a')
    assert q


def test_add_raises_exception_on_already_contained(q):
    q.add('a')
    with pytest.raises(ValueError) as e:
        q.add('a')
    assert "already in queue" in str(e)


def test_del(q):
    q.add('a')
    assert 'a' in q
    del q['a']
    assert 'a' not in q


def test_del_raises_key_error(q):
    q.add('a')
    assert 'a' in q
    del q['a']
    with pytest.raises(KeyError):
        del q['a']


def test_pop_and_rotate(q):
    q.add('a')
    q.add('b')
    items = [q.pop_and_rotate() for _ in range(5)]
    assert items == list('babab')
