__title__ = "brittle_wit"
__description__ = "Brittle Wit is a Twitter Lib for Python."
__uri__ = "https://github.com/jbn/brittle_wit"
__doc__ = __description__ + " <" + __uri__ + ">"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2017 John Bjorn Nelson"
__version__ = "0.0.5"
__author__ = "John Bjorn Nelson"
__email__ = "jbn@abreka.com"


from brittle_wit_core import AppCredentials, ClientCredentials
from brittle_wit_core import BrittleWitError, Cursor, ELIDE
from brittle_wit.executors import (ANY_CREDENTIALS,
                                   ClientRequestProcessor,
                                   LOGGER,
                                   ManagedClientRequestProcessors)
from brittle_wit.streaming import (basic_streamer,
                                   StreamProcessor,
                                   StreamingHTTPPipe,
                                   TwitterStream)
from brittle_wit.app import App
from brittle_wit.helpers import monkey_patch_ipython_disp


def _patch_retryables():
    import aiohttp
    import asyncio
    import brittle_wit_core
    exceptions = brittle_wit_core.WrappedException.RETRYABLE_EXCEPTIONS
    exceptions.add(aiohttp.ClientOSError)
    exceptions.add(aiohttp.ClientConnectorError)
    exceptions.add(asyncio.TimeoutError)

_patch_retryables()
