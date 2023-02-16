#!/usr/bin/env python
"""
# Plantuml

Aliases: uml, plant

Uses: {CMD}

# Syntax


uml
<multiline plantuml spec>
<empty line>


## Examples

uml
participant Participant as Foo
actor       Actor       as Foo1
boundary    Boundary    as Foo2
control     Control     as Foo3
entity      Entity      as Foo4
database    Database    as Foo5
collections Collections as Foo6
queue       Queue       as Foo7
Foo -> Foo1 : To actor 
Foo -> Foo2 : To boundary
Foo -> Foo3 : To control
Foo -> Foo4 : To entity
Foo -> Foo5 : To database
Foo -> Foo6 : To collections
Foo -> Foo7: To queue

Result:
                              ┌─┐                                                                       ,.-^^-._                                        
                              ║"│                                                                      |-.____.-|                                       
                              └┬┘                                                                      |        |                                       
                              ┌┼┐              |   ,-.                                                 |        |                                       
     ┌───────────┐             │               +--{   )          ┌───────┐          ┌──────┐           |        |         ┌───────────┐          ┌─────┐
     │Participant│            ┌┴┐              |   `-'           │Control│          │Entity│           '-.____.-'         │Collections│          │Queue│
     └─────┬─────┘           Actor            Boundary           └───────┘          └──────┘           Database           └───────────┘          └─────┘
           │     To actor      │                 │                   │                 │                  │                     │                   │   
           │──────────────────>│                 │                   │                 │                  │                     │                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │            To boundary              │                   │                 │                  │                     │                   │   
           │────────────────────────────────────>│                   │                 │                  │                     │                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │                   │   To control    │                   │                 │                  │                     │                   │   
           │────────────────────────────────────────────────────────>│                 │                  │                     │                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │                   │            To entity                │                 │                  │                     │                   │   
           │──────────────────────────────────────────────────────────────────────────>│                  │                     │                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │                   │                 │   To database     │                 │                  │                     │                   │   
           │─────────────────────────────────────────────────────────────────────────────────────────────>│                     │                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │                   │                 │            To collections           │                  │                     │                   │   
           │───────────────────────────────────────────────────────────────────────────────────────────────────────────────────>│                   │   
           │                   │                 │                   │                 │                  │                     │                   │   
           │                   │                 │                   │     To queue    │                  │                     │                   │   
           │───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────>│   
     ┌─────┴─────┐           Actor            Boundary           ┌───────┐          ┌──────┐           Database           ┌───────────┐          ┌─────┐
     │Participant│            ┌─┐              |   ,-.           │Control│          │Entity│            ,.-^^-._          │Collections│          │Queue│
     └───────────┘            ║"│              +--{   )          └───────┘          └──────┘           |-.____.-|         └───────────┘          └─────┘
                              └┬┘              |   `-'                                                 |        |                                       
                              ┌┼┐                                                                      |        |                                       
                               │                                                                       |        |                                       
                              ┌┴┐                                                                      '-.____.-'                                       

 

"""

import os
from share import notify, ctx, cli_mode, uid, vimcmd, BL_SQR
from share import delete_cur_line


exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

# CMD = 'echo -e "{spec}" | plantuml -syntax -pipe -tutxt'
CMD = 'echo -e "{spec}" | plantuml -pipe -tutxt'


def buf():
    return ctx.src_buf


def try_help():
    b = buf()
    l = b[ctx.L1 - 1].strip()
    # if we have a next line and tihs is not -h: draw block
    if l in {'uml', 'plant', 'plantuml'} and b[ctx.L1].strip():
        return try_load('', line='')
    s = __doc__.format(CMD=CMD)
    return s


def render(spec, offs):
    fn = f'/tmp/vpe.uml.{uid}'
    cmd = CMD.format(spec=spec)
    os.system(f'echo -e "" > "{fn}"')
    os.system(f'{cmd} >> {fn} 2>>{fn}')
    return vimcmd(f'.{offs}read {fn}')


def try_load(s: str = '', line='vpe'):
    block, nr, b = [], ctx.L1, buf()
    for nr in range(ctx.L1, len(b)):
        l = b[nr]
        if not l.strip():
            break
        block.append(l)
    render('\n'.join(block), len(block))


L = '['
R = ']'
