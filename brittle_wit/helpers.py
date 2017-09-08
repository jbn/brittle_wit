import asyncio
from collections import OrderedDict
from datetime import datetime
from brittle_wit_core import TwitterRequest, WrappedException


def parse_datetime(s):
    """
    Parse a date string sent in a tweet.
    :param s: a Twitter-returned date-time string
    :return: a datetime object
    """
    return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")


def linear_backoff(failure_num, sleep_time):
    return failure_num * sleep_time


def expon_backoff(failure_num, sleep_time):
    return 2**(failure_num - 1) * sleep_time


async def retrying(make_coro, n_tries, strategy=linear_backoff, sleep_time=60):
    for attempt in range(1, n_tries + 1):
        try:
            return await make_coro()
        except Exception as e:
            wrapped = WrappedException.wrap_if_nessessary(e)
            if not wrapped.is_retryable or attempt == n_tries:
                raise wrapped
            await asyncio.sleep(strategy(attempt, sleep_time))


def grouping(items, n):
    """
    Group items into sequential chunks.

    Each chunk has a length of n. However, the last chunk is somewhere
    between 1 and n.

    :param items: the iterable of items
    :param n: the chunk size
    """
    group = []
    for item in items:
        if len(group) == n:
            yield group
            group = []
        group.append(item)

    if group:
        yield group


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


def _twitter_request_html_repr(self):
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


def monkey_patch_ipython_disp():
    TwitterRequest._repr_html_ = _twitter_request_html_repr
