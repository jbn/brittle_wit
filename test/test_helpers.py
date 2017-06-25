import os
import unittest
import brittle_wit as bw
from test.helpers import FIXTURES_DIR
from brittle_wit.helpers import *
from brittle_wit.ipython_helpers import twitter_request_html_repr


class TestHelpers(unittest.TestCase):

    def test_parse_date(self):
        s = "tue mar 29 15:40:03 +0000 2016"
        self.assertEqual(parse_date(s).timestamp(), 1459266003.0)

    def test_wrapping_handler(self):
        messages = []

        handler = WrappingHandler(lambda msg: messages.append(msg))
        handler.send("hello.")
        handler.send("it's me.")

        self.assertEqual(" ".join(messages), "hello. it's me.")


# class TestIPythonHelpers(unittest.TestCase):

#     def test_twitter_request_html_repr(self):
#         with open(os.path.join(FIXTURES_DIR, "ipython_html.html")) as fp:
#             expected = fp.read()

#         req = bw.rest_api.direct_messages.new("hello world")
#         self.assertEqual(twitter_request_html_repr(req).strip(),
#                          expected.strip())
