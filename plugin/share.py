from os import unlink
import os
import sys
from functools import partial as P
from operator import setitem
from importlib import import_module

uid = os.environ['USER']
here = os.path.abspath(os.path.dirname(__file__))
try:
    import vim
except Exception:
    # we can still parse swagger
    class vim:
        def command(*a, **kw):
            """just that the state addons work in eval"""

    # print('no vim api importable', file=sys.stderr)


class ctx:
    """Interface for the caller, setting us up Also transfers state over debug module reloads.

    Upper case ones set by the plugin vpe.vim
    """

    COL = 0   # column at ,r. From 1
    L = None   # full line under cursor at ,r
    L1 = 0   # Execution start line in vim source buffer. From 1, not 0
    L2 = 0   # L1 and L2 changed internally at recursive ExecSelRange call situations, e.g. jumps
    PTH = None   # full buffer file path
    W = None   # word under cursor
    _ = {'_loaded_libs': {'yaml': 'pyyaml'}}
    prev_win = None   # used in add_or_switch_to_window for 'previous' win
    cur_buffer = None
    cur_cls: list = []
    docs = []
    executed_lines = []   # cleared by the plugin at each ,r. Loop preventer
    on_any = True   # vpe_on_any support enabled
    original_line = None   # set to ctx.L1 at entry
    original_line_val = None   # content of the line. Not in use currently
    prev_buffer = None
    mod_openapi_ver = None   # mod openapi
    state = _   # transferred even over module reloads:


# -------------------------------------------------------------------------------------------- Tools
is_ = isinstance
debug = False
out = P(print, file=sys.stderr)
exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath


def deindent(s, spec={}):
    return s.replace(f'\n{" " * 8}', '\n') % spec


def cli_mode():
    return os.environ.get('vpe_cli_mode') == 'true'


def unlink_if(fn):
    if exists(fn):
        os.unlink(fn)


def write_file(fn, s):
    os.makedirs(dirname(fn), exist_ok=True)
    with open(fn, 'w') as fd:
        fd.write(s)


def read_file(fn):
    try:
        with open(fn) as fd:
            s = fd.read()
    except Exception:
        s = ''
    return s


printed = set()


def lib(libname, t={}):
    """we don't always require all libs"""
    c = ctx.state['_loaded_libs']
    v = c.get(libname, libname)
    if not is_(v, str):
        return v
    if not t.get(libname):
        try:
            t[libname] = True
            c[libname] = import_module(libname)
            return c[libname]
        except Exception:
            pass
    s = '\n' + '-' * 40 + '\n'
    msg = f'{s}Please: pip install {libname}{s}\n'
    if not msg in printed:
        print(msg, file=sys.stderr)
        printed.add(msg)


def log(s, **kw):
    """for debug only"""
    kw = ', '.join([f'{k}: {v}' for k, v in kw.items()])
    with open(f'/tmp/vpe', 'a') as fd:
        s = f'{s} {kw}\n'
        fd.write(s)


def notify(title='', msg='', dt=3):
    title = title or 'VPE'
    os.system(f'notify-send -t {dt} "{title}" "{msg}"')


# ------------------------------------------------------------------------------------------------ Vim API tools


def win_showing(buffername):
    bid = vim.eval(f'bufwinnr("{buffername}")')
    return False if bid == '-1' else bid


def result_win_showing():
    return win_showing('results.py')


def clear_all(buffer):
    del buffer[0: len(buffer)]


def buf():
    return vim.current.buffer


def add_or_switch_to_window(buffername, remember_cur=False, b=None):
    """Create a split win, or, if present, switch to it
    Provides a remember feature to switch back using the convention name 'previous'
    """
    if buffername == 'previous':
        vim.current.window = ctx.prev_win
        return
    if remember_cur:
        ctx.prev_win = vim.current.window
    bid = win_showing(buffername)
    if bid == False:
        vimcmd(f'rightbelow vsplit {buffername}')
        vimcmd('setlocal buftype=nofile nospell')
    else:
        vimcmd(f'{bid}wincmd w')
    return vim.current.buffer


def vimcmd(cmd):
    return vim.command(cmd)


def delete_cur_line():
    vimcmd('.d')


def vimcmdr(cmd, silent=True, title=True, opt=''):
    """vimcmd with redir into current buffer
    opt: /foo/  => insert at line matching foo
    opt: .+10   => insert 10 lines below

    """
    fn = '/tmp/vi.r.%s' % os.environ['USER']
    unlink_if(fn)
    # vimcmd(f':write | redir >> {fn} | :{cmd} | redir END | edit')
    vimcmd(f'redir >> {fn}')
    vimcmd(f'silent! {cmd}')
    vimcmd('redir END')
    s = read_file(fn)  # .strip()
    if not s.strip():
        return None if silent else vimcmd(f'lua vim.notify("{cmd}")')

    # sometimes cmd is first line (:!date)
    while '\n' in s:
        _, s = s.split('\n', 1)
        if _.strip() and _ != cmd:
            break
    t = '' if not title else title if is_(title, str) else str(cmd)
    with open(fn, 'w') as fd:
        fd.write(f'{t}\n') if t else None
        fd.write(s)
    # TODO: check ctx.L1, ctx.src_buf if have enough lines below and above
    return vimcmd(f'{opt} read {fn}')

    # if '\n' in s:
    #     # insert below cursor:
    #     return vimcmd(f'.-0read {fn}')
    # else:
    #     src_buf[nrs[0]] = s


# Avoiding the infomous python indent bug for Treesitter...
BRKT = {'{', '['}
BL_RND, BL_SQR = '(['
