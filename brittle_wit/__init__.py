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
                                  BrittleWitError, IGNORE)
from brittle_wit.oauth import (AppCredentials, ClientCredentials,
                               ANY_CREDENTIALS)
from brittle_wit.executors import (ClientRequestProcessor,
                                   ManagedClientRequestProcessors)
from brittle_wit.helpers import parse_date
from brittle_wit.streaming import (TwitterStream,
                                   StreamProcessor,
                                   StreamingHTTPPipe)
