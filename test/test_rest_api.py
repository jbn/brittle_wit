import unittest
import brittle_wit as bw


class TestRestAPI(unittest.TestCase):

    def test_from_ignorance(self):
        # Note attribute_street_address -> attribute:street_address
        req = bw.api.geo.search(attribute_street_address="sullivan street")
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.family, "geo")
        self.assertEqual(req.url,
                         "https://api.twitter.com/1.1/geo/search.json")
        self.assertFalse(req.supports_cursor)
        self.assertIn("attribute:street_address", req.params)
        self.assertEqual(req.params["attribute:street_address"],
                         "sullivan street")
