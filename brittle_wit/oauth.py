"""
This module contains a bare-bones OAuth implementation. It is
minimally-compliant so as to conform to Twitter's requirements.

See: https://dev.twitter.com/oauth/overview
"""

import binascii
import hashlib
import hmac
import random
import time

from urllib.parse import quote


ALPHANUMERIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def _generate_nonce(length=42):
    """
    Generate an alpha numeric string that is unique for each request.

    Twitter used a 42 character alpha-numeric (case-sensitive) string in the
    API documentation. However, they note "any approach which produces a
    relatively random alphanumeric string should be OK here." I opted not to
    use a cryptographically secure source of entropy. `SystemRandom` is
    convenient, but it uses file IO to connect to `/dev/urandom`. Adding
    `async` machinery here seems like expensive complexity.
    """
    return "".join(random.choice(ALPHANUMERIC) for _ in range(length))


def _generate_timestamp():
    return int(time.time())


def _generate_header_string(params):
    """
    Generate the string for use in the http "Authorization" header field.

    :param params: a dictionary with the oauth_* key-values.
    """
    return "OAuth " + ", ".join('{}="{}"'.format(k, quote(params[k], safe=''))
                                for k in sorted(params))


def _generate_param_string(params):
    """
    Generate the parameter string for signing.

    :param params: A dictionary with both the request and oauth_* parameters,
        less the `oauth_signature`.
    """
    d = {quote(k, safe=''): quote(v, safe='') for k, v in params.items()}
    return "&".join(["{}={}".format(k, d[k]) for k in sorted(d)])


def _generate_sig_base_string(method, base_url, param_string):
    """
    :param method: either `get` or `post`
    :param base_url: the API base URL (i.e. without parameters)
    :param param_string: string generated by generate_param_string
    """
    return "&".join([method.upper(),
                     quote(base_url, safe=''),
                     quote(param_string, safe='')])


def _generate_signing_key(consumer_secret, oauth_token_secret):
    return "{}&{}".format(quote(consumer_secret, safe=''),
                          quote(oauth_token_secret, safe=''))


def _generate_signature(sig_base_string, signing_key):
    digest = hmac.new(signing_key.encode('ascii'),
                      sig_base_string.encode('ascii'),
                      hashlib.sha1).digest()

    return binascii.b2a_base64(digest)[:-1]  # Strip newline


def generate_authorization_header(twitter_req, app_cred, client_cred,
                                  **overrides):
    """
    Generate the 'Authorization' HTTP-header field as a dict.

    :param twitter_req: A TwitterRequest object
    :param app_cred: an AppCredentials object
    :param client_cred: a ClientCredentials object
    :param overrides: key-value pairs which override (or, adds a new value
        to) the oauth_* dictionary used for signature generation.
    """
    oauth_d = {'oauth_consumer_key': app_cred.key,
               'oauth_nonce': _generate_nonce(),
               'oauth_signature_method': "HMAC-SHA1",
               'oauth_timestamp': str(_generate_timestamp()),
               'oauth_token': client_cred.token,
               'oauth_version': "1.0"}

    if overrides:
        oauth_d.update(overrides)

    param_string = _generate_param_string({**oauth_d, **twitter_req.params})
    sig_base_string = _generate_sig_base_string(twitter_req.method,
                                                twitter_req.url,
                                                param_string)
    signing_key = _generate_signing_key(app_cred.secret, client_cred.secret)
    oauth_d['oauth_signature'] = _generate_signature(sig_base_string,
                                                     signing_key)
    return {'Authorization': _generate_header_string(oauth_d)}
