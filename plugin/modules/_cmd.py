#!/usr/bin/env python
"""
# Runs Vim Commands

Hotkey on a line starting with 'cmd ', ':' (or after ':vpe ' anywhere in a line)
=> vim evaluates the result into the buffer (as if typed in ex mode with colon).

Note: When line starts with `<!--`, we split off closing `-->`

## Syntax

❗🟥 Special treatment of `:` alias: No space required after the colon!

:<vim cmd>
cmd <vim cmd>
[any text] :vpe <cmd>

## Jump Commands

If the "vim cmd" is between slashes, we search the buffer and execute all matching lines.
Starting with `/gg` we search from beginning.

## Examples:

:lua P(require('telescope.mappings').default_mappings)
:hi
:map
:!ls -lta /
:history
:map
`<!-- :vpe !ls -lta -->`
:vpe /gg/@parser/ # executes all lines with "@parser" in them, e.g. markdown py code blocks
"""
from share import vimcmdr, ctx, vim, notify
import re
import vim_python_eval


def try_load(line, **kw):
    if not hasattr(vim, 'current'):
        return 'this module can only be run in vim'

    # this is a (vim) command or jump. Any directives behind ' # :'
    line = line.split(' # :', 1)[0]
    cmd = line
    # we support :/foo.bar/ -> jump to the line with 'foo?bar' in it and execute that one (handy in md)
    # :/gg/foo.bar/ searches form start
    if not (cmd and cmd[0] + cmd[-1] == '//'):
        return vimcmdr(cmd, silent=False, title=False)

    # realize jumps:
    search_start = ctx.L1
    if '/gg/' in cmd:
        cmd = cmd.replace('gg/', '')
        search_start = 1
    wind = vim.current.window
    have = set()
    match = '.*' + cmd[1:-1]
    for line in range(search_start, len(ctx.src_buf)):
        lstr = ctx.src_buf[line]
        # avoid hits on the jump declaration itself:
        if re.match(match, lstr) and cmd not in lstr:
            if lstr in have:
                continue
            have.add(lstr)
            ctx.L1 = ctx.L2 = line + 1
            vim_python_eval.ExecuteSelectedRange()
            vim.current.window = wind
