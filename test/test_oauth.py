import json
import os
import unittest
from functools import lru_cache

from brittle_wit import *
from brittle_wit.oauth import (_generate_nonce,
                               _generate_timestamp,
                               _generate_header_string,
                               _generate_param_string,
                               _generate_sig_base_string,
                               _generate_signing_key,
                               _generate_signature,
                               _quote,
                               generate_authorization_header)


class TestOAuth(unittest.TestCase):
    """
    Test the OAuth functions against the test data and expectations provided
    by Twitter's API documentation.

    See: https://dev.twitter.com/oauth/overview
    """
    def test_quote(self):
        self.assertEqual(_quote(1), "1")
        self.assertEqual(_quote(1.0), "1.0")

    def test_generate_nonce(self):
        self.assertEqual(len(_generate_nonce(100)), 100)
        self.assertNotEqual(_generate_nonce(), _generate_nonce())

    def test_generate_timestamp(self):
        self.assertTrue(type(_generate_timestamp()) == int)

    def test_generate_header_string(self):
        params = _load_oauth_params()
        expected = load_fixture_expectation("header_string.txt")
        self.assertEqual(_generate_header_string(params), expected)

    def test_generate_param_string(self):
        params = _load_request_params()
        expected = load_fixture_expectation("param_string.txt")
        self.assertEqual(_generate_param_string(params), expected)

    def test_generate_sig_base_string(self):
        method = "post"  # Keep lowercase as test of uppercase assurance
        url = "https://api.twitter.com/1/statuses/update.json"
        param_string = load_fixture_expectation("param_string.txt")

        result = _generate_sig_base_string(method, url, param_string)
        expected = load_fixture_expectation("sig_base_string.txt")

        self.assertEqual(result, expected)

    def test_generate_signing_key(self):
        consumer_secret = "kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw"
        token_secret = "LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE"
        k = _generate_signing_key(consumer_secret, token_secret)
        expected = load_fixture_expectation("signing_key.txt")
        self.assertEqual(k, expected)

    def test_generate_signature(self):
        signing_key = load_fixture_expectation("signing_key.txt")
        sig_base_string = load_fixture_expectation("sig_base_string.txt")
        expected = b"tnnArxj06cWHq44gCs1OSKk/jLY="

        self.assertEqual(_generate_signature(sig_base_string, signing_key),
                         expected)

    def test_generate_authorization(self):
        # Given the way generate_authorization works, this is almost an
        # integration test.
        oauth_params = _load_oauth_params()

        app = AppCredentials(oauth_params['oauth_consumer_key'],
                             "kAcSOqF21Fu85e7zjz7ZN2U4ZRhfV3WpwPAoE3Z7kBw")
        client = ClientCredentials(1,
                                   oauth_params['oauth_token'],
                                   "LswwdoUaIvS8ltyTt5jkRh4J50vUPVVHtR2YPi5kE")

        status = "Hello Ladies + Gentlemen, a signed OAuth request!"
        req = TwitterRequest("POST",
                             "https://api.twitter.com/1/statuses/update.json",
                             'statuses',
                             {'include_entities': 'true',
                              'status': status})
        expected = load_fixture_expectation("header_string.txt")

        overrides = {k: oauth_params[k]
                     for k in ['oauth_nonce', 'oauth_timestamp']}

        auth = generate_authorization_header(req, app, client, **overrides)
        self.assertEqual(set(auth.keys()), {'Authorization'})
        self.assertEqual(auth['Authorization'], expected)



FIXTURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "fixtures")

@lru_cache()
def _load_oauth_params():
    with open(os.path.join(FIXTURES_DIR, "oauth_params.json")) as fp:
        return json.load(fp)


@lru_cache()
def _load_request_params():
    with open(os.path.join(FIXTURES_DIR, "request_params.json")) as fp:
        return json.load(fp)


@lru_cache()
def load_fixture_expectation(file_name):
    print(file_name)
    with open(os.path.join(FIXTURES_DIR, file_name)) as fp:
        return fp.read()


if __name__ == '__main__':
    unittest.main()
