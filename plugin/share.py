from pathlib import Path
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

all_mods = {}


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
    prev_mod_line = None  # module line of a previous run (so that we can us it if inside block)
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
    src_buf = None  # .current.buffer
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


fn_into_buf = '/tmp/vi.here.%s' % os.environ['USER']


def add_lines(lines, offs=1):
    src_buf = ctx.src_buf or vim.current.buffer
    with open(fn_into_buf, 'w') as fd:
        fd.write(lines)
    if ctx.L1 == len(src_buf):
        src_buf.append('')
    vimcmd(f'.+{offs}read {fn_into_buf}')


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


def cast(s: str, b={'true': True, 'false': False}):
    s = s.lower()
    if s in b:
        return b[s]
    try:
        return float(s)
    except Exception:
        try:
            return int(s)
        except Exception:
            pass
    return s


def write_file_relative(pth, s, ext=None):
    if ext:
        pth = pth if pth.endswith(f'.{ext}') else f'{pth}.{ext}'
    fn = Path(ctx.PTH).parent.joinpath(Path(pth))
    d = str(fn.parent)
    notify('dir', d)
    if not exists(d):
        notify('making dir', d)
        os.makedirs(str(fn.parent))
    if not os.path.isdir(d):
        raise Exception(f"{d} is not a directory")
    if isinstance(s, bytes):
        fn.write_bytes(s)
    else:
        fn.write_text(s)
    return str(fn), pth


def linekw(line, kw):
    kw = ' ' + kw
    line = ' ' + line
    if kw not in line:
        return None
    pre, val = line.split(kw, 1)
    if val.startswith('='):
        return cast(val.split(' ', 1)[0][1:])
    return True


def find_block_end_seps(b, nr, ends, addl=0):
    '''Block end encountered, do we have more enclosing endings right after, which we should keep?
    '''
    while nr < len(b)-1:
        nr += 1
        if b[nr] not in ends:
            break
        addl += 1
    return addl


def get_this_and_block_after(sep, mod, seps, wanted):   # ends={'-->', ''}):
    '''block terminated by sep, which is '', '-->', '"""', ...:'''
    seps = dict(seps)
    end = seps[sep] if sep else ''
    fmt = getattr(mod, 'linefmt', None)
    block, nr, b = [], ctx.L1, buf()
    addl = 1
    for nr in range(ctx.L1, len(b)):
        l = b[nr]
        if l.strip() == end:
            a = 1 if end else 0
            addl = find_block_end_seps(b, nr, seps.values(), a)
            break
        if fmt:
            b[nr] = fmt(l)
        block.append(l)
    ub, full_block = False, False
    if 'upsert_below' in wanted:
        after = find_block_after(nr+addl-1, b, seps)
        ub = P(upsert_below, after=after, offs=nr-ctx.L1+addl, delim=['<!--', '-->'])
    if 'full_block' in wanted:
        # go up:
        full_block, i = list(block), ctx.L1
        for nr in range(ctx.L1, 0, -1):
            if not b[nr-1].strip():
                break
            full_block.insert(0, b[nr-1])

    return block, ub, full_block


def find_block_after(nr, buffer, seps):
    '''returns start and stop line of the next block determinated by seps'''
    b = buffer
    seps.pop('', None)  # empty lines allowed
    strt, stp = 0, 0
    # look max 4 lines ahead:
    for nr in range(nr, min(len(b), nr + 4)):
        l = b[nr].strip()
        if not l or l not in seps:
            continue
        end = seps[l]
        strt = nr + 1
        for nr in range(nr, len(b)):
            le = b[nr]
            if le.startswith(end):
                stp = nr + 1
                if '<!--' in le:
                    stp += int(le.split('<!--', 1)[1][:-3])
                return strt, stp+1


def upsert_below(rendered, after, offs, delim):
    if isinstance(rendered, str):
        rendered = {'lines': rendered}
    res = rendered['lines']
    s = f'\n{delim[0]}\n{res.rstrip()}\n{delim[1]}\n'
    se = rendered.get('block_append')
    if se:
        l = len(se.splitlines())
        s = s[:-1] + f'<!--{l}-->\n' + se

    fn = '/tmp/vpe.rendering.{UID}'.format(UID=uid)
    write_file(fn, s)
    vimcmd(f'.{offs}read {fn}')
    if after:
        l = len(s.splitlines())
        i = 1 if after[1] + l > len(buf()) else 0
        vimcmd(f'{after[0] + l},{after[1] + l-i}d')
        vimcmd(str(ctx.original_line))
        # vimcmd(f'{ctx.L1}')


# Avoiding the infomous python indent bug for Treesitter...
BRKT = {'{', '['}
BL_RND, BL_SQR = '(['
