#!/usr/bin/env python
"""
# Making Screenshots

shot <filename>

Uses: {CMD}

# Example

`shot img/foo`

Will let you

- select a rectangle or window (double click) on the screen
- shoot it, using `scrot --freeze -s img/foo.png`
- delete `img/foo.png` if existing
- save the shot as at `img/foo.png`
- replace the line with `![](img/foo.png)`
"""

import os
from share import notify, ctx, cli_mode
from pathlib import Path

exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath

CMD = 'scrot --freeze -s "{filename}"'


def pth_join(dir, fn):
    return str(Path(dir).joinpath(Path(fn)))


def try_help():
    s = __doc__.format(CMD=CMD)
    return s


def try_load(line='vpe', **kw):
    """s the content of a swagger definition file"""
    img = line.split()[0]
    # notify(img, dir(ctx), 10)
    if not img.endswith('.png'):
        img += '.png'
    D = os.getcwd() if cli_mode() else dirname(ctx.PTH)

    fni = pth_join(D, img)
    os.unlink(fni) if exists(fni) else 0
    os.makedirs(dirname(fni), exist_ok=True)
    cmd = CMD.format(filename=fni)
    if os.system(cmd):
        notify('drag shot', 'aborted')
        return
    msg = f'scrot', f'created {fni}'
    if not cli_mode():
        notify(msg)
        ctx.src_buf[ctx.L1 - 1] = f'![]({img})'
    else:
        print(msg)
