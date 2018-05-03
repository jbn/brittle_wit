from tests.helpers import load_fixture_txt
import brittle_wit.rest_api as rest_api
from brittle_wit.helpers import _twitter_request_html_repr



def test_twitter_request_html_repr():
    expected = load_fixture_txt("ipython_html.html")
    req = rest_api.direct_messages.new("hello world")
    assert _twitter_request_html_repr(req).strip() == expected.strip()
