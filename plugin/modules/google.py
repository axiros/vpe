#!/usr/bin/env python
"""
# Google Around From Within Vim

`g my search keywords [@site]`

# --site keywords

{known_sites}

The keyword can be anywhere

# Examples

g cnn news germany
g @gh vpe

Will search google and display all URLs from the first page, excluding the non interesting
google internal ones.

💡 Select all links and open the browser on them using `,g`, smart open (see below).

# CLI Example

```
[gk@axgk ~]$ vpe g vim python evaluation
https: // vim.fandom.com/wiki/Evaluate_current_line_using_Python
https: // vim.fandom.com
(...)
```
"""

from share import notify, vim, wrap_text_result
import sys
import base64
import uuid
import requests
import urllib
import re


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
rm_from_res = ['.google', '.w3.', '.sec.', '.gstatic', 'schema.org']
rm_if_endswith = ['.svg', '.png', '&amp', '.xml', '.jpg', 'jpeg', '/stack_overflow_']
known_sites = {'@gh': 'github.com', '@so': 'stackoverflow.com'}


def try_help():
    h = __doc__.format(known_sites=known_sites)
    return h


def metas(line):
    line = line + ' '
    s, e = [], []
    for k, v in known_sites.items():
        if k in line:
            s.append(v)
            line = line.replace(k, '')
    return line.strip(), s, e


def links(txt):
    urls = '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'
    a = re.findall(urls, txt)

    def filt(i):
        url = f'{i[0]}://{"".join(i[1:])}'
        ul = url.lower()
        for k in rm_from_res:
            if k in ul:
                return
        for k in rm_if_endswith:
            if ul.endswith(k):
                return
        return url

    rd, r = [filt(i) for i in a], []
    [r.append(l) for l in rd if l and l not in r]
    return r

    # r = [l for l in r if l]
    # r = sorted(list(set(r)))
    # r = list(set(r))
    # return r


def from_picker(word):
    res = try_load(word)
    return res


def try_load(line='vpe', **kw):
    """s the content of a swagger definition file"""
    line, sites, exclude = metas(line)
    q = urllib.parse.quote_plus(line)
    q += '+OR'.join('+site:' + urllib.parse.quote_plus(site) for site in sites)
    q += ''.join('+-site:' + urllib.parse.quote_plus(e) for e in exclude)
    sei = base64.encodebytes(uuid.uuid4().bytes)
    sei = sei.decode('ascii').rstrip('=\n').replace('/', '_')
    # 'gbv': '1',  # 1: js / 2: no javascript
    url = f'https://www.google.com/search?ie=UTF-8&oe=UTF-8&q={q}&sei={sei}'
    n = {
        'Accept': 'text/html',
        'Accept-Encoding': 'gzip',
        'User-Agent': USER_AGENT,
        'Cookie': '',
        'Connection': 'keep-alive',
        'DNT': '1',
    }

    t = requests.get(url, headers=n).text
    l = links(t)
    s = '\n'.join(l).strip()
    s = wrap_text_result(s, 'google', line)
    return {'lines': s, ':here': True, 'list': l}


if __name__ == '__main__':
    res = try_load(line=' '.join(sys.argv[1:]))
    for k in res['list']:
        print(k)
