import asyncio
import aiohttp
import time

from brittle_wit.constants import FIFTEEN_MINUTES, LOGGER
from brittle_wit.oauth import generate_req_headers, ANY_CREDENTIALS
from brittle_wit.rate_limit import RateLimit
from brittle_wit.ticketing import TicketMaster
from brittle_wit.messages import (TwitterResponse, TwitterError,
                                  WrappedException, BrittleWitError)


def twitter_req_to_http_req(session, app_cred, client_cred, twitter_req):
    headers = generate_req_headers(twitter_req, app_cred, client_cred)
    
    if twitter_req.method == 'POST':
        return session.request(twitter_req.method,
                               twitter_req.url,
                               data=twitter_req.params,
                               headers=headers)
    else:
        return session.request(twitter_req.method,
                               twitter_req.url,
                               params=twitter_req.params,
                               headers=headers)


async def execute_req(credentials, twitter_req, http_req, rate_limit, timeout):
    """
    Execute a request with no exception handling.

    :param credentials: the credentials used to build the http_req
    :param twitter_req: the original TwitterRequest
    :param http_req: the HttpRequest with encoded authentication information
    :param rate_limit: the RateLimit object associated with the endpoint and
        credentials
    :param timeout: the time, in seconds, to wait before an exception is
        thrown
    :return: a TwitterResponse
    """
    LOGGER.info("Executing %s request (%s) for %s",
                credentials.user_id, id(twitter_req), twitter_req.service)
    try:
        with aiohttp.Timeout(timeout):

            # Send request over the wire.
            async with http_req as resp:

                # Update rate limits ASAP. Note: The prior call to comply
                # decremented the rate limits already. If the context manager
                # threw an exception on entry, it is still in compliance.
                rate_limit.update(resp)

                # An error occurred.
                if resp.status != 200:
                    raise TwitterError(credentials,
                                       twitter_req,
                                       resp,
                                       await resp.json())

                # The status code indicates a good response.
                if twitter_req.parse_as == 'json':
                    body = await resp.json()
                else:
                    body = await resp.text()

                return TwitterResponse(twitter_req, resp, body)
    except TwitterError as e:
        LOGGER.exception("Failed %s request (%s) for %s with %s",
                         credentials.user_id,
                         twitter_req.service,
                         id(twitter_req),
                         e.status_code)
        raise e
    except Exception as e:
        LOGGER.exception("Failed %s request (%s) for %s",
                         credentials.user_id,
                         twitter_req.service,
                         id(twitter_req))
        raise WrappedException(e)


class ClientRequestProcessor:
    """
    The ClientRequestProcessor manages rate limits while executing requests.

    When the caller issues a request for execution, the request processor
    enforces rate limitations. Such enforcement occurs in the context of the
    given credentials and for a given service. If multiple callers request
    execution at the same time (for a given set of credentials and service),
    the requests execute FIFO.
    """

    def __init__(self, client_credentials):
        """
        :param client_credentials: the ClientCredentials to manage
        """
        self._client_credentials = client_credentials
        self._ticket_master = TicketMaster()
        self._rate_limits = {}

    @property
    def user_id(self):
        return self._client_credentials.user_id

    def _rate_limit_for(self, service):
        """
        Get existing or create new RateLimit for the given service.

        :param service: API endpoint service
        :return: the RateLimit object associated with the service
        """
        limit = self._rate_limits.get(service)

        if limit is not None:
            return limit
        else:
            max_requests = RateLimit.CLIENT_LIMITS[service]
            limit = RateLimit(max_requests,
                              max_requests,
                              time.time() + FIFTEEN_MINUTES)
            self._rate_limits[service] = limit
            return limit

    def cleanup(self, now=None):
        """
        Remove all rate limits which have expired.

        :param now: the current time as per time.time()
        """
        rate_limits = self._rate_limits

        # Abort quickly if possible.
        if not rate_limits:
            return

        now = now or time.time()

        remove_ks = []
        for service, rate_limit in rate_limits.items():
            # If the reset time is in the past, remove it.
            if rate_limit.reset_time < now:
                remove_ks.append(service)

        for k in remove_ks:
            del rate_limits[k]

    def is_removable(self):
        """
        :return: True if this executor is not in use and is monitoring no
            rate limits
        """
        return self.is_not_processing() and not self._rate_limits

    def is_not_processing(self):
        """
        :return: True if no caller is using this processors' credentials for
            any endpoint otherwise True
        """
        return self._ticket_master.all_lines_empty()

    def is_immediately_available_for(self, service):
        """
        :param service: the API service name, as per the Twitter docs
        :return: True if no caller is using this objects associated credentials
            for the given service AND that service is not rate limited
        """
        if self._ticket_master.is_line_empty(service):
            if service not in self._rate_limits:
                return True
            else:
                return not self._rate_limits[service].is_exhausted
        return False

    async def _execute(self, session, app_cred, twitter_req, timeout=120):
        service = twitter_req.service

        LOGGER.debug("Waiting for ticket on %s request (%s) for %s",
                     self._client_credentials.user_id,
                     id(twitter_req),
                     twitter_req.service)
        async with self._ticket_master.take_ticket(service):
            # The caller is now in charge of this service.
            rate_limit = self._rate_limit_for(service)

            # Block request execution until not rate limited.
            await rate_limit.comply()

            http_req = twitter_req_to_http_req(session,
                                               app_cred,
                                               self._client_credentials,
                                               twitter_req)

            # This coroutine will raise an exception for non-200 statuses.
            return await execute_req(self._client_credentials,
                                     twitter_req,
                                     http_req,
                                     rate_limit,
                                     timeout)

    async def execute(self, session, app_cred, twitter_req, timeout=120,
                      n_retries=5):
        tries = 0
        while True:
            try:
                return await self._execute(session, app_cred,
                                           twitter_req, timeout)
            except BrittleWitError as e:
                tries += 1
                if not e.is_retryable or tries >= n_retries:
                    raise e
                else:
                    await asyncio.sleep(60 * tries)  # Sleep progressively


class ContextualizedProcessor:
    def __init__(self, session, app_cred, client_processor):
        self._session = session
        self._app_cred = app_cred
        self._client_processor = client_processor

    @property
    def user_id(self):
        return self._client_processor.user_id

    def __call__(self, twitter_req, timeout=60):
        return self._client_processor.execute(self._session,
                                              self._app_cred,
                                              twitter_req,
                                              timeout)


class ManagedClientRequestProcessors:
    """

    = Any Credential Management

    For many tasks, you don't need specific credentials, you just need some
    credentials. For example, if you and your social network analyst friends
    wanted to analyze the followers of Bernie Sanders, you need to collect all
    the user objects. Given that there are millions of them that could take
    time. But, if you already have the user id's you can partition the
    collection and run it in parallel. The specific credentials don't matter.
    (Well, ignoring the case of a follower blocking that person.)

    Finding an unused set of credentials is non-trivial. Managing a ready-queue
    for each service is expensive in terms of space when there are many users.
    (See notes on sparsity in rateLimit.RateLimitEnforcer.) As an alternative,
    I rely on probability. (That is, until I think more and find a better
    solution.)

    The any_cred_queue maintains a circular buffer for each set of
    credentials. When a client asks for AnyCredentials, the queue pops
    credentials off the top. When it asks again, it pushes that initial item
    to the end of the queue, and pops the head again.

    This is far from perfect. For example, this could select a token that is
    currently rate-limited even though non-limited ones remain. But, it's
    cheap, and does well, probabilistically. Additionally, I believe this
    should perform better as the number of managed users rises. (I'll think
    more about it; then, pen an arXiv article.)
    """
    def __init__(self):
        self._credentials = {}
        self._any_cred_queue = []

    def is_managed(self, cred):
        return cred in self._credentials

    def add(self, cred):
        assert not self.is_managed(cred)

        client_req_processor = ClientRequestProcessor(cred)
        self._credentials[cred] = client_req_processor

        # Add a new set of credentials to the front of the queue.
        self._any_cred_queue.insert(0, cred)

        return client_req_processor

    def remove(self, cred):
        del self._credentials[cred]
        self._any_cred_queue.remove(cred)

    def __getitem__(self, cred):
        if cred is ANY_CREDENTIALS:
            credentials = self._any_cred_queue.pop(0)
            self._any_cred_queue.append(credentials)
            return self[credentials]
        else:
            managed = self._credentials.get(cred)

            if not managed:
                managed = self.add(cred)

            return managed

    def maintain(self, cull_interval=FIFTEEN_MINUTES):
        now = time.time()

        # Collect
        removal_keys = []
        for k, req_processor in self._credentials.items():
            req_processor.cleanup(now)  # Remove disused rate limits

            if req_processor.is_removable():
                removal_keys.append(k)

        # Remove
        for k in removal_keys:
            self.remove(k)


async def repeating(interval, f, *args, **kwargs):
    """
    Call f(**args, **kwargs) every interval seconds.

    :param interval: the interval in seconds
    :param f: a function
    :param args: positional arguments
    :param kwargs: keyword arguments
    """
    while True:
        f(*args, **kwargs)  # Do test for coro?
        await asyncio.sleep(interval)

# I don't want to require requests as a dependency. And, I really don't want
# to encourage the use of a blocking function, especially outside the system
# of rate limit management. But, when debugging, it's terribly useful to have
# a the following function.
try:
    from requests import request as _request
except ImportError:
    def _request(*args, **kwargs):
        raise ImportError("This function requires the `requests` package.")


def debug_blocking_request(app_cred, client_cred, twitter_req):
    """
    Fulfill a request using requests (for humans).

    WARNING: This method is for debugging purposes. It does no rate-limit
        enforcement.

    :param app_cred: the AppCredentials
    :param client_cred: the ClientCredentials
    :param twitter_req: The TwitterRequest

    :return: a requests.Response
    """
    headers = generate_req_headers(twitter_req, app_cred, client_cred)
    return _request(twitter_req.method,
                    twitter_req.url,
                    params=twitter_req.params,
                    headers=headers)
