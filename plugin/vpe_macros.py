from share import os, read_file

# ------------------------------------------------------------------------------------------------ "macros"
# some predefined code blocks, extensible by user:
m_r = """
if 'Sending requests to API endpoint':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from json import dumps
    headers = {'Content-Type': 'application/json', 'User-Agent': 'vpe'}

    def Post(url, data):
        req = Request(url, data=dumps(data).encode(), headers=headers, method='POST')
        try:
            with urlopen(req, timeout=10) as r:
                return r.read().decode()
        except HTTPError as e:
            return e.read().decode()

class R:
    # :clear
    # :cmt pastebin example
    url = 'http://httpbin.org/post'
    data = { "mydata": { "hello": "world" }}
    p = Post(url, data=data)
    # y = Post(url, data=data)

"""

m_rx = """

'Testing Reactive-X for Python'
import gevent

import rx as Rx
from rx import operators as rx  # noqa

# If you need subjects:
from rx import subject

# If you need a scheduler:
from rx.scheduler.eventloop import GEventScheduler  # noqa
GS = GEventScheduler(gevent)

# and an actual test:
s1 = Rx.from_([1, 2, 3])
s2 = Rx.from_(['a', 'b', 'c', 'd'])
s3 = Rx.from_(['A', 'B'])
p = []
s1.pipe(rx.combine_latest(s2, s3)).subscribe(lambda x: p.append(x))

"""

macros = {'r': m_r, 'rx': m_rx}
# custom ones:
fn_m = os.environ['HOME'] + '/.config/vpe/macros.py'
s = read_file(fn_m)
m = {}
if s:
    exec(s, m, m)
    if 'macros' in m:
        macros.update(m['macros'])


def help():
    """Display available macros"""

    r = 'Enter letter and hit evaluation hotkey on it:\n\n'
    for m, v in macros.items():
        v = '# ' + v.lstrip().split('\n', 1)[0].replace('if ', '')
        r += f'{m}: {v}\n'
    r += '\n\nResults you get by assigning "p" or "y" in code blocks.'
    r += '\n\n ' + __file__
    return r
