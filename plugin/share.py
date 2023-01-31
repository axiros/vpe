import os
import sys
from functools import partial as P
import importlib

try:
    import vim
except Exception:
    # we can still parse swagger
    class vim:
        def command(*a, **kw):
            """just that the state addons work in eval"""

    print('no vim api importable', file=sys.stderr)


def vimcmd(cmd):
    return vim.command(cmd)


def vimcmdr(cmd, silent=True, title=True, opt=''):
    """vimcmd with redir into current buffer
    opt: /foo/  => insert at line matching foo
    opt: .+10   => insert 10 lines below

    """
    fn = '/tmp/vi.r.%s' % os.environ['USER']
    os.unlink(fn) if os.path.exists(fn) else 0
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


def deindent(s, spec={}):
    return s.replace(f'\n{" " * 8}', '\n') % spec


is_ = isinstance
debug = False
out = P(print, file=sys.stderr)


class ctx:
    """Interface for the caller, setting us up
    Also transfers state over debug module reloads.
    """

    cur_cls: list = []
    cur_buffer = None
    prev_buffer = None
    L1 = 0   # selected first line in vim source buffer
    L2 = 0
    # transferred even over module reloads:
    state = {'_loaded_libs': {'yaml': 'pyyaml'}}
    docs = []


def read_file(fn):
    try:
        with open(fn) as fd:
            s = fd.read()
    except Exception:
        s = ''
    return s


def lib(libname, t={}):
    """we don't always require all libs"""
    c = ctx.state['_loaded_libs']
    v = c.get(libname, libname)
    if not is_(v, str):
        return v
    if not t.get(libname):
        try:
            t[libname] = True
            c[libname] = importlib.import_module(libname)
            return c[libname]
        except Exception:
            pass
    s = '\n' + '-' * 40 + '\n'
    print(f'{s}Please: pip install {libname}{s}\n')


def log(s, **kw):
    """for debug only"""
    with open(f'/tmp/vpe', 'a') as fd:
        s = f'{s} {kw}\n'
        fd.write(s)


def notify(title, msg=''):
    os.system(f'notify-send "vpe: {title}" {msg}')


# Avoiding the infomous python indent bug for Treesitter...
BRKT = {'{', '['}
