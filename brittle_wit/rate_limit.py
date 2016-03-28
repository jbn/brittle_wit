import asyncio
import time
from datetime import datetime


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
            now = time.time()
            if now < self._reset_time:
                await asyncio.sleep(self._reset_time - now)
            self._remaining = self._limit

        self._remaining -= 1

    @property
    def is_exhausted(self):
        return self._remaining <= 0

    @property
    def reset_time(self):
        return self._reset_time

    def update(self, resp):
        """
        Update (overwrite) the limits given a Twitter response object.

        Note: From the Twitter Docs:

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
