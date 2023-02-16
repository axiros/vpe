#!/usr/bin/env python
"""
# Graph Easy

Alias: ge

Uses: {CMD}

## Syntax

### Single Line

ge <words>

In the single line version, the line will be replaced with result

### Multi Line

ge
<multiline graph easy spec>
<empty line>


You may omit the brackets. But you need the spaces!


## Examples

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
"""

import os
from share import notify, ctx, cli_mode, uid, vimcmd, BL_SQR
from share import delete_cur_line


exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

CMD = 'echo -e "{spec}" | graph-easy --as=boxart'


def buf():
    return ctx.src_buf


def try_help():
    b = buf()
    l = b[ctx.L1 - 1].strip()
    # if we have a next line and tihs is not -h: draw block
    if l == 'ge' or l == 'grapheasy' and b[ctx.L1].strip():
        return try_load('', line='')
    s = __doc__.format(CMD=CMD)
    return s


def render(spec, offs):
    fn = f'/tmp/vpe.ge.{uid}'
    spec = f'[{spec}]' if not spec[0] == BL_SQR else spec
    cmd = CMD.format(spec=spec)
    os.system(f'echo -e "" > "{fn}"')
    os.system(f'{cmd} >> {fn} 2>>{fn}')
    return vimcmd(f'.{offs}read {fn}')


def try_load(s: str = '', line='vpe'):
    if line.strip():
        # single line version:
        delete_cur_line()
        return render(line, -1)

    block, nr, b = [], ctx.L1, buf()
    for nr in range(ctx.L1, len(b)):
        l = b[nr]
        if not l.strip():
            break
        l1 = fmt(l)
        b[nr] = l1
        block.append(l1)
    render('\n'.join(block), len(block))


def fmt(line, starts='-.=<', ends='>>'):
    """convenience, omit brakets:
    foo - x -> bar to [foo] - x -> [bar]
    """
    r = []
    line = line.strip()
    if not line:
        return ''
    inarrw = False
    if not line[0] == L:
        line = L + line
    line = [c for c in line]
    while line:
        c = line.pop(0)
        if not inarrw and c in starts:
            inarrw = True
            if r[-2] != R:
                r.insert(-1, R)

        elif inarrw and c in ends:
            inarrw = False
            if line[1] != L:
                line.insert(1, L)
        r.append(c)
    if not r[-1] in [R, '}']:
        r.append(R)
    return ''.join(r)


L = '['
R = ']'
p = fmt('B - x -> A')
