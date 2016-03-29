import unittest

from brittle_wit.parsing import *


class TestParsing(unittest.TestCase):
    """
    Test the OAuth functions against the test data and expectations provided
    by Twitter's API documentation.

    See: https://dev.twitter.com/oauth/overview
    """
    def test_parse_date(self):
        s = "Tue Mar 29 15:40:03 +0000 2016"
        self.assertEqual(parse_date(s).timestamp(), 1459266003.0)
