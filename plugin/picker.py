import time
from share import ctx, notify, vim, here, read_file, uid, exists, import_module, all_mods
from share import add_lines
import os

fn_picker_result = f'/tmp/picker.result.{uid}'


def make_picker(c=[0]):
    p = c[0]
    if p:
        return p
    # os.unlink(fn_fifo) if exists(fn_fifo) else 0
    # os.mkfifo(fn_fifo)
    T = read_file(here + '/assets/lua_picker')
    vim.exec_lua(T)
    p = c[0] = vim.lua._picker
    return p


def pickers(c=[0]):
    p = c[0]
    if p:
        return p
    l = os.listdir(here + '/modules/pickermods')
    l = c[0] = sorted([i[:-3] for i in l if i.endswith('.py')])
    return l


class S:
    last_picker = None


def process_result(txt):
    modn = S.last_picker = read_file(fn_picker_result)
    os.unlink(fn_picker_result)
    if not all_mods.get(modn):
        notify(msg=f'importing {modn}')
        #  show any exception in vim:
        all_mods[modn] = import_module(f'modules.pickermods.{modn}')
    mod = all_mods[modn]
    res = mod.from_picker(txt)
    lines = res['lines']
    add_lines(lines, offs=0)


def show_action_picker():
    txt = '\n'.join(ctx.SEL)
    txt = txt or ctx.W
    if exists(fn_picker_result):
        notify('foo', str(txt))
        return process_result(txt)
    title = txt.split('\n', 1)[0] + '...' if '\n' in txt else txt
    p = make_picker()
    l = list(pickers())
    if S.last_picker:
        l.remove(S.last_picker)
        l.insert(0, S.last_picker)
    p.show(title, l, fn_picker_result)

    # time.sleep(3)
    # notify('open')
    # with open(fn_fifo, 'w') as fd:
    #     s = fd.read()
    #
    # notify('onde', str(s))
