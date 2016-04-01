import unittest
import brittle_wit as bw
from brittle_wit import rest_api
from brittle_wit.rest_api import _slugged_pythonic_string, _generate_slugger
from collections import OrderedDict


class TestRestAPI(unittest.TestCase):

    def test_geo_search(self):
        # Note attribute_street_address -> attribute:street_address
        req = bw.api.geo.search(attribute_street_address="sullivan street")
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.family, "GEO")
        self.assertEqual(req.url,
                         "https://api.twitter.com/1.1/geo/search.json")
        self.assertIn("attribute:street_address", req.params)
        self.assertEqual(req.params["attribute:street_address"],
                         "sullivan street")

    def test_update_params_ordering_required_first(self):
        api_def = dict(params=OrderedDict([("a", ('REQUIRED', "desc")),
                                           ("b", ('OPTIONAL', "desc")),
                                           ("c", ('OPTIONAL', "desc")),
                                           ("d", ('REQUIRED', "desc"))]))

        rest_api._update_params_ordering_required_first(api_def)
        keys = list(api_def['params'].keys())
        self.assertEqual(set(keys[:2]), {"a", "d"})
        self.assertEqual(set(keys[2:]), {"b", "c"})

    def test_slugged_pythonic_string(self):
        examples = [("https://api.twitter.com/1.1/geo/id/:place_id.json",
                     ('https://api.twitter.com/1.1/geo/id/{place_id}',
                      ['place_id'])),
                    ("https://api.twitter.com/1.1/:user_id/id/:place_id.json",
                     ('https://api.twitter.com/1.1/{user_id}/id/{place_id}',
                      ['user_id', 'place_id'])),
                    ("https://api.twitter.com/1.1/geo/id/home",
                     None)]

        for url, expected in examples:
            self.assertEqual(_slugged_pythonic_string(url),
                             expected)

    def test_generate_slugger(self):
        f = _generate_slugger('https://api.twitter.com/1.1/geo/id/{pid}',
                              ['pid'])
        params = dict(pid=100)
        self.assertIn('pid', params)
        self.assertEqual(f(params), "https://api.twitter.com/1.1/geo/id/100")
        self.assertNotIn('pid', params)

        f = _generate_slugger('https://api.twitter.com/1.1/{gid}/id/{pid}',
                              ['gid', 'pid'])
        params = dict(pid=100, gid=200)
        self.assertIn('pid', params)
        self.assertIn('gid', params)
        self.assertEqual(f(params), "https://api.twitter.com/1.1/200/id/100")
        self.assertNotIn('pid', params)
        self.assertNotIn('gid', params)
