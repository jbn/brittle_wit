from datetime import datetime
from functools import wraps


def parse_date(s):
    return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")


class WrappingHandler:
    def __init__(self, underlying_func):
        self._underlying_func = underlying_func

    def send(self, msg):
        return self._underlying_func(msg)
