

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

