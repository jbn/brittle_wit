import asyncio
import heapq
import random
import time
from contextlib import contextmanager
from collections import namedtuple, defaultdict
from brittle_wit import TwitterResponse
from brittle_wit.rate_limit import RateLimit
from brittle_wit.oauth import generate_auth_header


AnyCredentials = None


class Requestor:
    """
    A class to enforce rate limit updating after credential use.

   When the caller's code needs a client's credentials, it invokes
   `use_credentials`. Do not assign the credentials to an intermediary
   variable. After use, call `update_limits_from_response(resp)`. If the
   update call never happens, the requestor is in a stale state, and the next
   use_credentials raises an exception.
    """

    def __init__(self, credentials, rate_limit):
        """
        :param credentials: a ClientCredentials object
        :param rate_limit: a shared RateLimit object
        """
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


@contextmanager
def loan_requestor(resource_family, credentials, rate_limit):
    """
    Enforce credential release after acquisition via a context manager.

    :param resource_family: The underlying ResourceFamily object
    :param credentials: The requested credentials
    :param rate_limit: The RateLimit object associated with the requested
        credentials by the resource_family.
    """
    yield Requestor(credentials, rate_limit)
    resource_family.release(credentials)


WaitQueueItem = namedtuple('WaitQueueItem', "wake_time jitter credentials")


class ResourceFamily:
    """
    Note, the wait queue uses random jitter to inject non-determinism. Consider
    the case of a pair of credentials on sitting on the wait queue, both
    sharing the same reset time. Which should move to the head of the ready
    queue after a reset? If it was always the same (e.g. order over the
    credentials), there is arbitrary determinism. Such determinism may
    introduce subtle throttling.

    For example, if the credentials for user A alway moved to the ready queue
    first, a caller requesting AnyCredentials would receive it before user
    B. But, if there was also a caller that always needed user A's credentials
    (i.e. not AnyCredentials), there would be contention between the callers.
    However, had the AnyCredential-is-okay-caller received user B's
    credentials instead, there would be no contention. To minimize the
    unconditional probability of this type of contention, the reinsertion order
    is partially a function of random jitter.
    """
    def __init__(self, wait_queue_sleep_time=1):
        # The wait queue is a heap because I don't need thread locking
        # semantics. And I'm just popping.
        self._ready_queue = []  # Has at least one req remaining
        self._wait_queue = []   # (Wake time, jitter, credentials)
        self._status = {}       # Credentials -> 'ready'|'wait'|'checked_out'
        self._rate_limit = {}   # Credentials -> RateLimit

        self._caller_queue = defaultdict(list)

        self._wait_queue_sleep_time = wait_queue_sleep_time

    def is_managed(self, credentials):
        """
        :return: true if this resource family manages the given credentials
        """
        return credentials in self._status

    def current_status(self, credentials):
        """
        :return: current status associated with the given credentials
        """
        return self._status.get(credentials, 'unmanaged')

    def remove(self, credentials):
        # Remove if not in use.
        # Otherwise, wtf?
        # Prioritize removal (i.e. the user said, STOP).
        pass

    def manage(self, credentials):
        """
        Take management responsibility over the given credentials.

        :param credentials: A ClientCredentials object
        """
        if credentials in self._status:
            msg = "{} already managed by this resource family!"
            raise ValueError(msg.format(credentials))

        self._status[credentials] = 'ready'
        self._rate_limit[credentials] = RateLimit.from_ignorance()
        self._ready_queue.append(credentials)

    def manage_all(self, credentials_iter):
        """
        Take management responsibility for all credentials in the given list
        :param credentials_iter: an iterable of ClientCredentials
        """
        for credentials in credentials_iter:
            self.manage(credentials)
        return self

    @staticmethod
    def _generate_waiting_nonce(credentials):
        return "{}-{}".format(random.random(), credentials)

    def _is_next_caller(self, cred, nonce):
        next_caller = self._caller_queue[cred]
        assert next_caller is not None, "Bad State"
        return next_caller[0] == nonce

    async def acquire(self, credentials_req=AnyCredentials):
        credentials = None

        # The caller_queue enforces FIFO resource acquisition.
        waiting_nonce = self._generate_waiting_nonce(credentials_req)
        self._caller_queue[credentials_req].append(waiting_nonce)

        try:
            while True:
                # I am the next caller waiting.
                # XXX: Best replaced by some automatically managed semaphore.
                if self._is_next_caller(credentials_req, waiting_nonce):

                    # Take the credentials if it is on the ready queue.
                    if credentials_req is AnyCredentials:
                        if self._ready_queue:
                            credentials = self._ready_queue.pop(0)
                            self._status[credentials] = 'checked_out'
                            break
                    elif self._status[credentials_req] == 'ready':
                        i = self._ready_queue.index(credentials_req)
                        credentials = self._ready_queue.pop(i)
                        self._status[credentials] = 'checked_out'
                        break

                # Keep waiting for next caller status or ready credentials.
                await asyncio.sleep(self._wait_queue_sleep_time)
        finally:
            # Remove self (via waiting_nonce) from caller queue
            # If the assertion fails, there is bad code.
            assert self._caller_queue[credentials_req].pop(0) == waiting_nonce

        return loan_requestor(self, credentials, self._rate_limit[credentials])

    def release(self, credentials):
        """
        Releases the loaned credentials, freeing it for subsequent use.

        :param credentials: the ClientCredentials to return
        """
        if credentials not in self._status:
            msg = "{} not known to this family!".format(credentials)
            raise LookupError(msg)

        rate_limit = self._rate_limit[credentials]

        if rate_limit.is_exhausted:
            self._wait_queue.append(WaitQueueItem(rate_limit.reset_time,
                                                  random.random(),
                                                  credentials))
            self._status[credentials] = 'waiting'
        else:
            self._ready_queue.append(credentials)
            self._status[credentials] = 'ready'

    async def maintain_queues(self):
        """
        Move items to ready queue from wait queue after rate limit waiting.
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
            self._ready_queue.append(next_item.credentials)
            self._status[next_item.credentials] = 'ready'


class RequestProcessor:
    FAMILY_NAMES = ['application', 'favorites', 'followers', 'friends',
                    'friendships', 'help', 'lists', 'search',
                    'statuses', 'trends', 'users']

    def __init__(self, app_cred, client_creds, *, excluding_families=None):
        self._app_cred = app_cred
        self._client_creds = {cred.user_id: cred for cred in client_creds}
        self._build_resource_families(excluding_families)

    def _build_resource_families(self, excluding_families):
        self._resource_families = {}

        if excluding_families is None:
            excluding_families = set()

        for family_name in RequestProcessor.FAMILY_NAMES:
            if family_name in excluding_families:
                continue
            resource_family = ResourceFamily()
            resource_family.manage_all(self._client_creds.values())
            self._resource_families[family_name] = resource_family

    async def _get_requestor(self, family_name, uid=AnyCredentials):
        # Having client_cred hanging around is error prone in methods
        # which use the requestor. This is isolating, which is why
        # I like it.
        client_cred = AnyCredentials
        if uid is not AnyCredentials:
            client_cred = self._client_creds[uid]  # LookupError is good.

        family = self._resource_families[family_name]
        return await family.acquire(client_cred)

    async def execute(self, session, twitter_req, *, uid=AnyCredentials):
        # XXX: `with await` is unconventional, therefore confusing.
        with await self._get_requestor(twitter_req.family, uid) as requestor:
            headers = generate_auth_header(twitter_req,
                                           self._app_cred,
                                           await requestor.use_credentials())

            req = session.request(twitter_req.method,
                                  twitter_req.url,
                                  params=twitter_req.params,
                                  headers=headers)
            async with req as resp:
                requestor.update_limits_from_response(resp)
                body = None
                if twitter_req.parse_as == 'json':
                    body = await resp.json()
                else:
                    body = await resp.read()

                return TwitterResponse(twitter_req, resp, body)
