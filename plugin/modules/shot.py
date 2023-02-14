#!/usr/bin/env python

import os
from share import notify, ctx, cli_mode
from pathlib import Path

exists, dirname, abspath = os.path.exists, os.path.dirname, os.path.abspath


def pth_join(dir, fn):
    return str(Path(dir).joinpath(Path(fn)))


def try_load(s: str = '', line='vpe'):
    """s the content of a swagger definition file"""
    img = line.split()[0]
    # notify(img, dir(ctx), 10)
    if not img.endswith('.png'):
        img += '.png'
    D = os.getcwd() if cli_mode() else dirname(ctx.PTH)

    fni = pth_join(D, img)
    os.unlink(fni) if exists(fni) else 0
    os.makedirs(dirname(fni), exist_ok=True)
    cmd = f'scrot --freeze -s "{fni}"'
    if os.system(cmd):
        notify('drag shot', 'aborted')
        return
    msg = f'scrot', f'created {fni}'
    if not cli_mode():
        notify(msg)
        ctx.src_buf[ctx.L1 - 1] = f'![]({img})'
    else:
        print(msg)
