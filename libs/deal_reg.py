import re


def regrex_version(href):
    p = re.compile(".*path=(.*)/")
    m = p.search(href)
    return m.group(1)
