import os
import unittest
import brittle_wit as bw
from test.helpers import FIXTURES_DIR
from brittle_wit.api_tools import (NOT_SPECIFIED,
                                   generate_api_request_builder_func,
                                   _update_params_ordering_required_first,
                                   _slugged_pythonic_string,
                                   _generate_func_name,
                                   _generate_doc_str,
                                   _generate_slugger,
                                   _generate_signature)
from collections import OrderedDict


TEST_DEF = {"method": "POST",
            "url": "https://brittle-wit.artifexdeus.com/api/mock/:id",
            "service": "mock/:id/content",
            "family": "mock",
            "resp_format": [
                "JSON"
            ],
            "rate_limited": True,
            "authentication_required": "YES",
            "limits": {
                "app": 42,
                "user": 42
            },
            "desc": "A mock service",
            "params": OrderedDict([
                ("auth", [
                    "REQUIRED",
                    "Auth token for user."
                ]),
                ("limit", [
                    "OPTIONAL",
                    "The number of elements to return. Defaults to 500 if not specified."
                ]),
                ("format", [
                    "OPTIONAL",
                    "The output format request. This param can be either json or xml. It will default to json."
                ]),
            ]),
            "reference_url": "https://dev.twitter.com/rest/reference/get/example"}


class TestRestAPI(unittest.TestCase):

    def test_generate_signature(self):
        sig = _generate_signature(TEST_DEF)
        self.assertEqual(list(sig.parameters.keys()), ['auth', 'limit', 'format'])

        auth, limit, format = list(sig.parameters.values())
        self.assertEqual(auth.default, auth.empty)
        self.assertEqual(limit.default, NOT_SPECIFIED)
        self.assertEqual(format.default, NOT_SPECIFIED)

    def test_generate_doc_str(self):
        with open(os.path.join(FIXTURES_DIR, "doc_str.txt")) as fp:
            expected = fp.read()
        self.assertEqual(_generate_doc_str(TEST_DEF).strip(), expected.strip())

    def test_update_params_ordering_required_first(self):
        api_def = dict(params=OrderedDict([("a", ('REQUIRED', "desc")),
                                           ("b", ('OPTIONAL', "desc")),
                                           ("c", ('OPTIONAL', "desc")),
                                           ("d", ('REQUIRED', "desc"))]))

        _update_params_ordering_required_first(api_def)
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

    def test_generate_func_name(self):
        s = _generate_func_name(TEST_DEF['service'],
                                TEST_DEF['family'],
                                TEST_DEF['method'])
        self.assertEqual(s, "content_by_id")

        # Special cases.
        self.assertEqual(_generate_func_name("media/upload(INIT)", "", ""),
                         "upload_init")

    def test_generate_api_request_builder_func(self):
        f = generate_api_request_builder_func(TEST_DEF)
        req = f("hello", limit=20, format='yoho')
        self.assertEqual(req.method, 'POST')
        self.assertEqual(req.url, TEST_DEF['url'])
        self.assertEqual(req.family, 'MOCK')
        self.assertEqual(req.service, 'MOCK/:ID/CONTENT')
        self.assertEqual(req.parse_as, 'json')
        self.assertEqual(req.params, {'auth': 'hello', 'format': 'yoho', 'limit': 20})

    def test_geo_search(self):
        if not hasattr(bw, 'rest_api'):
            return

        # Note attribute_street_address -> attribute:street_address
        req = bw.rest_api.geo.search(attribute_street_address="sullivan street")
        self.assertEqual(req.method, "GET")
        self.assertEqual(req.family, "GEO")
        self.assertEqual(req.url,
                         "https://api.twitter.com/1.1/geo/search.json")
        self.assertIn("attribute:street_address", req.params)
        self.assertEqual(req.params["attribute:street_address"],
                         "sullivan street")
