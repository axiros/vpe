#!/usr/bin/env python
"""
Tests: see __main__
"""

import time
from pathlib import Path
import re
import sys
import json
from functools import partial
from share import notify, log, ctx, BL_RND, BL_SQR

try:
    import vim
except Exception:
    vim = None
import os

dirname, abspath, exists = os.path.dirname, os.path.abspath, os.path.exists


def imgopencmd(fnimg):
    return f'$BROWSER "{fnimg}" >/dev/null 2>&1'


def google_search(word):
    return 'https://www.google.com/search?client=%s-b-d&q=' + word


# fmt: off
class Edit(Exception)   : pass
class Browse(Exception) : pass
class RunCmd(Exception) : pass
class Noop(Exception)   : pass
def browse(url)         : raise Browse(url)
def edit(fn, content=''): raise Edit(fn, content)
def run(cmd)            : raise RunCmd(cmd)
# fmt: on


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


def read_file(fn):
    try:
        with open(fn) as fd:
            return fd.read()
    except Exception:
        return ''


def google(word):
    return browse(google_search(word))


def is_markdown_ref_link(fn, word, word_space_sepped, dir, line, **kw):
    """Always open it, no matter where we are in that line"""
    if not line:
        return  # or not fn.endswith('.md'): return
    # comments (with e.g. other links) are anyway not allowed in ref link lines by md => really, just hit the link:
    if not (line[0] == '[' and ']: ' in line):
        return
    title, link = line.split(']: ', 1)
    link = link.split(' ', 1)[0].strip()
    if not link:
        google(title[1:])
    url_or_file_browse_or_edit(link, dir, title=title)

    # fn1 = pth_join(dir, link)
    #
    # if exists(fn1):
    #     edit(fn1)
    #
    # browse(link)


def pth_join(dir, fn):
    return str(Path(dir).joinpath(Path(fn)))


def url_or_file_browse_or_edit(lnk, dir, title=''):
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
            run(imgopencmd(pth))
        edit(pth)
    if exists(pth + '.md'):
        edit(pth + '.md')
    if not pth.endswith('.md'):
        return
    d = dirname(pth)
    if not exists(d):
        notify('Creating directory', d)
        os.makedirs(d)
    edit(pth, content=f'# {title}\n(save to create file)')

    # if not lnk.endswith('.md'): edit(lnk)


def touch_new_md_file(fn, title):
    notify('Creating file', fn)
    os.makedirs(dirname(abspath(fn)), exist_ok=True)
    with open(fn, 'w') as fd:
        fd.write('# %s' % title)


def is_markdown_direct_link(fn, word_space_sepped, **kw):
    w = word_space_sepped
    if w.startswith('<http') and '://' in w and w[-1] == '>':
        browse(w[1:-1])


def is_markdown_link(col, fn, word, word_space_sepped, dir, line, **kw):
    """On title: browse. On link: open. On ref link: go to it"""
    # log('link', **locals())
    if not word_space_sepped:  # or not fn.endswith('.md'):
        return

    # word can be within a space sepped title ->
    x = between(col, line, ']', ']')
    if x and x[0] == BL_SQR:
        # we are in md ref link.
        rlt = between(col + 1, line, '[', ']')
        # search it in buffer or file
        if vim and hasattr(vim, 'current'):
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
        url_or_file_browse_or_edit(x[1:], dir, title=title)
        # pth = pth_join(dir, x[1:])
        # if pth.endswith('.md'):
        #     touch_new_md_file(pth, title)
        #     edit(pth)


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


def no_apos(w):
    for k in '"', "'", '`':
        w = w.replace(k, '')
    return w


def is_file_path_or_url(dir, **kw):
    words = all_words(kw)
    H = os.environ['HOME']
    for d in dir, os.getcwd():
        for w in words:
            if not w:
                continue
            w = no_apos(w)
            if w.startswith('http') and '://' in w:
                browse(w)
            w = w.replace('~', H).replace('$HOME', H)
            k = pth_join(d, w)
            if exists(k):
                edit(k)
            if len(w.split('/')) == 2:
                browse('https://github.com/' + w)


def is_lcdoc_lp_line(dir, fn, **kw):
    return


def is_browsable(word, **kw):
    if word.startswith('http') and '://' in word:
        browse(word)
    if len(word) > 3:
        google(word)


def get_test_table(T):
    table = ['', '|Word|Whole Line<BR>Valid Cursor Positions: ^<br>Open Action|Comment|']
    table += ['|-  |-           | - |']
    for msg, set in T:
        for t in set:
            # many cols in one test?
            L = ['']
            add = L.append
            curs = t[0][0]
            if not isinstance(curs, tuple):
                curs = (t[0][0], t[0][0] + 1)
            word, line = t[0][1], t[0][2]
            line = line.replace('`', '^')

            mark = '^' * (curs[1] - curs[0])
            if curs[0] > 0:
                mark = '.' * curs[0] + mark
            add(f'`{word}`')
            t.append('')
            if not t[1]:
                res = ' '
            elif t[1][0]:
                fn = t[1][0]
                if isinstance(fn, tuple):
                    fn, dir, content = fn
                    content = content.replace('\n', ' LS ')
                    t[2] += f'<BR>dir created<BR>content: `{content}`'
                res = f'✔️`{fn}`'
            elif t[1][1]:
                # add(f'`{t[1][0]}')
                res = f'🌐`{t[1][1]}`'
                if 'search?' in res:
                    res = f'🌐search: `{res.split("search?", 1)[1]}'
            elif t[1][2]:
                res = f'⌨`{t[1][2]}`'
            else:
                res = ' '
            add(f'`{line}` <br> `{mark}` <br> {res}')
            if len(t) > 2 and t[2]:
                add(f'{t[2]}')
            add(' ')
            table.append('|'.join(L))

    t = '\n'.join(table)
    return f'\n\n{t}\n||Notes: <br> - backticks replaced with `^` <br> - Testfile contains markdown ref:<br>   `[foo bar]: http://foo.bar`|\n\n'


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
        is_markdown_direct_link,
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
    now = time.time
    t0 = now()
    H = os.environ['HOME']
    L = 'http://foo.bar'
    TMD1 = """
    Test [title](newfile.md) bla
    bla [bar][foo] bla
    xxx
    [foo bar]: {L}
    [hosts]: /etc/hosts
    """
    TMD1 = TMD1.format(L=L).replace('\n    ', '\n')
    # we use foo a lot and want to avoid a file foo existing in test dir
    TD = f'/tmp/vpeso.{os.environ["USER"]}'  # testdir
    os.system(f'/bin/rm -rf "{TD}"')
    os.makedirs(TD)
    os.system(f'touch {TD}/testimg.png')
    fntmd1 = f'{TD}/m1.md'
    G = google_search

    # Testmatrix gourps all use cases uder the error msgs as first item of the nested list
    # thhen defines what is handed over to the handle entry function.
    # and defines what is expected to happen ([edit, browse] or function or None)
    T = [
        [
            'Must edit',
            [
                [
                    [(11, 15), 'readme', '[foo bar][hosts](, g bla)', 1, fntmd1],
                    ['/etc/hosts'],
                    'Ref link to existing file is opened',
                ],
                [
                    [(9, 14), 'x', f'[new]: {fntmd1}'],
                    [fntmd1],
                    'Ref link to existing file is opened',
                ],
                [
                    [(9, 14), 'x', 'foo [xxx](x1/x1.md)', 1, fntmd1],
                    [(f'{TD}/x1/x1.md', f'{TD}/x1', '# xxx\n')],
                    'Linked non existing markdown files: Dir created, file unsaved opened in vi',
                ],
                [
                    [(4, 10), 'bashrc', 'foo ~/.bashrc', ''],
                    [H + '/.bashrc'],
                    'tilde replaced, file open in vi',
                ],
                [
                    [(4, 15), 'bashrc', 'foo $HOME/.bashrc', ''],
                    [H + '/.bashrc'],
                    '$HOME replaced',
                ],
                [
                    [(5, 10), 'bashrc', "'foo ~/.bashrc'", ''],
                    [H + '/.bashrc'],
                    'tilde replaced, file open in vi',
                ],
                [
                    [(15, 25), 'etc', 'foo some_func("/etc/hosts") bar', ''],
                    ['/etc/hosts'],
                    'file name extracted',
                ],
                [
                    [(15, 25), 'etc', 'foo some_func(`/etc/hosts`) bar', ''],
                    ['/etc/hosts'],
                    'file name extracted in backticks',
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
                [
                    [(16, 18), 'y', 'x b [a][foo bar] y', 1, fntmd1],
                    [],
                    'y only: no action',
                ],
            ],
        ],
        [
            'Must Run Command',
            [
                [
                    [(10, 16), 'testimg', 'x b ![](./testimg.png)', 1, fntmd1],
                    [0, 0, imgopencmd(TD + '/testimg.png')],
                    'Must run the image open command',
                ]
            ],
        ],
        [
            'Must browse',
            [
                [[(1, 6), 'foobar', 'a foobar bar foo'], [0, G('foobar')]],
                [[(0, 6), 'foobar', 'foobar bar foo'], [0, G('foobar')]],
                [[(5, 12), 'a', 'b [a](http://foo/bar) x'], [0, 'http://foo/bar']],
                # markdown_direct_links:
                [[(5, 12), 'a', 'b <http://foo/bar>'], [0, 'http://foo/bar']],
                [[(5, 12), 'a', 'b <https://foo/bar> '], [0, 'https://foo/bar']],
                # ref link:
                [[(0, 10), 'foo', f'[foo]: {L}'], [0, L]],
                [
                    [(3, 9), 'git', 'a "git/hub" foo'],
                    [0, 'https://github.com/git/hub'],
                    'github default for 2 word slash sepped',
                ],
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
                    [(4, 6), 'a', 'x b [a][foo bar] x', 1, fntmd1],
                    [0, G('a')],
                    'Google the title',
                ],
                [
                    [(4, 13), 'barx', 'x b [barx bah][foo] x', fntmd1],
                    [0, G('barx bah')],
                    'Google ALL title',
                ],
            ],
        ],
    ]
    if match == 'get_table':
        t = get_test_table(T)
        print(t)
        fn = dirname(__file__) + '/../docs/smart_goto.md'
        sep = '<!--@examples-->'
        s = read_file(fn).split(sep)
        s = sep.join([s[0], t, s[2]])
        with open(fn, 'w') as fd:
            fd.write(s)
        return print('written', fn)

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
                    fn = t[1][0]
                    if isinstance(fn, tuple):
                        fn, dir, content = fn
                        assert exists(dir), msg
                        assert ex.args[1].startswith(content), msg
                    assert ex.args[0] == fn, msg
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

                except RunCmd as ex:
                    try:
                        assert ex.args[0] == t[1][2], msg
                    except Exception as ex1:
                        print('breakpoint set')
                        breakpoint()
                        keep_ctx = True
                    print(' ✅')
                    continue
                raise Exception(msg, t)
    test(match='get_table')
    print(f'\x1b[1m✅ All well \x1b[0m [{round(now()-t0, 2)}s]')


if __name__ == '__main__':
    sys.argv.append('')
    test(match=sys.argv[1])
