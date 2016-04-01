from datetime import datetime


def parse_date(s):
    return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
