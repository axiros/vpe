#!/usr/bin/env python
"""
# Graph Easy

Alias: ge

Uses: {CMD}

# Syntax

# Single Line

ge <words>

In the single line version, the line will be replaced with result.
Intended for outlining important content.

# Multi Line

ge
<multiline graph easy spec>
<empty line>

<!-- ge
ge spec
-->



# Examples

ge My Nice Title
┌───────────────┐
│ My Nice Title │ # replaces original line
└───────────────┘
---

ge
[ Bonn ] -> [ Berlin ]
[ Berlin ] -> [ Frankfurt ]
[ Frankfurt ] -> [ Dresden ]
[ Berlin ] <. car .> [ Potsdam ]
[ Potsdam ] = bus => [ Cottbus ]

┌──────┐     ┌─────────┐        ┌───────────┐     ┌─────────┐
│ Bonn │ ──> │ Berlin  │ ─────> │ Frankfurt │ ──> │ Dresden │
└──────┘     └─────────┘        └───────────┘     └─────────┘
               ∧
               :
               : car
               ∨
             ┌─────────┐  bus   ┌───────────┐
             │ Potsdam │ ═════> │  Cottbus  │
             └─────────┘        └───────────┘

----

ge
Bonn - car -> Berlin

┌──────┐  car   ┌────────┐
│ Bonn │ ─────> │ Berlin │
└──────┘        └────────┘


## Shorthand Notation

Lines w/o a [ and a ] are being transformed:

    'a -b< c'    '[a] -- b <-- [c]'
    'a - b < c'  '[a] -- [b] <-- [c]'
    'a - b < c'  '[a] -- [b] <-- [c]'
    'a>b'        '[a] --> [b]'
    'a = b'      '[a] == [b]'
    'a.>b'       '[a] ..> [b]'

and so on

## Html Comments

To avoid --> interpreted as html closing comments we replace those in the source by '──>'
"""

import os

from share import notify, ctx, cli_mode, uid, vimcmd, BL_SQR
from share import delete_cur_line, read_file, write_file, unlink_if
from share import get_this_and_block_after, buf, linekw, write_file_relative

exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

CMD = 'echo -e "{spec}" | graph-easy --as={fmt} 2>&1'


def try_help():
    s = __doc__.replace('{{CMD}}', CMD)
    return s


def render(spec, fmt, **kw):
    spec = spec.replace('──>', '-->')
    s = os.popen(CMD.format(spec=spec, fmt=fmt)).read()
    ret = {'lines': s}

    for img_fmt in ['svg']:
        img_kw = kw.get(img_fmt)
        if not img_kw:
            continue
        bin = True if img_fmt == 'png' else False
        img = os.popen(CMD.format(spec=spec, fmt=img_fmt)).read()
        if img_kw is True:
            # no filename -> inline them:
            # if not bin:
            #     # we ahve the source ;-0:
            #     img = img.split('<!--', 1)[0] + '</svg>'
            img = img.replace('\n', '  ')
            ret['block_append'] = img
        else:
            _, pth = write_file_relative(img_kw, img, ext=img_fmt)
            ret['block_append'] = f'![]({pth})'
    return ret


def try_load(line, block, upsert_below, **kw):

    fmt = 'boxart'
    if ' txt' in line:
        fmt = 'ascii'

    if not block:
        # single line version: foo bar -> box around both words
        delete_cur_line()
        line = f'[{line}]' if not line[0] == BL_SQR else line
        r = render(line, fmt=fmt)['lines']
        fn = f'/tmp/vpe.geres{uid}'
        write_file(fn, r)
        return vimcmd(f'.-1read {fn}')

    # other formats, png, svg wanted? svg support currently only:
    kw = {k: linekw(line, k) for k in ['svg']}
    block = [gefmt(line) for line in block]
    b = buf()
    for line, nr in zip(block, range(len(block))):
        b[ctx.L1 + nr] = line

    s = render('\n'.join(block), fmt=fmt, **kw)
    upsert_below(s)


# ------------------------------------ All below: short format
def in_brkt(s):
    s = s.strip()
    s = ' ' if not s else s
    s = (L + s) if not s[0] == L else s
    s = (s + R) if not s[-1] == R else s
    return s


# arrow single char shorthands:
full_arrw = {'-': '--', '<': '<-', '>': '->', '=': '==', '.': '..'}


def fmt_arrow(s):
    s = s.strip()
    s = full_arrw.get(s, s)
    if len(s) == 1:
        return '->'  # fallback
    if s[-1] == '>':
        b = '<' if s[0] == '<' else s[-2]
        return b + s[-2] + '>'
    elif s[0] == '<':
        e = '>' if s[-1] == '>' else s[1]
        return '<' + s[1] + e
    else:
        return s[1] + s[1]


def gefmt(line, starts='-.=<', ends='>>'):
    """Ends HAVE to be there at end of arrow"""
    if L in line and R in line:
        # already formatted
        return line
    in_node, in_arr, in_arrt = 1, 2, 3
    pos = in_node
    arrwc = starts + ends
    r = []
    while line:
        c, line = line[0], line[1:]
        if pos == in_node:
            s = c
            while line and line[0] not in arrwc:
                c, line = line[0], line[1:]
                s += c
            r.append(in_brkt(s))
            pos = in_arr

        elif pos == in_arr:
            s = c
            while line:
                if line[0] in arrwc or line[0] == ' ':
                    c, line = line[0], line[1:]
                    s += c
                    continue
                s = fmt_arrow(s)
                r.append(s)
                # line label or end node, that's the question:
                # Answer: labels must come w/o spaces:
                if (
                    c == ' '
                    or line[0] == L
                    or not any([c for c in line if c in arrwc])
                    or c == '>'
                ):
                    pos = in_node
                else:
                    pos = in_arrt
                break
        elif pos == in_arrt:
            s = c
            while line[0] not in arrwc:
                c, line = line[0], line[1:]
                s += c
            r.append(s.strip())
            pos = in_arr
    return (' '.join(r)).replace('-->', '──>')


L = '['
R = ']'
# p = fmt('B - x -> A')


def eq(s1, s2):
    print('')
    print('exp', s2)
    print('got', s1)
    assert s1 == s2


if __name__ == '__main__':
    eq(gefmt('a -b< c'), '[a] -- b <-- [c]')
    eq(gefmt('a - b < c'), '[a] -- [b] <-- [c]')
    eq(gefmt('a - b < c'), '[a] -- [b] <-- [c]')
    eq(gefmt('a > b'), '[a] --> [b]')
    eq(gefmt('a - b'), '[a] -- [b]')
