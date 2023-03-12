#!/usr/bin/env python
"""
# Build a TOC Tree

UNFINISHED / EXPERIMENTAL

toctree <depth> [size=100]

USES: {CMD}
"""

import os
from share import notify, ctx, cli_mode, read_file, vimcmd, write_file
from pathlib import Path

exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

CMD = 'fd --follow --type=f --extension=md --maxdepth={depth}'


def try_help():
    return __doc__.format(CMD=CMD)


def nfos(fn, size):
    s = '\n' + read_file(fn) + '\n'
    h, l = '#', ''
    for i in range(5):
        l = s.split(f'\n{h} ', 1)
        if len(l) == 2:
            break
        h += '#'
    if i > 3:
        l = [0, s]
    h, post = l[1].split('\n', 1)
    s = f'**{h}**\n{post[:size]}...'
    return {'pth': f'./{fn}', 'txt': s}


def intofn(fninto, toc):
    s = read_file(fninto)
    sep = '<!-- toctree -->'
    if not sep in s:
        s += f'\n{sep}\n{sep}\n'
    pre, old_toc, post = s.split(sep)[:3]
    toc = '\n'.join(toc)
    s = f'{pre}{sep}{toc}{sep}{post}'
    write_file(fninto, s)


def basename(fn):
    return fn.rsplit('.md', 1)[0].rsplit('/', 1)[-1]


def add(spec, toc):
    fn, s = spec['pth'], spec['txt']
    lvl = len(fn.split('/'))
    fn = basename(fn)
    ins = lvl * '  '
    s = f'<tr><td>{ins}{fn}</td></tr>'
    toc.append(s)


def build(fninto, depth, size):
    dir = dirname(fninto)
    os.chdir(dir)
    files = sorted(os.popen(CMD.format(depth=depth)).read().strip().splitlines())
    specs = [nfos(f, size) for f in files if not fninto.endswith(f'/{f}')]
    toc = ['', '<table>']
    [add(spec, toc) for spec in specs]
    toc.extend(['</table>', ''])
    intofn(fninto, toc)
    vimcmd('edit')


def try_load(s: str = '', line='vpe', **kw):
    """s the content of a swagger definition file"""
    line += ' 100'
    depth, size = [int(i) for i in line.split()[:2]]
    tree = build(ctx.PTH, depth, size)
    here = os.getcwd()
    notify('', tree, 10)
    os.chdir(here)
