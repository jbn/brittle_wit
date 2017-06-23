"""
Import this module to monkey patch twitter requests for display in an
IPython/Jupyter notebook.
"""
from collections import OrderedDict
from brittle_wit import TwitterRequest


def _make_table(d, header_labels=None, sort=False):
    snippets = ["<table>"]

    if header_labels:
        assert len(header_labels) == 2
        snippets.append("<tr><th>{}</th><th>{}</th>".format(*header_labels))

    row_str = "<tr><td>{}</td><td>{}</td>"

    ks = sorted(d) if sort else d
    for k in ks:
        snippets.append(row_str.format(k, d[k]))

    snippets.append("</table>")

    return "\n".join(snippets)


def twitter_request_html_repr(self):
    d = OrderedDict()

    for k in ['_method', '_url', '_family', '_service', '_parse_as']:
        d[k[1:]] = getattr(self, k)

    if self._params:
        d['Params'] = _make_table(self._params, ('Key', 'Value'), True)

    api_url = TwitterRequest.DOC_URLS.get(self._url, None)
    if api_url:
        api_link = "<a href='{}' target='_new'>{}</a>".format(api_url, api_url)
        d["docs"] = api_link.replace(".json", "")

    return _make_table(d, ("Name", "Value"))


TwitterRequest._repr_html_ = twitter_request_html_repr
