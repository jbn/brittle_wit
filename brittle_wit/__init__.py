__title__ = "brittle_wit"
__description__ = "Brittle Wit is a Twitter Lib for Python."
__uri__ = "https://github.com/jbn/brittle_wit"
__doc__ = __description__ + " <" + __uri__ + ">"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2017 John Bjorn Nelson"
__version__ = "0.0.3"
__author__ = "John Bjorn Nelson"
__email__ = "jbn@abreka.com"

import os

from brittle_wit.constants import LOGGER, FIFTEEN_MINUTES
from brittle_wit.messages import (TwitterRequest, Cursor, TwitterResponse,
                                  BrittleWitError)
from brittle_wit.oauth import (AppCredentials, ClientCredentials,
                               ANY_CREDENTIALS)
from brittle_wit.executors import (ClientRequestProcessor,
                                   ManagedClientRequestProcessors)
from brittle_wit.helpers import parse_date
from brittle_wit.api_tools import build_api
from brittle_wit.streaming import (TwitterStream,
                                   StreamProcessor,
                                   StreamingHTTPPipe)


# By default, build each API endpoint into a function. Access the endpoints by
# dot-accessing the family. For example, `rest_api.statuses.home_timeline()`.
# To disable API building -- mostly, if you are just issuing custom
# requests -- set the respective environmental variable to 'SKIP'.
def _build_from_file(file_name):
    LOGGER.debug("Building API from `{}`".format(file_name))
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             file_name)
    return build_api(file_path)


if os.environ.get('BUILD_REST_API', '') != 'SKIP':
    rest_api = _build_from_file("rest_api.json")

if os.environ.get('BUILD_STREAMING_API', '') != 'SKIP':
    streaming_api = _build_from_file("streaming_api.json")

if os.environ.get('BUILD_ADS_API', '') != 'SKIP':
    ads_api = _build_from_file("ads_api.json")

if os.environ.get('BUILD_WEBHOOK_API', '') != 'SKIP':
    webhook_api = _build_from_file("webhook_api.json")
