from collections import namedtuple
from aiohttp.errors import ClientOSError, TimeoutError, ContentEncodingError
import asyncio

RETRYABLE_CODES = {500,  # INTERNAL SERVER ERROR
                   502,  # BAD GATEWAY
                   503,  # SERVICE UNAVAILABLE
                   504}  # GATEWAY TIMEOUT


RETRYABLE_EXCEPTIONS = {ContentEncodingError, ClientOSError, TimeoutError, 
                        asyncio.TimeoutError}


class TwitterRequest:
    """
    An Immutable (mostly) Twitter Request
    """

    # This is a static mapping from the request url to the Twitter API
    # documentation URL. `brittle_wit.twitter_request.build_api` populates it,
    # but there is no reason values cannot be overwritten.
    DOC_URLS = {}

    __slots__ = ('_method', '_url', '_family',
                 '_service', '_parse_as', '_params')

    def __init__(self, method, url, family, service,
                 *, parse_as='json', **params):
        self._method = method
        self._url = url
        self._family = family
        self._service = service.upper()
        self._parse_as = parse_as
        self._params = params

    @property
    def method(self):
        return self._method

    @property
    def url(self):
        return self._url

    @property
    def family(self):
        return self._family

    @property
    def service(self):
        return self._service

    @property
    def parse_as(self):
        return self._parse_as

    @parse_as.setter
    def parse_as(self, parse_format):
        self._parse_as = parse_format

    @property
    def params(self):
        return self._params

    def __str__(self):
        return "TwitterRequest(url={})".format(self._url)

    def clone_and_merge(self, updated_params):
        return TwitterRequest(self._method, self._url, self._family,
                              self._service,
                              parse_as=self._parse_as,
                              **{**self._params, **updated_params})


class Cursor:
    def __init__(self, twitter_req):
        self._req = twitter_req
        self._cursor = -1
        self._update_called = True

    def update(self, resp):
        next_cursor = resp.body.get('next_cursor')

        if next_cursor is None or next_cursor == 0:
            self._req = None
        else:
            self._cursor = next_cursor
            self._req = self._req.clone_and_merge({'cursor': next_cursor})

        self._update_called = True

    def __iter__(self):
        return self

    def __next__(self):
        if not self._update_called:
            raise RuntimeError("Must call update() between __next__s")

        if self._req is None:
            raise StopIteration

        self._update_called = False
        return self._req


TwitterResponse = namedtuple('TwitterResponse', 'req resp body')


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
        fmt = "WrappedException({})"
        return fmt.format(repr(self._underlying_exception))

    def __repr__(self):
        return self.__str__()
