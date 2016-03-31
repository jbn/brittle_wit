class TwitterRequest:
    # This is a static mapping from the request url to the Twitter API
    # documentation URL. `brittle_wit.twitter_request.build_api` populates it,
    # but there is no reason values cannot be overwritten.
    DOC_URLS = {}

    """
    An Immutable (mostly) Twitter Request
    """

    def __init__(self, method, url, family, *, parse_as='json', **params):
        self._method = method.upper()
        self._url = url
        self._family = family.lower()
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

    def _repr_html_(self):
        snippets = ["<table>"]
        snippets.append("<tr><th>Field</th><th>Value</th></tr>")

        fields = ['_method', '_url', '_family', '_parse_as']
        row_s = "<tr><td>{}</td><td>{}</td></tr>"
        for k in fields:
            snippets.append(row_s.format(k[1:], self.__dict__[k]))

        snippets.append("<tr><td>params</td><td><table>")
        snippets.append("<tr><th>Field</th><th>Value</th></tr>")
        for k in self._params:
            snippets.append(row_s.format(k, self._params[k]))

        snippets.append("</table></td></tr>")

        api_url = TwitterRequest.DOC_URLS.get(self._url, None)
        if api_url:
            api_link = "<a href='{}' target='_new'>{}</a>".format(api_url,
                                                                  api_url)
            snippets.append(row_s.format("docs",
                                         api_link.replace(".json", "")))

        snippets.append("</table>")

        return "\n".join(snippets)
