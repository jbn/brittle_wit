__version__ = "0.0.1"

import os


from brittle_wit.constants import LOGGER, FIFTEEN_MINUTES
from brittle_wit.messages import (TwitterRequest, Cursor, TwitterResponse,
                                  BrittleWitError)
from brittle_wit.oauth import (AppCredentials, ClientCredentials,
                               ANY_CREDENTIALS)
from brittle_wit.executors import (ClientRequestProcessor,
                                   ContextualizedProcessor,
                                   ManagedClientRequestProcessors)

from brittle_wit.helpers import parse_date
from brittle_wit.rest_api import build_api
from brittle_wit.streaming import (TwitterStream,
                                   StreamProcessor,
                                   StreamingHTTPPipe)


# By default, build each API endpoint into a function. Access the endpoints by
# dot-accessing the family. For example, `api.statuses.home_timeline()`. To
# disable API building -- mostly, if you are just issuing custom requests --
# set the API_BUILD environmental variable to 'SKIP'.
if os.environ.get('API_BUILD', '') != 'SKIP':
    LOGGER.debug("Building API from `api_reference.json`")
    api = build_api(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                 "api_reference.json"))
