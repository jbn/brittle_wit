import asyncio
import aiohttp
import async_timeout
import time
import logging


from brittle_wit_core import (generate_req_headers,
                              TwitterResponse,
                              TwitterError,
                              BrittleWitError,
                              WrappedException)
from brittle_wit.helpers import retrying
from brittle_wit.rate_limit import RateLimit, FIFTEEN_MINUTES
from brittle_wit.ticketing import TicketMaster


LOGGER = logging.getLogger('brittle_wit')

ANY_CREDENTIALS = None


def twitter_req_to_http_req(session, app_cred, client_cred, twitter_req, **overrides):
    """
    Convert a TwitterRequest into a aiohttp request.

    :param session: an aiohttp.ClientSession object
    :param app_cred: an `AppCredentials` object
    :param client_cred: an `ClientCredentials` object
    :param twitter_req: an `TwitterRequest` object
    :param overrides: override keys for the request

    :return: the aiohttp request
    """
    headers = generate_req_headers(twitter_req, app_cred, client_cred)
    payload_k = 'data' if twitter_req.method == 'POST' else 'params'
    kwargs = {payload_k: twitter_req.params,
              'headers': headers}
    kwargs.update(overrides)

    return session.request(twitter_req.method, twitter_req.url, **kwargs)


async def execute_req(client_cred, twitter_req, http_req, rate_limit):
    """
    Execute a request with no exception handling.

    :param client_cred: the client_cred used to build the http_req
    :param twitter_req: the original TwitterRequest
    :param http_req: the HttpRequest with encoded authentication information
    :param rate_limit: the RateLimit object associated with the endpoint and
        client_cred
    :return: a TwitterResponse
    """

    # Send request over the wire.
    async with http_req as resp:

        # Update rate limits ASAP. Note: The prior call to comply
        # decremented the rate limits already. If the context manager
        # threw an exception on entry, it is still in compliance.
        rate_limit.update(resp)

        # An error occurred.
        if resp.status != 200:
            raise TwitterError(client_cred, twitter_req, resp,
                               await resp.text())

        # The status code indicates a good response.
        # Choose appropriate parsing strategy.
        if twitter_req.parse_as == 'json':
            body = await resp.json()
        else:
            body = await resp.text()

        return TwitterResponse(twitter_req, resp, body)


class ClientRequestProcessor:
    """
    The ClientRequestProcessor manages rate limits while executing requests.

    When the caller issues a request for execution, the request processor
    enforces rate limitations. Such enforcement occurs in the context of the
    given credentials and for a given service. If multiple callers request
    execution at the same time (for a given set of credentials and service),
    the requests execute FIFO.

    There should only be one ClientRequestProcessor per set of credentials!

    Perioditically call ``#cleanup()``. When `#is_removable()` is true, there
    is no useful state information in the processor, and you can let Python
    garbage collect the object. This allows for stochastic reclaimation of
    memory.
    """

    def __init__(self, client_cred):
        """
        :param client_cred: the ClientCredentials to manage
        """
        self._client_cred = client_cred
        self._ticket_master = TicketMaster()
        self._rate_limits = {}

    @property
    def user_id(self):
        return self._client_cred.user_id

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

    def _rate_limit_for(self, service):
        """
        Get existing or create new RateLimit for the given service.

        Only this object should manage the RateLimits, hence a private method.

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
        if not self._rate_limits:
            return

        now = now or time.time()

        remove_ks = []
        for service, rate_limit in self._rate_limits.items():
            # If the reset time is in the past, remove it.
            if rate_limit.reset_time < now:
                remove_ks.append(service)

        for k in remove_ks:
            del self._rate_limits[k]

    async def _execute(self, session, app_cred, twitter_req, timeout=None):
        """
        :param session: an aiohttp.ClientSession object
        :param app_cred: an `AppCredentials` object
        :param twitter_req: an `TwitterRequest` object
        :param timeout: maximium time to wait for a response EVEN IF TWITTER
            IS STILL SENDING INFORMATION. (default None for no timeout)
        """
        service = twitter_req.service

        # This thows after some amount of time, even if it's still reading!
        async with async_timeout.timeout(timeout):

            async with self._ticket_master.take_ticket(service):
                # The caller is now in charge of this service.
                rate_limit = self._rate_limit_for(service)

                # Block request execution until not rate limited.
                await rate_limit.comply()

                http_req = twitter_req_to_http_req(session,
                                                   app_cred,
                                                   self._client_cred,
                                                   twitter_req)

                # This coroutine will raise an exception for non-200 statuses.
                return await execute_req(self._client_cred,
                                         twitter_req,
                                         http_req,
                                         rate_limit)

    async def execute(self, session, app_cred, twitter_req, timeout=120,
                      n_retries=5, sleep_time=60):
        def bound_execute():
            return self._execute(session, app_cred, twitter_req, timeout)
        return await retrying(bound_execute, n_retries, sleep_time=sleep_time)


class ManagedClientRequestProcessors:
    """
    Manages client request processors

    Any Credential Management
    -------------------------

    For many tasks, you don't need specific credentials, you just need some
    credentials. For example, if you and your social network analyst friends
    wanted to analyze the followers of Tech Crunch, you need to collect all
    the user objects. Given that there are millions of them that could take
    time. But, if you already have the user id's you can partition the
    collection and run it in parallel. The specific credentials don't matter.
    (Well, ignoring the case of a follower blocking that person's access.)

    Finding an unused set of credentials is non-trivial. Managing a ready-queue
    for each service is expensive in terms of space when there are many users.
    As an alternative, I rely on probability. (That is, until I think
    more and find a better solution.)

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
        self._credentials, self._any_cred_queue = {}, []

    def is_managed(self, cred):
        return cred in self._credentials

    def add(self, cred, any_cred_eligible=True):
        """
        Create and manage a request processor for the given credentials.

        If you add already added credentials, it raises a runtime exception.

        :param cred: the client's credentials
        :param any_cred_eligible: if True, then an app may use this
            client's credentials promiscuously; otherwise, only the
            client can use it.
        """
        # XXX: TODO: What? Why? I'm sure I did this for a reason but...
        if self.is_managed(cred):
            raise RuntimeError("Credential already managed.")

        client_req_processor = ClientRequestProcessor(cred)
        self._credentials[cred] = client_req_processor

        if any_cred_eligible:
            self._any_cred_queue.insert(0, cred)

    def add_all(self, bulk_credentials, any_cred_eligible=True):
        """
        Add and manage client credentials in bulk.
        """
        for cred in bulk_credentials:
            self.add(cred, any_cred_eligible=any_cred_eligible)

    def remove(self, cred):
        """
        Stop managing the processor associated with the given credentials
        """
        del self._credentials[cred]
        try:
            self._any_cred_queue.remove(cred)
        except ValueError:
            pass  # Was added with any_cred_eligible=False

    def __getitem__(self, cred):
        """
        Get the processor associated with the given credentials.

        Client code should not store a reference to the processor. You
        should call this method every time to avoid the possibility of
        multiple processors for the same credentials. (The ``maintain``
        method may deallocate some processors if not recently used.)

        :param cred: the client's credentials, or ``ANY_CREDENTIALS`` to
            make promiscuous requests.
        :return: the client's processor or None if a ``ANY_CREDENTIALS``
            request was made with no eligible processors
        """
        if cred is ANY_CREDENTIALS:
            if self._any_cred_queue:
                credentials = self._any_cred_queue.pop(0)
                self._any_cred_queue.append(credentials)
                return self[credentials]
            else:
                return None
        else:
            managed = self._credentials.get(cred)

            if managed is not None:
                return managed
            else:
                self.add(cred)
                return self._credentials[cred]

    async def maintain(self, cull_interval=FIFTEEN_MINUTES):
        """
        Maintains the request processors, forever.

        Mostly, this means cleaning up request processors, allowing GC.

        :param cull_interval: how frequently, in seconds, maintain
            should run.
        """
        while True:
            await asyncio.sleep(cull_interval)

            try:
                self._maintain()
            except KeyboardInterrupt:
                raise
            except asyncio.CancelledError:
                break
            except Exception as e:
                LOGGER.error("Error %s during maintain()", e)

    def _maintain(self):
        now = time.time()

        # Cleanup all the request processors and identify those which
        # can be removed.
        removal_keys = []
        for k, req_processor in self._credentials.items():
            req_processor.cleanup(now)  # Remove disused rate limits

            if req_processor.is_removable():
                removal_keys.append(k)

        # Remove all those processors not in use or rate limited.
        for k in removal_keys:
            self.remove(k)


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
    # I don't want to require requests as a dependency. And, I really don't
    # want to encourage the use of a blocking function, especially outside
    # the system of rate limit management. But, when debugging, it's terribly
    # useful to have a the following function.
    from requests import request as _request

    headers = generate_req_headers(twitter_req, app_cred, client_cred)

    return _request(twitter_req.method,
                    twitter_req.url,
                    params=twitter_req.params,
                    headers=headers)
