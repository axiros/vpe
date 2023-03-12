#!/usr/bin/env python
"""
# Plantuml

Aliases: uml, plant

Uses: {{CMD}}

## Syntax

uml [txt] [utxt]
<multiline plantuml>
<emptyline>

- You can omit the @startuml
- Result in html comments, so that we can replace old after changes of source
- And also browser view does not fubar (we use unicode, not nice rendered there)
- MarkdownPreview WILL show the svgs 🥲
- Use txt if you want to view in browser. Default is utxt (unicode)


## Examples

### Txt
uml txt
'hide footbox
participant "Bob on\nseveral lines" as Bob
actor Alice
Bob -> Alice : hello
note right of Alice
  this is a note
end note


<!--
                                ,-.                  
                                `-'                  
     ,-------------.            /|\                  
     |Bob on       |             |                   
     |several lines|            / \                  
     `------+------'           Alice                 
            |       hello        |                   
            |------------------->|                   
            |                    |                   
            |                    | ,--------------!. 
            |                    | |this is a note|_\
     ,------+------.           Alic`----------------'
     |Bob on       |            ,-.                  
     |several lines|            `-'                  
     `-------------'            /|\                  
                                 |                   
                                / \                  

-->


### Complex (utxt)

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


import zlib
import base64
import sys
import json
from requests import post, get
import os

from share import notify, ctx, cli_mode, uid, vimcmd, BL_SQR
from share import delete_cur_line, read_file, write_file, unlink_if
from share import get_this_and_block_after, buf, linekw, write_file_relative


exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

# CMD = 'echo -e "{spec}" | plantuml -syntax -pipe -tutxt'
# CMD = 'plantuml -tutxt "{fn}" 2>&1'
SERVER = os.environ.get('KROKI_SERVER', 'https://kroki.io/')
notify(SERVER)


def try_help():
    s = __doc__.replace('{{CMD}}', SERVER)
    return s


def srv(spec, fmt, bin=False):
    if fmt == 'svg':
        inl = os.environ.get('PLANTUML_HDR', '')
        if inl:
            spec = inl + '\n' + spec
    spec = f'@startuml\n{spec}\n@enduml'
    k = base64.urlsafe_b64encode(zlib.compress(spec.encode('utf-8'), 9)).decode('utf-8')
    # TODO: txt not working always utxt!?
    s = get(f'{SERVER}/plantuml/{fmt}/{k}')
    return s.text if not bin else s.content


def render(spec,  fmt, **kw):
    """we go via file, better for e.g. \n in source"""
    spec = spec.strip()
    for img_fmt in '@startuml', '@enduml':
        spec = spec.replace(img_fmt, '')
    s = srv(spec, fmt)
    ret = {'lines': s}
    for img_fmt in 'svg', 'png':
        img_kw = kw.get(img_fmt)
        if not img_kw:
            continue
        bin = True if img_fmt == 'png' else False
        img = srv(spec, img_fmt, bin=bin)
        if img_kw is True:
            # no filename -> inline them:
            if not bin:
                # we ahve the source ;-0:
                img = img.split('<!--', 1)[0] + '</svg>'
            else:
                data_uri = base64.b64encode(img).decode('utf-8')
                img = f'<img src="data:image/{img_fmt};base64,{data_uri}">'
            ret['block_append'] = img
        else:
            _, pth = write_file_relative(img_kw, img, ext=img_fmt)
            ret['block_append'] = f'![]({pth})'

    return ret


def try_load(line, block, upsert_below, **kw):
    fmt = 'utxt'
    if ' txt' in line:
        fmt = 'txt'
    kw = {k: linekw(line, k) for k in ['svg', 'png']}
    s = render('\n'.join(block), fmt=fmt, **kw)
    upsert_below(s)


L = '['
R = ']'

# vi:sw=4
