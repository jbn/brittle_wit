"""
Import this module to monkey patch various classes for display in an IPython
HTML notebook.
"""
from collections import OrderedDict, Counter, defaultdict
import asyncio
from asyncio.selector_events import BaseSelectorEventLoop
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


def _make_ol(items):
    if not items:
        return ""

    return "<ul>\n\t<li>" + "</li>\n\t<li>".join(items) + "\t</li>\n</ul>"


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


def event_loop_html_repr(self):
    """
    Note: This only works if you run_forever() otherwise tasks get cleared.
    """
    d = OrderedDict()

    d['Type'] = type(self).__name__
    d['Is Running'] = self.is_running()
    d['Is Closed'] = self.is_closed()
    d['Is Debug'] = self.get_debug()
    d['Time'] = self.time()
    d['Current Task'] = asyncio.Task.current_task(self)

    tasks = asyncio.Task.all_tasks(self)
    pending, n_done, errored, coro_to_err = [], 0, [], defaultdict(set)

    for t in tasks:
        name = t._coro.cr_code.co_name
        if t.done():
            err = t.exception()
            if err:
                errored.append((name, err))
                coro_to_err[name].add(repr(err))
            n_done += 1
        else:
            pending.append(name)

    d['N(Tasks)'] = len(tasks)
    d['N(Done)'] = n_done
    d['N(Pending)'] = len(pending)
    if pending:
        d['Pending'] = _make_table(Counter(pending), ("Name", "N"),
                                  sort=True)

    d['N(Err)'] = len(errored)
    if errored:
        d['Errors'] = _make_table(coro_to_err,
                                 ("Coroutine", "Exceptions"),
                                 sort=True)

    return _make_table(d, ('Name', 'Value'))


BaseSelectorEventLoop._repr_html_ = event_loop_html_repr
TwitterRequest._repr_html_ = twitter_request_html_repr
