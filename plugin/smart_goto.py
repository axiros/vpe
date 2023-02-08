#!/usr/bin/env python
"""
":reload" in the line will reload this file
"""
from pathlib import Path
import re
import sys
import json
from functools import partial
from share import notify, log, ctx

try:
    import vim
except Exception:
    vim = None
import os

dirname, abspath, exists = os.path.dirname, os.path.abspath, os.path.exists


class Edit(Exception):
    pass


class Browse(Exception):
    pass


class Noop(Exception):
    pass


def is_man_page(word, fn, **_):
    """are we viewing a manpage and we ,g over e.g. touch(5)"""
    if not fn.startswith('man://'):
        return
    w = word.split(')', 1)[0]
    try:
        _ = int(w.split(BL_RND, 1)[1])
    except Exception:
        return

    raise Edit(f'man://{word}')


def is_help(word, **m):
    """edit this file"""
    if word in {'help', '?'}:
        raise Edit(__file__)


def browse(url):
    raise Browse(url)


def edit(fn):
    raise Edit(fn)


def read_file(fn):
    try:
        with open(fn) as fd:
            return fd.read()
    except Exception:
        return ''


def google_search(word):
    return 'https://www.google.com/search?client=%s-b-d&q=' + word


def google(word):
    return browse(google_search(word))


def is_markdown_ref_link(fn, word, word_space_sepped, dir, line, **kw):
    """Always open it, no matter where we are in that line"""
    if not line or not fn.endswith('.md'):
        return
    # comments (with e.g. other links) are anyway not allowed in ref link lines by md => really, just hit the link:
    if line[0] == '[' and ']: ' in line:
        title, link = line.split(']: ', 1)
        link = link.split(' ', 1)[0].strip()
        if not link:
            google(title[1:])
        browse(link)


def pth_join(dir, fn):
    return str(Path(dir).joinpath(Path(fn)))


def url_or_file(lnk, dir):
    if lnk.startswith('http') and '://' in lnk:
        browse(lnk)
    # (./parameters.md#section)
    lnk = lnk.split('#', 1)[0]

    if lnk.endswith('/'):
        pth = pth_join(dir, lnk + 'index.md')
        if exists(pth):
            lnk += 'index.md'

    pth = pth_join(dir, lnk)
    if exists(pth):
        if pth.rsplit('.', 1)[-1].lower() in {'png', 'svg', 'jpeg', 'gif', 'jpg'}:
            # show img in browser
            browse(pth)
        edit(pth)
    if exists(pth + '.md'):
        edit(pth + '.md')

    # if not lnk.endswith('.md'): edit(lnk)


def touch_new_md_file(fn, title):
    notify('Creating file', fn)
    os.makedirs(dirname(abspath(fn)), exist_ok=True)
    with open(fn, 'w') as fd:
        fd.write('# %s' % title)


def is_markdown_link(col, fn, word, word_space_sepped, dir, line, **kw):
    """On title: browse. On link: open. On ref link: go to it"""
    if not word_space_sepped or not fn.endswith('.md'):
        return

    # word can be within a space sepped title ->
    x = between(col, line, ']', ']')
    if x and x[0] == BL_SQR:
        # we are in md ref link title.
        rlt = between(col + 1, line, '[', ']')
        # search it in buffer or file
        if vim:
            b = vim.current.buffer
        else:
            b = read_file(fn).splitlines()

        s = f'[{rlt}]: '
        line = [k for k in range(0, len(b)) if b[k].startswith(s)]
        if line:
            return handle(2, rlt, b[line[0]])
        google(rlt)

    # [[(4, 5), 'a', 'x b [a][foo bar] x', 1, fntmd1], [0, L]],
    x = between(col + 1, line, '[', ']')
    if x and BL_SQR not in x and BL_RND not in x:
        # is md title:
        google(x)
    x = between(col + 1, line, ']', ')')
    if x and x[0] == BL_RND:
        # md link
        title = line.split(x, 1)[0]
        if BL_SQR not in title:
            return
        title = title.rsplit(BL_SQR, 1)[-1][:-1]
        url_or_file(x[1:], dirname(fn))
        pth = pth_join(dir, x[1:])
        if pth.endswith('.md'):
            touch_new_md_file(pth, title)
            edit(pth)


def between_spaces(col, line):
    return between(col, line, ' ', ' ', req=False)


def between(col, line, sepl, sepr, req=True):
    pre, post = line[:col], line[col:]
    r = ''
    if req:
        if not (sepl in pre and sepr in post):
            return ''
    if not pre.endswith(sepl):
        r = pre.rsplit(sepl, 1)[-1]
    if not post.startswith(sepr):
        r += post.split(sepr, 1)[0]
    return r


def between_apos(col, line):
    w = between(col, line, '"', '"')
    if not w:
        w = between(col, line, "'", "'")
    if not w:
        w = between(col, line, '`', '`')
    return w


def clean_special_chars(w):
    for k in {'*', ':'}:
        w = w.replace(k, '')
    return w


def all_words(kw):
    k = 'word  word_between_apos  word_space_sepped  word_between_apos_clean'
    return [kw[i] for i in k.split()]


def is_file_path_or_url(dir, **kw):
    words = all_words(kw)
    H = os.environ['HOME']
    for d in dir, os.getcwd():
        for w in words:
            if not w:
                continue
            if w.startswith('http') and '://' in w:
                browse(w)
            w = w.replace('~', H).replace('$HOME', H)
            k = pth_join(d, w)
            if exists(k):
                edit(k)


def is_lcdoc_lp_line(dir, fn, **kw):
    return


def is_browsable(word, **kw):
    if word.startswith('http') and '://' in word:
        browse(word)
    if len(word) > 3:
        google(word)


def handle(col, word, line, linenr=1, fn='x.md'):
    """pth='' when no writgble buffer"""
    dir = abspath(dirname(fn))
    line = line.rstrip()
    col = min(len(line) - 1, col)
    # vim will pck NEXT word on spaces:
    while line[col] == ' ':
        col += 1
    word_space_sepped = between_spaces(col, line)
    word_between_apos = between_apos(col, line)
    word_between_apos_clean = clean_special_chars(word_between_apos)

    m = dict(locals())
    s = '\n\r'.join([f'{k.ljust(5)}: {v}' for k, v in m.items()])
    # notify('📖 Smart Goto', s, 10)

    for f in [
        is_man_page,
        is_help,
        is_markdown_ref_link,
        is_markdown_link,
        is_file_path_or_url,
        is_lcdoc_lp_line,
        is_browsable,
    ]:
        print(f'Trying {f.__name__}')
        f(**m)
    raise Noop()


def test(match):
    """We write one test FILE which we rely on for some "same directory" related tests
    For most of the use cases we do not need that and just act on current word marked
    when pressing the hotky

    """
    H = os.environ['HOME']
    L = 'http://foo.bar'
    TMD1 = """
    Test [title](newfile.md) bla
    bla [bar][foo] bla
    xxx
    [foo bar]: {L}
    """
    TMD1 = TMD1.format(L=L).replace('\n    ', '\n')
    d = f'/tmp/vpeso.{os.environ["USER"]}'
    os.makedirs(d, exist_ok=True)
    # we use foo a lot and want to avoid a file foo existing in test dir
    [os.unlink(f'{d}/{i}') for i in os.listdir(d)]
    fntmd1 = f'{d}/m1.md'
    G = google_search

    def check_created(t, ex, fn):
        assert exists(fn)
        assert type(ex) == Edit
        os.unlink(fn)

    # Testmatrix gourps all use cases uder the error msgs as first item of the nested list
    # thhen defines what is handed over to the handle entry function.
    # and defines what is expected to happen ([edit, browse] or function or None)
    T = [
        [
            'Must edit',
            [
                [
                    [(9, 14), 'x', f'foo [xxx]({fntmd1}.tst.md)'],
                    partial(check_created, fn=fntmd1 + '.tst.md'),
                    'Linked  markdown files are autocreated',
                ],
                [
                    [16, 'newfile', 'Test [my title](newfile.md) bla', 1, fntmd1],
                    partial(check_created, fn=d + '/newfile.md'),
                ],
                [
                    [(4, 10), 'bashrc', 'foo ~/.bashrc', ''],
                    [H + '/.bashrc'],
                    'tilde replaced',
                ],
                [
                    [(4, 15), 'bashrc', 'foo $HOME/.bashrc', ''],
                    [H + '/.bashrc'],
                    '$HOME replaced',
                ],
            ],
        ],
        [
            'No Op',
            [
                [
                    [(9, 14), 'bla', f'foo [xxx]({fntmd1}.tst)'],
                    [],
                    'No auto creation of non .md file',
                ],
                [
                    [0, 'x', 'x b [a][foo bar] x'],
                    [],
                    '< 3 letter words (x) are not googled',
                ],
                [[16, 'y', 'x b [a][foo bar] y', 1, fntmd1], [], 'y only: no action'],
            ],
        ],
        [
            'Must browse',
            [
                [[(1, 6), 'foobar', 'a foobar bar foo'], [0, G('foobar')]],
                [[(0, 6), 'foobar', 'foobar bar foo'], [0, G('foobar')]],
                [[(5, 12), 'a', 'b [a](http://foo/bar) x'], [0, 'http://foo/bar']],
                [[(0, 10), 'foo', f'[foo]: {L}'], [0, L]],
                [
                    [1, 'foo', f'[foo]: {L} .'],
                    [0, L],
                    'Splits off after the link by space',
                ],
                [
                    [(0, 5), 'foo', '[foo bar]: '],
                    [0, G('foo bar')],
                    'No link -> google title',
                ],
                [
                    [(7, 12), 'foo', 'x b [a][foo bar] x', 1, fntmd1],
                    [0, L],
                    'Find defined link in the file, open it',
                ],
                [
                    [(4, 5), 'a', 'x b [a][foo bar] x', 1, fntmd1],
                    [0, G('a')],
                    'Google the title',
                ],
                [
                    [(4, 12), 'barx', 'x b [barx bah][foo] x', fntmd1],
                    [0, G('barx bah')],
                    'Google ALL title',
                ],
            ],
        ],
    ]

    def h(col, word, line, nr=0, fn='/tmp/foo.md'):
        # md has most features -> is default
        return handle(col, word, line, nr, fn)

    with open(fntmd1, 'w') as fd:
        fd.write(TMD1)
    for msg, set in T:
        for t in set:
            if match not in str(t):
                continue

            print(f'\x1b{BL_SQR}41m%s\x1b{BL_SQR}0m' % str(t))

            # many cols in one test?
            if not isinstance(t[0][0], tuple):
                t[0][0] = (t[0][0], t[0][0] + 1)
            for col in range(*t[0][0]):
                try:
                    print(f'{msg}: {col} {t[1:]}', end='')
                    h(col, *t[0][1:])

                except Noop:
                    assert not t[1]
                    print(' ✅')
                    continue

                except Edit as ex:
                    if callable(t[1]):
                        t[1](t, ex)
                        continue
                    assert ex.args[0] == t[1][0], msg
                    print(' ✅')
                    continue

                except Browse as ex:
                    try:
                        assert ex.args[0] == t[1][1], msg
                    except Exception as ex1:
                        print('breakpoint set')
                        breakpoint()
                        keep_ctx = True
                    print(' ✅')
                    continue
                raise Exception(msg, t)
    print('All well')


BL_RND = '('
BL_SQR = '['
if __name__ == '__main__':
    sys.argv.append('')
    test(match=sys.argv[1])

# is_markdown_dragshot_req,
# on_empty_in_md_file_do_mkdocs_serve,
# on_empty_in_md_file_do_mkdocs_serve,
