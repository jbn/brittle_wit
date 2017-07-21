from datetime import datetime


def parse_date(s):
    return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")


class WrappingHandler:

    def __init__(self, underlying_func):
        self._underlying_func = underlying_func

    def send(self, msg):
        return self._underlying_func(msg)


def grouping(items, n):
    group = []
    for item in items:
        if len(group) == n:
            yield group
            group = []
        group.append(item)

    if group:
        yield group
