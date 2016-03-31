__version__ = "0.0.1"

import os
from collections import namedtuple

from brittle_wit.twitter_request import TwitterRequest
TwitterResponse = namedtuple('TwitterResponse', 'request response body')

from brittle_wit.scheduling import RequestProcessor
from brittle_wit.parsing import parse_date
from brittle_wit.oauth import AppCredentials, ClientCredentials
from brittle_wit.rest_api import build_api

if os.environ.get('API_BUILD', '') != 'SKIP':
    api = build_api(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 "rest_api.json"))

