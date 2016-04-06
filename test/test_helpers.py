import unittest

from brittle_wit.helpers import *


class TestHelpers(unittest.TestCase):

    def test_parse_date(self):
        s = "Tue Mar 29 15:40:03 +0000 2016"
        self.assertEqual(parse_date(s).timestamp(), 1459266003.0)

    def test_wrapping_handler(self):
        messages = []

        handler = WrappingHandler(lambda msg: messages.append(msg))
        handler.send("hello.")
        handler.send("it's me.")

        self.assertEqual(" ".join(messages), "hello. it's me.")
