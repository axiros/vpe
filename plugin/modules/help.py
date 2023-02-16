from vpe_macros import help as macro_help
from share import add_or_switch_to_window, ctx, result_win_showing, here, dirname
from mods import all_mods

try:
    import vim

    vim.command
except Exception:
    vim = None


H1 = """
# VPE Help
[Full help][readme] (,g on word readme)

# Default Operation
- Hotkey on a line or visual range => Tried execution as python.
- If `p` or `y` are assigned, their values are printed
- Code in md fences (py understood as lang): Whole md block evaluated

# Modules
---

{modules}

---
Help: Hotkey on module name

# Macros
{macro_help}

----
[readme]: {readme}
"""


def try_load(*a, **kw):
    if result_win_showing():
        add_or_switch_to_window('results.py', remember_cur=True)
        vim.command('bd')
        return
    m = dict(
        modules='\n'.join([f'{k}' for k in sorted(all_mods)]),
        macro_help=macro_help(),
        readme=dirname(here) + '/README.md',
    )
    return H1.format(**m).strip()


try_help = try_load
