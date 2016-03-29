class TwitterRequest:
    """
    An Immutable (mostly) Twitter Request
    """

    def __init__(self, method, url, family, *,
                 parse_as='json', supports_cursor=False, **params):
        self._method = method.upper()
        self._url = url
        self._family = family.lower()
        self._parse_as = parse_as
        self._supports_cursor = supports_cursor
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
    def supports_cursor(self):
        return self._supports_cursor

    @property
    def params(self):
        return self._params

    def __str__(self):
        return "TwitterRequest(url={})".format(self._url)

    def _repr_html_(self):
        snippets = ["<table>"]
        snippets.append("<tr><th>Field</th><th>Value</th></tr>")

        fields = ['_method', '_url', '_family', '_parse_as',
                  '_supports_cursor']
        row_s = "<tr><td>{}</td><td>{}</td></tr>"
        for k in fields:
            snippets.append(row_s.format(k[1:], self.__dict__[k]))

        snippets.append("<tr><td>params</td><td><table>")
        snippets.append("<tr><th>Field</th><th>Value</th></tr>")
        for k in self._params:
            snippets.append(row_s.format(k, self._params[k]))

        snippets.append("</table></td></tr>")

        api_url = ("https://dev.twitter.com/rest/reference/" +
                   self._method.lower() + "/" +
                   self._url.split("1.1/")[-1])
        api_link = "<a href='{}' target='_new'>{}</a>".format(api_url, api_url)
        snippets.append(row_s.format("docs", api_link.replace(".json", "")))

        snippets.append("</table>")

        return "\n".join(snippets)
