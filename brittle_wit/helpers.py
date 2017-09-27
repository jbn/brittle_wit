import asyncio
import logging
from collections import OrderedDict
from datetime import datetime
from brittle_wit_core import TwitterRequest, WrappedException


LOGGER = logging.getLogger('brittle_wit')


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
            LOGGER.error("Error %s", e)
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


def running_task_names():
    """
    :return: list of all ``qual_name``s for running tasks.
    """
    tasks = asyncio.Task.all_tasks()
    return [t._coro.__qualname__ for t in tasks if not t.done()]


class CircularQueue:
    """
    A Circular Queue with Fast Membership Testing.
    """

    def __init__(self):
        self._queue, self._members = [], set()

    def __contains__(self, item):
        return item in self._members

    def __bool__(self):
        return bool(self._queue)

    def __delitem__(self, item):
        self._members.remove(item)
        self._queue.remove(item)

    def add(self, item):
        """
        Adds an item to the FIRST slot in the queue.

        :raises: a ValueError if the item is already enqueued.
        :param item: the item to add.
        """
        if item in self._members:
            raise ValueError("Item {} already in queue".format(item))

        self._queue.insert(0, item)
        self._members.add(item)

    def pop_and_rotate(self):
        """
        :return: the next item on the queue while maintaining
            the circular buffer.
        """
        if not self._queue:
            return None

        item = self._queue.pop(0)
        self._queue.append(item)
        return item
