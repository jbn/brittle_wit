__version__ = "0.0.1"

import os

FIFTEEN_MINUTES = 15 * 60

from brittle_wit.twitter_request import TwitterRequest
from brittle_wit.twitter_response import TwitterResponse
from brittle_wit.oauth import (AppCredentials, ClientCredentials,
                               ANY_CREDENTIALS)
from brittle_wit.brittle_wit_error import BrittleWitError
from brittle_wit.executors import (ClientRequestProcessor,
                                   ManagedClientRequestProcessors)

from brittle_wit.helpers import parse_date
from brittle_wit.rest_api import build_api


# By default, build each API endpoint into a function. Access the endpoints by
# dot-accessing the family. For example, `api.statuses.home_timeline()`. To
# disable API building -- mostly, if you are just issuing custom requests --
# set the API_BUILD environmental variable to 'SKIP'.
if os.environ.get('API_BUILD', '') != 'SKIP':
    api = build_api(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 "rest_api.json"))

