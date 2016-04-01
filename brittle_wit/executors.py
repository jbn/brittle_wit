from collections import defaultdict
from brittle_wit import TwitterResponse
from brittle_wit.rate_limit import RateLimitEnforcer
from brittle_wit import oauth


AnyCredentials = None


def twitter_req_to_http_req(session, app_cred, client_cred, twitter_req):
    headers = oauth.generate_req_headers(twitter_req, app_cred, client_cred)
    return session.request(twitter_req.method,
                           twitter_req.url,
                           params=twitter_req.params,
                           headers=headers)


class AnyCredentialsQueue:
    """
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

    The AnyCredentialsQueue maintains a circular FIFO queue for each set of
    credentials. When a client asks for AnyCredentials, the queue takes the
    pops a token off the top. When it asks again, it pushes that initial item
    to the end of the queue, and pops the head again.

    This is far from perfect. For example, this could select a token that is
    currently rate-limited even though non-limited ones remain. But, it's
    cheap, and does well, probabilistically. Additionally, I believe this
    should perform better as the number of managed users rises. (I'll think
    more about it; then, pen an arXiv article.)
    """
    def __init__(self, credentials_iter=None):
        self._queue = []
        self._managed = set()
        if credentials_iter:
            for credentials in reversed(credentials_iter):
                self.add_credentials(credentials)

    def add_credentials(self, credentials):
        """
        Add a new set of credentials to the front of the queue.
        """
        assert credentials not in self._managed
        self._queue.insert(0, credentials)
        self._managed.add(credentials)

    def remove_credentials(self, credentials):
        """
        Remove a set of credentials from the queue.
        """
        self._queue.remove(credentials)
        self._managed.remove(credentials)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Get the next item on the queue.
        """
        credentials = self._queue.pop(0)
        self._queue.append(credentials)

        return credentials


class RequestProcessor:
    # What about app credentials?

    def __init__(self, app_cred):
        self._app_cred = app_cred
        self._client_creds = {}
        self._enforcers = defaultdict(lambda: RateLimitEnforcer())
        self._any_queue = iter(AnyCredentialsQueue())

    def add_enforcer(self, service, enforcer):
        self._enforcers[service] = enforcer

    def delete_enforcer(self):
        pass # Close all process loops?

    def add_credentials(self, credentials):
        self._client_creds[credentials.user_id] = credentials
        self._any_queue.add_credentials(credentials)

    def remove_credentials(self, credentials):
        pass

    def swap_credentials(self, user_id, new_credentials):
        pass

    def _get_credentials(self, user_id):
        # Having client_cred hanging around is error prone in methods
        # which use the requestor. This is isolating, which is why
        # I like it.
        #client_cred = AnyCredentials
        #if uid is not AnyCredentials:
        return self._client_creds[uid]  # LookupError is good?

    async def _get_ctx(self, service, credentials):
        if credentials is AnyCredentials:
            credentials = next(self._any_queue)

        return await self._enforcers[service].acquire(credentials)

    async def execute(self, session, twitter_req, credentials=AnyCredentials):
        # XXX: `with await` is unconventional, therefore confusing.
        # DO NOT USE CREDENTIALS raw

        with await self._get_ctx(twitter_req.service, credentials) as ctx:
            req = twitter_req_to_http_req(session,
                                          self._app_cred,
                                          await ctx.use_credentials(),
                                          twitter_req)
            async with req as resp:
                ctx.update_limits_from_response(resp)
                # check for rate limiting.
                # Raise exception.
                body = None
                if twitter_req.parse_as == 'json':
                    body = await resp.json()
                else:
                    body = await resp.read()

                return TwitterResponse(twitter_req, resp, body)


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
    headers = oauth.generate_req_headers(twitter_req, app_cred, client_cred)
    return _request(twitter_req.method,
                    twitter_req.url,
                    params=twitter_req.params,
                    headers=headers)
