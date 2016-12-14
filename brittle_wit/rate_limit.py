import asyncio
import time

from datetime import datetime
from collections import defaultdict


FIFTEEN_MIN = 15 * 60 + 2 # Add two seconds.

class RateLimit:
    """
    Captures and enforces rate limiting.

    See: https://dev.twitter.com/rest/public/rate-limiting
    """
    CLIENT_LIMITS = defaultdict(lambda: FIFTEEN_MIN)
    APP_LIMITS = defaultdict(lambda: FIFTEEN_MIN)

    @staticmethod
    def from_ignorance():
        """
        Create a RateLimit object assuming one request allowed and remains.

        Given the way update works, this is a good initialization pattern.
        However, to make sure it is clear to the caller, ignorance is part of
        the name.
        """
        return RateLimit(1, 1, int(time.time() + FIFTEEN_MIN))  # 15 minutes from now

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
                         int(time.time() + FIFTEEN_MIN))  # 15 minutes from now

    __slots__ = '_limit', '_remaining', '_reset_time'

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
                # Time sync issue so always add 5 seconds?
                await asyncio.sleep(self._reset_time - now + 5)
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


class TimingRateLimiter:
    """
    Enforces a maximum number of operations per second.

    This class does not enforce Twitter's API rate limits. Instead, it's a soft
    limiter for social interactions. For example, if you are writing something
    ike a feed consolidator bot, you would not want to retweet more than an
    *average* of one status every hour. To do so, create a TimingRateLimiter
    with the minimum number of seconds between each operation.  Immediately
    prior to each possible operation, call bool(timing_rate_limiter). If it
    returns False, do not take the action. If it returns True, take the action.
    Implicitly, if it returns True, it assumes you did take the action.
    """
    def __init__(self, min_secs_per_op):
        """
        :param min_secs_per_op: the minimum average number of seconds which
            must pass between each operation
        """
        self._n = 0
        self._min_secs_per_op = min_secs_per_op
        self._start_time = time.time()

    @property
    def is_rate_limited(self):
        rate = (time.time() - self._start_time) / self._n
        return rate < self._min_secs_per_op

    def can_proceed(self):
        """
        :return: True if the operation is not limited.
        """
        if self._n == 0 or not self.is_rate_limited:
            self._n += 1
            return True
        else:
            return False
