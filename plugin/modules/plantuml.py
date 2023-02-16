#!/usr/bin/env python
"""
# Plantuml

Aliases: uml, plant

Uses: {CMD}

## Syntax

uml
<multiline plantuml>
<emptyline>

- You can omit the @startuml
- Result in html comments, so that we can replace old after changes of source
- And also browser view does not fubar (we use unicode, not nice rendered there)
- MarkdownPreview WILL show the svgs 🥲

## Examples

### Complex

uml
'hide footbox
participant "Bob on\nseveral lines" as Bob
actor Alice
Bob -> Alice : hello
note right of Alice
  this is a note
end note
Alice -> Bob : Is it ok\nwith a message that is\non several lines?
note right
  This other note
  should work
  on several lines
end note
== This is a separation ==
Bob -> Last : Yes it works!
Last -> Last : working in progress
note left : this is\nanother note
Last --> Last : working in progress
Last --> Bob : done
opt dummy comment
  Bob -> Last : Error\nOn\nSeveral\nLine
  Last --> Bob : None
else
  Last --> Bob : None
  Last -> Bob : None
else other
  Last -> Bob : None
  note over Alice, Last
    This is a long note
    over Alice and Last
  end note
  Last -> Bob : None
  Last -> Bob : None
end

<!--
                                                  ┌─┐
                                                  ║"│
                                                  └┬┘
                    ┌─────────────┐               ┌┼┐
                    │Bob on       │                │             ┌────┐
                    │several lines│               ┌┴┐            │Last│
                    └──────┬──────┘              Alice           └─┬──┘
                           │        hello          │               │
                           │──────────────────────>│               │
                           │                       │               │
                           │                       │ ╔═════════════╧══╗
                           │                       │ ║this is a note ░║
                           │                       │ ╚═════════════╤══╝
                           │Is it ok               │ ╔═════════════╧════╗
                           │with a message that is │ ║This other note  ░║
                           │on several lines?      │ ║should work       ║
                           │<──────────────────────│ ║on several lines  ║
                           │                       │ ╚═════════════╤════╝
                           │                       │               │
                           │      ╔════════════════╧═════╗         │
═══════════════════════════╪══════╣ This is a separation ╠═════════╪═════════════════════════
                           │      ╚════════════════╤═════╝         │
                           │                       │               │
                           │            Yes it works!              │
                           │──────────────────────────────────────>│
                           │                       │               │
                           │                       ╔══════════════╗│────┐
                           │                       ║this is      ░║│    │ working in progress
                           │                       ║another note  ║│<───┘
                           │                       ╚══════════════╝│
                           │                       │               │─ ─ ┐
                           │                       │               │    | working in progress
                           │                       │               │< ─ ┘
                           │                       │               │
                           │                 done  │               │
                           │<─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │
                           │                       │               │
                           │                       │               │
          ╔══════╤═════════╪═══════════════════════╪═══════════════╪════════════╗
          ║ OPT  │  dummy comment                  │               │            ║
          ╟──────┘         │                       │               │            ║
          ║                │               Error   │               │            ║
          ║                │               On      │               │            ║
          ║                │               Several │               │            ║
          ║                │               Line    │               │            ║
          ║                │──────────────────────────────────────>│            ║
          ║                │                       │               │            ║
          ║                │                 None  │               │            ║
          ║                │<─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │            ║
          ╠════════════════╪═══════════════════════╪═══════════════╪════════════╣
          ║                │                       │               │            ║
          ║                │                 None  │               │            ║
          ║                │<─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │            ║
          ║                │                       │               │            ║
          ║                │                 None  │               │            ║
          ║                │<──────────────────────────────────────│            ║
          ╠════════════════╪═══════════════════════╪═══════════════╪════════════╣
          ║ [other]        │                       │               │            ║
          ║                │                 None  │               │            ║
          ║                │<──────────────────────────────────────│            ║
          ║                │                       │               │            ║
          ║                │                   ╔═══╧═══════════════╧═══╗        ║
          ║                │                   ║This is a long note   ░║        ║
          ║                │                   ║over Alice and Last    ║        ║
          ║                │                   ╚═══╤═══════════════╤═══╝        ║
          ║                │                 None  │               │            ║
          ║                │<──────────────────────────────────────│            ║
          ║                │                       │               │            ║
          ║                │                 None  │               │            ║
          ║                │<──────────────────────────────────────│            ║
          ╚════════════════╪═══════════════════════╪═══════════════╪════════════╝
                    ┌──────┴──────┐              Alice           ┌─┴──┐
                    │Bob on       │               ┌─┐            │Last│
                    │several lines│               ║"│            └────┘
                    └─────────────┘               └┬┘
                                                  ┌┼┐
                                                   │
                                                  ┌┴┐

-->

### Roles

uml
participant Foo [
        Title
        "Sub Title"
        ]
actor       Actor       as Foo1
boundary    Boundary    as Foo2
control     Control     as Foo3
entity      Entity      as Foo4
database    Database    as Foo5
collections Collections as Foo6
queue       Queue       as Foo7
Foo->Foo1: sig

<!--
                              ┌─┐                                                                       ,.-^^-._
                              ║"│                                                                      |-.____.-|
                              └┬┘                                                                      |        |
     ┌───────────┐            ┌┼┐              |   ,-.                                                 |        |
     │Title      │             │               +--{   )          ┌───────┐          ┌──────┐           |        |         ┌───────────┐          ┌─────┐
     │"Sub Title"│            ┌┴┐              |   `-'           │Control│          │Entity│           '-.____.-'         │Collections│          │Queue│
     └─────┬─────┘           Actor            Boundary           └───────┘          └──────┘           Database           └───────────┘          └─────┘
           │       sig         │                 │                   │                 │                  │                     │                   │
           │──────────────────>│                 │                   │                 │                  │                     │                   │
     ┌─────┴─────┐           Actor            Boundary           ┌───────┐          ┌──────┐           Database           ┌───────────┐          ┌─────┐
     │Title      │            ┌─┐              |   ,-.           │Control│          │Entity│            ,.-^^-._          │Collections│          │Queue│
     │"Sub Title"│            ║"│              +--{   )          └───────┘          └──────┘           |-.____.-|         └───────────┘          └─────┘
     └───────────┘            └┬┘              |   `-'                                                 |        |
                              ┌┼┐                                                                      |        |
                               │                                                                       |        |
                              ┌┴┐                                                                      '-.____.-'

-->


-
"""


import json
from requests import post
import os
from share import notify, ctx, cli_mode, uid, vimcmd, BL_SQR
from share import delete_cur_line, read_file, write_file, unlink_if


exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

# CMD = 'echo -e "{spec}" | plantuml -syntax -pipe -tutxt'
# CMD = 'plantuml -tutxt "{fn}" 2>&1'
SERVER = 'https://kroki.io/'


def buf():
    return ctx.src_buf


def try_help():
    b = buf()
    l = b[ctx.L1 - 1].strip()
    # if we have a next line and tihs is not -h: draw block
    if l in {'uml', 'plant', 'plantuml'} and b[ctx.L1].strip():
        return try_load('', line='')
    s = __doc__.format(CMD=SERVER)
    return s


def render(spec, offs):
    """we go via file, better for e.g. \n in source"""
    spec = spec.strip()
    for k in '@startuml', '@enduml':
        spec = spec.replace(k, '')
    spec = f'@startuml\n{spec}\n@enduml\n'
    fn = f'/tmp/vpe_uml_{uid}'   # no dots
    d = {'diagram_source': spec, 'diagram_type': 'plantuml', 'output_format': 'utxt'}
    s = post(SERVER, data=json.dumps(d)).text
    s = f'\n<!--\n{s}\n-->\n'
    write_file(fn, s)
    return vimcmd(f'.{offs}read {fn}')


def try_load(s: str = '', line='vpe'):
    block, nr, b = [], ctx.L1, buf()
    for nr in range(ctx.L1, len(b)):
        l = b[nr].strip()
        if not l or l == '-':
            break
        block.append(l)
    delr = delete_old_chart_following(nr)
    if delr:
        start, end = delr

    lold = len(b)
    render('\n'.join(block), len(block))
    diff = len(b) - lold
    if delr:
        vimcmd(f'{start+diff},{end+diff}d')


def delete_old_chart_following(nr):
    b = buf()
    if len(b) < nr + 2:
        return
    start, end = 0, 0
    for nr in range(nr, min(len(b), nr + 4)):
        l = b[nr].strip()
        if not l:
            continue
        if l == '<!--':
            start = nr + 1
            for nr in range(nr, len(b)):
                if b[nr].rstrip() == '-->':
                    end = nr + 1
                    return start, end


L = '['
R = ']'
