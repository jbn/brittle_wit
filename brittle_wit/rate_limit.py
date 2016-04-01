import asyncio
import time
import random

from datetime import datetime
from collections import defaultdict, namedtuple
from brittle_wit.oauth import ClientCredentials, AppCredentials
import heapq


class RateLimitError(Exception):
    def __init__(self, credentials, twitter_req, resp_headers, resp_body):
        self.credentials = credentials
        self.twitter_req = twitter_req
        self.resp_headers = resp_headers
        self.resp_body = resp_body

    @property
    def is_client_cred(self):
        return type(self.credentials) is ClientCredentials

    @property
    def is_app_cred(self):
        return type(self.credentials) is AppCredentials

    def __str__(self):
        if self.is_client_cred:
            credentials_id = "user_id=" + str(self.credentials.user_id)
        elif self.is_app_cred:
            credentials_id = "app_key=" + str(self.credentials.key)
        else:
            credentials_id = 'cred=' + str(self.credentials)

        msg = "RateLimitError({}, url={}, msg={})"
        return msg.format(credentials_id, self.twitter_req.url, self.resp_body)

    def __repr__(self):
        return self.__str__()


class RateLimit:
    """
    Captures and enforces rate limiting.

    See: https://dev.twitter.com/rest/public/rate-limiting
    """

    @staticmethod
    def from_ignorance():
        """
        Create a RateLimit object assuming one request allowed and remains.

        Given the way update works, this is a good initialization pattern.
        However, to make sure it is clear to the caller, ignorance is part of
        the name.
        """
        return RateLimit(1, 1, int(time.time() + 15*60))  # 15 minutes from now

    @staticmethod
    def from_response(resp):
        """
        Create a RateLimit object from a twitter response.
        """
        return RateLimit.from_ignorance().update(resp)

    @staticmethod
    def from_initial_limit(initial_limit):
        """
        Create a RateLimit object from a limit with all requests remaining.
        """
        return RateLimit(initial_limit,
                         initial_limit,             # All remaining
                         int(time.time() + 15*60))  # 15 minutes from now

    def __init__(self, limit, remaining, reset_time):
        self._limit = limit
        self._remaining = remaining
        self._reset_time = reset_time

    async def comply(self):
        """
        Ensure request availability before allowing caller to proceed.

        If there are zero requests remaining, comply uses sleep to wake up
        after the reset time. Call this method immediately preceding any
        request. Doing so allows for  maximum throughput (i.e. minimum wasted
        sleep time.)

        This method decrements the requests remaining prior to actually using a
        request. This gives strong guarantees on rate limit compliance. If the
        caller then uses the request then -- for some reason -- fails to call
        update, the RateLimit object remains correct. If the caller does call
        update, remaining requests comports to whatever is in the response
        object.
        """
        if self.is_exhausted:
            now = time.time()  # Is time.time() blocking?
            if now < self._reset_time:
                await asyncio.sleep(self._reset_time - now)
            self._remaining = self._limit

        self._remaining -= 1

    @property
    def is_exhausted(self):
        return self._remaining <= 0

    @property
    def is_pristine(self):
        return self._remaining == self._limit

    @property
    def reset_time(self):
        return self._reset_time

    def mark_exhausted(self, resp):
        """
        Ensure that the credentials are rate-limited following a bad response.

        From the Twitter Docs:

        > Lastly, there may be times in which the rate limit values that
        we return are inconsistent, or cases where no headers are returned at
        all.

        If there was an rate limit response, then there are definitely 0
        requests remaining. If the reset time is not present, then set it to
        15 minutes from now.

        :param resp:
        :return:
        """
        self._limit = int(resp.headers.get('X-RATE-LIMIT-LIMIT', self._limit))
        self._remaining = 0
        self._reset_time = int(resp.headers.get('X-RATE-LIMIT-RESET',
                                                time.time() + 60*15))

    def update(self, resp):
        """
        Update (overwrite) the limits given a Twitter response object.

        From the Twitter Docs:

        > Lastly, there may be times in which the rate limit values that
        we return are inconsistent, or cases where no headers are returned at
        all.

        To cope with this, I skip updates to missing header information.
        """
        self._limit = int(resp.headers.get('X-RATE-LIMIT-LIMIT', self._limit))
        self._remaining = int(resp.headers.get('X-RATE-LIMIT-REMAINING',
                                               self._remaining))
        self._reset_time = int(resp.headers.get('X-RATE-LIMIT-RESET',
                                                self._reset_time))

        return self

    def __str__(self):
        msg = "RateLimit(limit={}, remaining={}, reset_time={})"
        time_s = datetime.fromtimestamp(self._reset_time).strftime("%H:%M:%S")

        return msg.format(self._limit, self._remaining, time_s)

    def __repr__(self):
        return self.__str__()


class CredentialContext:
    """
    A class to enforce rate limit updating after credential use.

    When the caller's code needs a client's credentials, it invokes
    `use_credentials`. Do not assign the credentials to an intermediary
    variable. After use, call `update_limits_from_response(resp)`. If the
    update call never happens, the manager is in a stale state, and the next
    use_credentials raises an exception.
    """

    def __init__(self, rate_limit_enforcer, credentials, rate_limit):
        """
        :param credentials: a ClientCredentials object
        :param rate_limit: a shared RateLimit object
        """
        self._rate_limit_enforcer = rate_limit_enforcer
        self._credentials = credentials
        self._rate_limit = rate_limit

        self._stale = False

    async def use_credentials(self):
        if self._stale:
            raise RuntimeError("Requestor Stale: call update() first!")

        self._stale = True
        await self._rate_limit.comply()

        return self._credentials

    def update_limits_from_response(self, resp):
        """
        :param resp: an object whose header field contains rate limit
            information for the last API call.
        """
        self._rate_limit.update(resp)
        self._stale = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._rate_limit_enforcer.release(self._credentials)


WaitQueueItem = namedtuple('WaitQueueItem', "wake_time credentials")


class RateLimitEnforcer:
    """
    Enforce a rate limit for an endpoint.

    Rate limits apply to specific endpoints. Twitter defines resource
    families, but the remaining requests change independently. Therefore,
    credential management occurs at the endpoint level.

    If an application serves thousands of Twitter users, maintaining the
    rate limits per-endpoint, per-user is expensive. There could literally
    be millions of RateLimit objects in your application. Abiding by rate
    limiting is necessary. But, applications with thousands of users
    probably don't have thousands of concurrent users, requesting every
    method during every window. This suggests sparse data structure.
    """
    def __init__(self, wait_queue_sleep_time=1, initial_limit=15):
        # The wait queue is a simple heap. The standard libraries queue
        # family of classes all use mutex locking. As Brittle Wit uses
        # an async-based, single-threaded execution pattern, mutex
        # locking represents wasted CPU time.
        self._wait_queue = []   # (Wake time, jitter, credentials)

        # The _status field reports either 'ready', 'waiting', or
        # 'checked_out' for a given set of credentials. Ready means
        # the credentials are ready for immediate checkout. Most of
        # the time, client credentials are in the 'ready' state.
        # Therefore, rather than storing the string 'status', it is
        # the default. When a set of credentials are ready, delete
        # it from the status dictionary.
        self._status = defaultdict(lambda: 'ready')

        # The _rate_limit field tracks the current rate limits for
        # a given set of credentials. If the RateLimit is pristine --
        # that is, the number of requests remaining is equal to the
        # number of requests allowed -- delete the credentials from
        # the _rate_limit dict. This should be the majority, again
        # allowing for a sparse data structure.
        def _rate_limit_factory():
            return RateLimit.from_initial_limit(initial_limit)
        self._rate_limit = defaultdict(_rate_limit_factory)

        # The caller queue enforces an FIFO ordering over requests
        # for a specific set of credentials. For example, caller A
        # requests credentials for user_id=3; then, just afterwards,
        # caller B does the same. Caller A should always receive the
        # credentials first. Caller B then waits for A to return the
        # credentials. When no one is waiting for a particular set of
        # credentials, delete the wait list.
        self._caller_queue = defaultdict(list)

        self._wait_queue_sleep_time = wait_queue_sleep_time

    def current_status(self, credentials):
        """
        :return: current status associated with the given credentials
        """
        return self._status[credentials]

    @staticmethod
    def _generate_waiting_nonce(credentials):
        # A caller doesn't have any specific identifier. Instead,
        # I'll generate one that *should* be unique.
        # XXX: does time() block?
        return "{}-{}-{}".format(time.time(), random.random(), credentials)

    def _is_next_caller(self, credentials, nonce):
        next_caller = self._caller_queue.get(credentials)

        return next_caller[0] == nonce if next_caller else True

    async def acquire(self, credentials):
        if self._status[credentials] == 'ready':
            # If the credentials are immediately ready, check them out.
            self._status[credentials] = 'checked_out'
        else:
            # The credentials are either checked out or in the wait queue.
            # This requires FIFO enforcement.
            waiting_nonce = self._generate_waiting_nonce(credentials)
            self._caller_queue[credentials].append(waiting_nonce)

            try:
                while True:
                    # I am the next caller waiting.
                    if self._is_next_caller(credentials, waiting_nonce):

                        # Take the credentials once on the ready queue.
                        if self._status[credentials] == 'ready':
                            self._status[credentials] = 'checked_out'
                            break

                    # Keep waiting for next caller and ready statuses.
                    await asyncio.sleep(self._wait_queue_sleep_time)
            finally:
                # Remove this request (via waiting_nonce) from caller queue
                # The following assertion should never fail.
                assert self._caller_queue[credentials].pop(0) == waiting_nonce

                # The caller queue is empty. Clean it up.
                if not self._caller_queue[credentials]:
                    del self._caller_queue[credentials]

        return CredentialContext(self,
                                 credentials,
                                 self._rate_limit[credentials])

    def release(self, credentials):
        """
        Releases the loaned credentials, freeing it for subsequent use.

        :param credentials: the ClientCredentials to return
        """
        rate_limit = self._rate_limit[credentials]

        if rate_limit.is_exhausted:
            self._wait_queue.append(WaitQueueItem(rate_limit.reset_time,
                                                  credentials))
            self._status[credentials] = 'waiting'
        else:
            if credentials in self._status:
                del self._status[credentials]  # i.e. ready

            if rate_limit.is_pristine:
                del self._rate_limit[credentials]  # i.e. pristine

    async def maintain_queues(self, slumber_time=15*60):
        """
        Move items to ready status from wait queue after rate limit waiting.

        :param slumber_time: the time to sleep if there is nothing to wait for
        """
        while True:
            # Peek at the next item. If it's still in the future, sleep
            # _wait_queue_sleep_time seconds then restart the loop. In between
            # now and then, an item with a higher priority may appear on the
            # queue.
            now = time.time()
            if not self._wait_queue or now < self._wait_queue[0].wake_time:
                await asyncio.sleep(self._wait_queue_sleep_time)
                continue

            # The next_item is ready for popping off the queue
            next_item = heapq.heappop(self._wait_queue)
            if next_item.credentials in self._status:
                del self._status[next_item.credentials]

            # If all the rate limits are pristine, sleep a full 15 minutes.
            # It is possible that maintenance needs to run in that interval.
            # For example, if:
            #
            # - the application restarted, resulting no initially known
            #   rate limits
            # - a request issued with some credentials was rate-limited
            #   by the prior process
            # - the rate-limit properly expires one minute from now
            #
            # then, this is incorrect waiting behavior. However, this is
            # an exceptional circumstance. Brittle Wit is designed for
            # long-running processes. It's not worth the additional complexity.
            #
            # Note: an empty _rate_limit dict implies no callers in-queue.
            if self._rate_limit:
                await asyncio.sleep(slumber_time)

