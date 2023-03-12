#!/usr/bin/env python
"""
# Creates MD Tables

Hotkey on a line starting with a "|" formats the whole block (incl. rows above)
delimitted by empty lines.

## Features

- Replaces ';' with '|' for easier typing (esacpe "real" ; with backslash, won't be rendered in html)
- Adds a spec line (the second line after headers) if not present
- Aligns cells, respecting ":-", ":-:", "-:" spec markers
- Puts headers in bold
- Autoclears empty columns right
- Keeps alignment of | delimiters even when concealleval is > 0, i.e. the ** bold markers are concealled (shifting cell width by 2)
"""
from share import vimcmdr, ctx, vim, notify, buf

PH = '❗🟥'   # placeholder


def bold(s):
    if not s:
        return ''
    while not s[:2] == '**':
        s = '*' + s
    while not s[-2:] == '**':
        s += '*'
    return s


def cells(l, row, conce):
    """Builds the max widths into COLS, puts headers to bold"""
    l = l.strip()
    if not l:
        l = ' '
    if not l[0] == '|':
        l = '|' + l
    if not l[-1] == '|':
        l = l + '|'
    l = l.replace('\;', PH).replace(';', '|').replace(PH, '\;')
    l = l.split('|')
    l = [i.strip() for i in l]
    while not l[-2]:
        l.pop(-2)
    if row == 0:
        l = [bold(s) for s in l]
    [COLS.append(0) for i in range(len(COLS), len(l))]
    minus = 0
    if row == 0 and conce > 0:
        minus = 2
    for col in range(len(l)):
        COLS[col] = max(COLS[col], len(l[col]) - minus)
    return l


def strip(k, chars):
    for c in chars:
        k = k.replace(c, '')
    return k.strip()


def cols(l):
    return len(l.split('|'))


def fill(row, cols, nr):
    [row.append('') for i in range(len(row), len(COLS))]
    if nr == 1:
        row = ['-' if not i.strip() else i for i in row]
        row[0] = row[-1] = ''
    return row


COLS = []   # column width. Reset per run.


def cell(s, spec, col, conce):
    is_bold = s[:2] == '**' and s[-2:] == '**'
    L = COLS[col]
    if is_bold and conce > 0:
        L += 2
    if ':' not in spec[1:]:
        r = s.ljust(L)
    elif not spec[0] == ':':
        r = s.rjust(L)
    else:
        d = L - len(s)
        s1 = ' ' * int(d / 2)
        r = s1 + s + s1 + ((d % 2) * ' ')
    return r


def align(row, spec, conce):
    return [cell(row[col], spec[col], col, conce) for col in range(len(spec))]


def try_load(line, block, full_block, **kw):
    COLS.clear()
    conce = int(vim.eval('&conceallevel'))
    if not len(full_block) > 1:
        return
    added_spec = 0
    if any([l for l in full_block[1] if strip(l, '|;-:')]):
        full_block.insert(1, '|-|')
        added_spec = 1
    matrix = [cells(l, row, conce) for l, row in zip(full_block, range(len(full_block)))]
    matrix = [fill(l, len(COLS), j) for l, j in zip(matrix, range(len(matrix)))]

    # l = [align(matrix[0], matrix[1])]
    l = []
    # l.append(matrix[1])
    [l.append(align(matrix[i], matrix[1], conce)) for i in range(0, len(matrix))]
    offs, b, j = len(full_block) - len(block), buf(), ctx.L1 + added_spec
    for line in l:
        if j - offs == len(b):
            b.append('')
        b[j - offs] = ' | '.join(line)[1:-1]
        j += 1
