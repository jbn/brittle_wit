from aiohttp.errors import ClientOSError, TimeoutError


RETRYABLE_CODES = {500,  # INTERNAL SERVER ERROR
                   502,  # BAD GATEWAY
                   503,  # SERVICE UNAVAILABLE
                   504}  # GATEWAY TIMEOUT


RETRYABLE_EXCEPTIONS = {ClientOSError, TimeoutError}


class BrittleWitError(Exception):
    @property
    def is_retryable(self):
        return False


class TwitterError(BrittleWitError):
    def __init__(self, credentials, twitter_req, http_resp, message):
        self._credentials = credentials
        self._twitter_req = twitter_req
        self._http_resp = http_resp
        self._status_code = http_resp.status
        self._message = message

    @property
    def status_code(self):
        return self._status_code

    @property
    def twitter_req(self):
        return self._twitter_req

    @property
    def is_retryable(self):
        return self._status_code in RETRYABLE_CODES

    @property
    def message(self):
        return self._message

    @property
    def credentials(self):
        return self._credentials

    def __str__(self):
        return "TwitterError(code={}, msg={})".format(self._status_code,
                                                      self._message)

    def __repr__(self):
        return self.__str__()


class WrappedException(BrittleWitError):
    def __init__(self, underlying_exception):
        self._underlying_exception = underlying_exception

    @property
    def underlying_exception(self):
        return self._underlying_exception

    @property
    def is_retryable(self):
        return type(self._underlying_exception) in RETRYABLE_EXCEPTIONS

    def __str__(self):
        fmt = "WrappedException({}, {})"
        return fmt.format(type(self._underlying_exception),
                          self._underlying_exception)

    def __repr__(self):
        return self.__str__()
