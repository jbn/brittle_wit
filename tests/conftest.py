import pytest


@pytest.fixture
def ignore_unawaited_request(recwarn):
    yield
    m = "coroutine 'ClientSession._request' was never awaited"
    obs_messages = {str(w.message) for w in recwarn}
    assert obs_messages == set([m])
