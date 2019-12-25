import re


def regrex_version(href):
    p = re.compile(".*path=(.*)/")
    m = p.search(href)
    return m.group(1)


def reg_dir(dir):
    try:
        m = re.compile("(\d*)\..*")
        p = m.search(dir)
        return p.group(1)
    except AttributeError:
        pass
