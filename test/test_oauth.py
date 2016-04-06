import json
import unittest
from functools import lru_cache

from brittle_wit import *
from brittle_wit import TwitterRequest
from brittle_wit.oauth import (_generate_nonce,
                               _generate_timestamp,
                               _generate_header_string,
                               _generate_param_string,
                               _generate_sig_base_string,
                               _generate_signing_key,
                               _generate_signature,
                               _quote,
                               generate_req_headers,
                               AppCredentials)


class TestOAuth(unittest.TestCase):
    """
    Test the OAuth functions against the test data and expectations provided
    by Twitter's API documentation.

    See: https://dev.twitter.com/oauth/overview
    """
    def test_quote(self):
        self.assertEqual(_quote(1), "1")
        self.assertEqual(_quote(1.0), "1.0")
        self.assertEqual(_quote(True), "true")
        self.assertEqual(_quote(False), "false")

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

    def test_generate_req_headers(self):
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
                             'statuses/update',
                             include_entities='true',
                             status=status)
        expected = load_fixture_expectation("header_string.txt")

        overrides = {k: oauth_params[k]
                     for k in ['oauth_nonce', 'oauth_timestamp']}

        auth = generate_req_headers(req, app, client, **overrides)
        self.assertIn('Authorization', auth.keys())
        self.assertEqual(auth['Authorization'], expected)


class TestAppCredentials(unittest.TestCase):
    def test_app_credentials(self):
        app_1 = AppCredentials("app_1", "secret")
        self.assertEqual(app_1, AppCredentials("app_1", "secret"))

        app_2 = AppCredentials("app_2", "password")
        self.assertNotEqual(app_1, app_2)

        self.assertEqual(len({app_1, app_2}), 2)
        self.assertEqual(str(app_1), "AppCredentials(app_1, ******)")
        self.assertEqual(repr(app_1), "AppCredentials(app_1, ******)")

        with self.assertRaises(AttributeError):
            app_1.key = 10  # Immutable(ish)


class TestClientCredentials(unittest.TestCase):
    def test_client_credentials(self):
        client_1 = ClientCredentials(1, "token_1", "secret")
        self.assertEqual(client_1, ClientCredentials(1, "token_1", "secret"))

        client_2 = ClientCredentials(2, "token_2", "secret")
        self.assertNotEqual(client_1, client_2)

        self.assertEqual(len({client_1, client_2}), 2)
        self.assertEqual(str(client_1),
                         "ClientCredentials(1, token_1, ******)")
        self.assertEqual(repr(client_1),
                         "ClientCredentials(1, token_1, ******)")

        with self.assertRaises(AttributeError):
            client_1.token = 10  # Immutable(ish)

        self.assertTrue(client_2 > client_1)

    def test_dict_serialization(self):
        client_1 = ClientCredentials(1, "token_1", "secret")
        client_2 = ClientCredentials.from_dict(client_1.as_dict)

        self.assertEqual(client_1.user_id, client_2.user_id)
        self.assertEqual(client_1.secret, client_2.secret)
        self.assertEqual(client_1.token, client_2.token)


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
