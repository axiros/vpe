#!/usr/bin/env python

"""
Tools to make use of python API.

API funcs are in Capitals. Currently only "Eval" -
evaluating selected python code.
"""
import traceback
from functools import partial as P
import time
import json
import os
import sys

from share import log, here, uid, read_file, ctx, is_, debug, notify, exists  # noqa
from share import clear_all, buf, add_or_switch_to_window  # noqa
from share import out, lib, BRKT, vim, vimcmd, BL_SQR  # noqa
from share import vimcmdr, add_lines  # noqa
from mods import refresh_known_mods, try_module, all_mods  # noqa
from vpe_macros import macros  # noqa

# ------------------------------------------------------------------------------------------------ Result Formatting


def check_print_wanted(state, want_state):
    def add_state(v, want=want_state):
        if not want:
            return v

        def hide(k, v):
            return k in {"__builtins__"} or hasattr(v, "__package__")

        r = [[k, v] for k, v in state.items() if not hide(k, v)]
        c = {k: v for k, v in r if callable(v)}
        a = {k: v for k, v in r if not callable(v)}
        return {
            "state": to_dict({"vars": a, "callables": c}),
            "result": v,
        }

    for k in formatters:
        v = state.pop(k, None)
        if v is not None:
            v = add_state(v)
            vs = formatters[k](v)
            return f"{k} = {vs}"
    clss = [k for k in state if not k[0] == "_" and k[0].upper() == k[0]]
    clss = [state[k] for k in clss if is_(state[k], type)]

    def check_cls(c):
        """class A: p= ... -> print p's value and delete the attr"""
        for k in formatters:
            v = getattr(c, k, None)
            if v is not None:
                delattr(c, k)
                vs = formatters[k](v)
                return f"{c.__name__} = {vs}"

    for c in clss:
        v = check_cls(c)
        if v:
            v = add_state(v)
            return str(v)
    if want_state:
        return f'p = {add_state("")}'


def to_dict(*a, **kw):
    """Try to represent anything in valid python, avoiding tons of lsp errors in the result window

    This is the place where we apply hide and filter
    filter='foo,bar,1': only return kvs which match foo OR bar. if 1 is contained: All lists are first item only
    hide='foo,bar': x out values for those
    """
    d = _to_dict(*a, **kw)
    d = json.loads(json.dumps(d, default=str))
    nosh: str = ctx.state.get("hide", "")
    filter: str = ctx.state.get("filter", "")
    if not nosh and not filter:
        return d
    fnr = [0]

    def ns(d, nosh=nosh, filter=filter, fnr=fnr):
        f = [s.strip() for s in str(filter).split(",")] if filter else []
        list_1st = False
        if "1" in f:
            f.pop(f.index("1"))
            list_1st = True
        n = [s.strip() for s in nosh.split(",")]
        if is_(d, (list, tuple, set)):
            ll = [ns(i) for i in d]
            if list_1st and ll:
                ll = [ll[0], f"...[{len(ll)} items]"]
            return type(d)(ll)
        if is_(d, dict):
            r = {}
            for k, v in d.items():
                s = f"{k}{v}"
                if f and not any([i for i in f if i in s]):
                    fnr[0] += 1
                    continue
                if any([i for i in n if i in k]):
                    v = "xxx"
                else:
                    v = ns(v)
                r[k] = v
            return r
        return d

    r = ns(d)
    if fnr[0]:
        ctx.docs.append(f"# {fnr[0]} keys filtered, matching [{filter}]")
    return r


def _to_dict(obj, depth=0, maxd=5, have=None):
    depth += 1
    if depth > maxd:
        return str(obj)
    if is_(obj, str) and obj and obj.lstrip()[0] in BRKT:
        try:
            obj = json.loads(obj)
        except Exception:
            pass

    if is_(obj, (dict, set, list, int, float, bool, str)):
        return obj
    have = set() if have is None else have
    try:
        if obj in have:
            return str(obj)
        have.add(obj)
    except Exception:
        return str(obj)
    if callable(obj):
        return str(obj)
    r = {}
    for k in dir(obj):
        if not k[0] == "_":
            v = getattr(obj, k)
            if not callable(v):
                r[k] = _to_dict(v, depth, have=have)
    return r


formatters = {"p": to_dict}
for k in range(1, 6):
    formatters[f"p{k}"] = P(to_dict, maxd=k)


def to_y(o):
    d = to_dict(o)
    y = lib("yaml").safe_dump(d, default_flow_style=False)
    return f'''"""
{y}\n"""
    '''


formatters["y"] = to_y


def into_src_buffer(sb, lines):
    """sometimes we modify the source buffer. macros, swagger, ..."""
    if isinstance(lines, str):
        lines = lines.strip().splitlines()
    for l in lines:
        l1 = l.strip()
        if l1.startswith("vim:"):
            vimcmd(f"{len(sb)}j")
            vimcmd(l1.split("vim:", 1)[1].strip())
        else:
            sb.append(l)


def find_directive_in_header_and_footer(buf, ctx, directive, check_lines=10):
    if not ctx.on_any:
        return  # disabled support
    L = len(buf)
    if L < 5:
        return
    for off, l in [[1, 0], [-1, L - 1]]:
        checked = 0
        while checked < check_lines and l > -1 and l < L:
            if directive in buf[l] and (l + 1) not in ctx.executed_lines:
                return l + 1
            l += off
            if l < 0 or l > L - 1:
                break
            if not buf[l].strip():
                continue
            checked += 1


def fn_dir_of_file():
    fnf = vim.eval("expand('%:p')")
    fnf = os.path.abspath(fnf)

    class here:
        fn = fnf
        here = os.path.dirname(fnf)

    return here


def SmartGoto():
    """
    2 modes - visual, then lines are set, we call use per line, then
    Else called on one line
    """

    b = vim.current.buffer
    import smart_goto

    if ctx.L2 > 0:
        for l in range(ctx.L1, ctx.L2 + 1):
            ctx.L = line = b[l - 1]
            # visual range in one line? google it:
            if ctx.L1 == ctx.L2:
                _, start = vim.eval("""getpos("'<")[1:2]""")
                _, end = vim.eval("""getpos("'>")[1:2]""")
                if start != end:
                    words = line[int(start) - 1 : int(end)]
                    words = smart_goto.google_search(words)
                    return browse(words)

            ctx.L1 = l
            if not line.strip():
                continue
            ctx.COL = ctx.L1
            ctx.L2 = -1
            SmartGoto()
        return

    try:
        # notify("fooadsfa", [ctx.W, ctx.L1])
        smart_goto.handle(ctx.COL - 1, ctx.W, ctx.L, ctx.L1 - 1, ctx.PTH)
    except smart_goto.Noop:
        pass
    except smart_goto.RunCmd as ex:
        os.system(ex.args[0])
    except smart_goto.Edit as ex:
        vim.command(f"edit {ex.args[0]}")
        cont = ex.args[1]
        if cont:
            b, ls = vim.current.buffer, cont.splitlines()
            if len(b) == 1 and not b[0]:
                b[0] = ls[0]
            else:
                b.append(ls[0])

            for l in ls[1:]:
                # special case: empty file
                vim.current.buffer.append(l)
    except smart_goto.Browse as ex:
        browse(ex.args[0])


def browse(lnk):
    browser = os.environ.get("BROWSER", "microsoft-edge")
    os.system('%s "%s" >/dev/null 2>/dev/null &' % (browser, lnk))


def Eval():
    """Called method when hotkey is pressed in vim"""
    # set by the vim plugin -> always emtpy at hotkey press

    if ctx.L2 < 0:
        ctx.L2 = ctx.L1

    src_buf = ctx.src_buf = vim.current.buffer
    if not ctx.executed_lines:
        ctx.original_line = ctx.L1
    ctx.executed_lines.append(ctx.L1)  # loop preventer, exec only once per ,r
    on_any = find_directive_in_header_and_footer(src_buf, ctx, ":vpe_on_any", 10)

    if on_any:
        ctx.L1 = ctx.L2 = on_any
        return Eval()

    filetype = ctx.filetype = vim.eval("&filetype")
    nrs = list(range(ctx.L1 - 1, ctx.L2))  # lines start with 1, buffer is a list -> 0
    # check if we are within a block and go up:
    # we do this only if there is no visual range selected
    show_help = clear_buffer = clear_help = False

    # for hotkey on single lines we evaluate a few convenience statements
    # and extend the selected range the top of the block:
    orig_line = src_buf[nrs[0]]
    post_generate = False
    # just hotkey on a single line?
    deindent = 0
    res_spec = None
    if len(nrs) == 1:
        # the most often calling case, ,r on a line
        # in general, if not special handling is wanted we move up until the py block starts, then go down:
        line = src_buf[nrs[0]].strip()
        if ":vpe " in line:
            line = ":" + line.split(":vpe ", 1)[1]
            # special case: md comment. know no other comment with end sep:
            if line.endswith("-->"):
                line = line.rsplit("-->", 1)[0].strip()

        # markdown code block?: go to stop fences if on start fences:
        if line.startswith("```") and not line.strip() == "```":
            # convenience, allowing ```py only
            if line.startswith("```py `"):
                src_buf[nrs[0]] = line.replace("```py ", "```python ")

            deindent = len(orig_line.rstrip()) - len(line)
            try:
                while not src_buf[nrs[-1] + 1].lstrip().startswith("```"):
                    nrs.append(nrs[-1] + 1)
            except Exception:
                pass

        else:
            # module? e.g. swagger?
            res_spec = try_module(line)
            if res_spec is None:
                return
            if res_spec is False:
                if line in macros:
                    # small chhunks of python. modules are bigger, that's the diff
                    vimcmd("delete")
                    vimcmd("delete")
                    v = macros[line]
                    into_src_buffer(src_buf, v)
                    clear_buffer = clear_help = True
                elif filetype == "python":
                    # move up in python files:
                    try:
                        while (src_buf[nrs[0]] + " ")[0] in {" ", "]", "}", ")"}:
                            nrs.insert(0, nrs[0] - 1)
                    except Exception:
                        pass
                    nrs = [nrs[0]]

    # if there is just one selected, we now take the whole block, i.e. move down:
    if len(nrs) == 1:
        try:
            while (src_buf[nrs[-1] + 1] + " ")[0] in {" ", "]", "}", ")"}:
                nrs.append(nrs[-1] + 1)
        except Exception:
            pass

    block = [src_buf[i][deindent:] for i in nrs]
    if block[0].startswith("```"):
        block[0] = "# " + block[0]

    # find statements like clear or doc:
    bs, docs, l1 = list(block), ctx.docs, []
    while bs:
        line = bs.pop()  # bottom to top
        line = line.strip()
        line = (line[1:] if line.startswith("#") else line).strip()
        if line.startswith(":cmt "):
            docs.insert(0, "# " + line.split(":cmt ", 1)[1].strip())
        elif line == ":doc":
            docs.insert(0, l1)
        l1 = line
    block = "\n".join(block).split(":stop", 1)[0]
    state = ctx.state
    ctx.state["always"] = ctx.state.get("always", {})

    wrap = doc_call = ""
    always = add_state = False
    if ":noalways" in block:
        ctx.state["always"].clear()

    if ":always" in block:
        always = True

    def is_set(key, alw=always, block=block, mod_res=res_spec):
        mod_res = {} if not isinstance(mod_res, dict) else mod_res
        a = ctx.state["always"]
        if key in a or key in block or key in mod_res:
            if alw:
                a[key] = True
            return True

    silent = here = False
    if is_set(":here"):
        here = True
    if is_set(":silent"):
        silent = True
    if is_set(":state"):
        add_state = True
    if is_set(":autodoc"):
        state["autodoc"] = True
    if is_set(":noautodoc"):
        state.pop("autodoc", 0)
    if is_set(":clear"):
        clear_buffer = True
    if is_set(":all"):
        all_ = "\n".join([src_buf[i] for i in range(0, len(src_buf))])
        exec(all_, state, state)
    if is_set(":wrap ") and "{}" in block.split(":wrap ", 1)[1]:
        wrap = block.split(":wrap ", 1)[1].split("\n", 1)[0].strip()
    if is_set(":doc"):
        doc_call = True
    if is_set(":single"):
        block = orig_line.strip()
        block = block[:-1] if block.strip().endswith(",") else block

    if wrap:
        block = wrap.replace("{}", block)
    dt = ""
    if not state:
        state.update(globals())

    res_buf = None
    if show_help:
        from vpe_help import vpe_help

        res_spec = vpe_help()
    elif clear_help:
        res_spec = {"lines": ""}
    else:
        # no mod res?
        if not res_spec:

            class vpe:
                """access to us from execed code"""

                on_any = ctx.on_any
                ctx = ctx
                state = ctx.state
                vim = vim
                cmd = vimcmdr
                notify = notify
                fnd = fn_dir_of_file
                hlp = hlp
                # when new one added during vim run
                refresh_known_mods = refresh_known_mods

            try:
                t0 = time.time()
                state["vpe"] = vpe
                # with open(f'{d_vpe}/vpe_block.py', 'w') as fd:
                #     fd.write(block)
                #
                # def run(s=state):
                #     locals().update(state)
                #     globals().update(state)
                #     import vpe_block
                #
                # run()
                exec(block, state, state)
                state.pop("vpe")
                # postgen from assigns i guess not needed, he can directly run vim commands
                # but swagger  does deliver a post gen, which IS needed
                post_generate = state.get("post_generate", post_generate)
                dt = round(time.time() - t0, 2)
                ctx.on_any = vpe.on_any
            except Exception as ex:
                silent = False
                exc_type, exc_value, exc_tb = sys.exc_info()
                # this is intended for interactive docs, for others.
                l1 = find_directive_in_header_and_footer(src_buf, ctx, ":vpe_on_err", 10)
                if l1:
                    vim.current.buffer = src_buf
                    ctx.L1 = ctx.L2 = l1
                    return Eval()

                if len(ctx.W) > 0:
                    from picker import show_action_picker

                    return show_action_picker()

                # tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
                lines = [
                    f"{str(l).rjust(4)}{block[l]}" for l in range(min(999, len(block)))
                ]
                state["p"] = {
                    "Python Evaluation Error": {
                        "block": lines,
                        "word": [ctx.W, ctx.COL],
                        "ex": [type(ex), str(ex)],
                        "tb": [str(l).split(",") for l in traceback.format_tb(exc_tb)],
                    }
                }
            res_spec = check_print_wanted(state, add_state)  # just a string
            ge = state.get("ge")
            if isinstance(ge, str) and BL_SQR in ge:
                state.pop("ge")  # do not re-evaluate
                res_spec += "\n"
                res_spec += os.popen(f'echo -e "{ge}" | graph-easy --as boxart').read()
                res_spec += "\n"
    if doc_call or state.get("autodoc"):
        dt = f"[{dt}s]" if dt else ""
        [docs.insert(0, f"# {i} {dt}") for i in block.splitlines()]

    res_spec = res_spec or {"lines": ""}
    if isinstance(res_spec, str):
        res_spec = {"lines": res_spec, "post_generate": post_generate}
    lines = res_spec["lines"]

    if not silent:
        if not here:
            res_buf: list = add_or_switch_to_window("results.py", remember_cur=True)
            if clear_buffer or state.get("autodoc"):
                clear_all(buffer=res_buf)
            [res_buf.append(l) for l in docs]
            docs.clear()
            if lines:
                [res_buf.append(l) for l in lines.splitlines()]
            ft = res_spec.get(":ft")
            if ft:
                vimcmd(f"set filetype={ft}")
            vimcmd(":lua vim.notify=print")  # lsp errs all the time on fails
            ft = res_spec.get(":nofmt")
            if ft is not True:
                vimcmd(":silent lua vim.lsp.buf.format()")
            vimcmd(f"{len(res_buf)}j")

            res_buf = add_or_switch_to_window("previous")
        elif lines:
            vim.command(str(nrs[-1]))  # goto last line of block
            add_lines(lines)

        # vimcmd('delete') if clear_buffer else 0

    p = res_spec.get("post_generate")
    if p:
        p(src_buf, res_buf)


class hlp:
    def insert_between(begin, end, txt):
        """Inserts txt into the buffer, between begin and end, no matter what's in between (also multiline)"""

        for sr in "\\;\\\\", "/;\\/", "~;\~", "&;\&":
            txt = txt.replace(*sr.split(";"))
        txt = txt.replace("\n", "\r")

        repl = f"{begin}\(\_.*\){end}"
        vim.command(f"%s/{repl}/{begin}{txt}{end}/")

    def insert_between_html_cmt(begin, txt, end):
        """Inserts txt into the buffer, between begin and end, no matter what's in between (also multiline)"""


if __name__ == "__main__":
    # we are callable directly as well, executing what's supported in try_module
    os.environ["vpe_cli_mode"] = "true"
    debug, a = True, sys.argv
    if len(a) < 2:
        print("Call me with <module name> [args].")
        print(" Modules: {list(all_mods.keys())}")
        sys.exit(1)
    # must work with a line in vim anyway so combine:
    res = try_module(" ".join(sys.argv[1:]))
    if isinstance(res, str):
        sys.exit(print(res))
    f = getattr(ctx.mod, "cli_post", 0)
    if not sys.stdout.isatty() or not f:
        if res:
            sys.exit(print(res["lines"]))
    if f:
        f(res)
