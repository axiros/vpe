import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + '/../plugin')
import mods   # noqa
import share   # noqa


class vim:
    def command(s):
        vim_cmds.append(s)

    class current:
        pass


share.vim = vim
vim_cmds = []


def setup_ctx(buffer_str_indented, L1):
    vim_cmds.clear()
    buffer = buffer_str_indented.replace('\n    ', '\n')
    share.ctx.src_buf = b = buffer.splitlines()
    vim.current.buffer = b
    share.ctx.L1 = L1


def run(b, cmd1=None, exp1=None):
    L1 = 1
    l = b.splitlines()
    while L1:
        if 'plantuml' in l[L1 - 1]:
            break
        L1 += 1
    setup_ctx(b, L1)
    res = mods.try_module(vim.current.buffer[L1 - 1])
    if not cmd1:
        return res
    s = share.read_file(vim_cmds[0].split(cmd1, 1)[1])
    if exp1:
        assert s == expect_1
    return s


def test_help():
    b = """
    plantuml
    a -> b: foo
    """
    res = run(b)
    assert 'This is a long note' in res['lines']


expect_1 = """
<!--
     ┌─┐          ┌─┐
     │a│          │b│
     └┬┘          └┬┘
      │    foo     │ 
      │───────────>│ 
     ┌┴┐          ┌┴┐
     │a│          │b│
     └─┘          └─┘
-->
"""


def test_parse_1():
    b = """
    <!-- plantuml
    a -> b: foo
    -->
    """
    run(b, cmd1='.2read ', exp1=expect_1)


def test_parse_2():
    b = """
    <!-- plantuml
    a -> b: foo
    -->"""
    run(b, cmd1='.2read ', exp1=expect_1)


def test_parse_3():
    b = """<!-- plantuml
    a -> b: foo
    -->"""
    run(b, cmd1='.2read ', exp1=expect_1)


def test_parse_4():
    b = """


    <!-- plantuml
    a -> b: foo
    -->"""
    run(b, cmd1='.2read ', exp1=expect_1)


def test_repl_1():
    b = """
    <!-- plantuml
    a -> b: foo
    -->

    <!--
    -->"""
    # res = run(b)
    share.ctx.original_line = 42
    run(b, cmd1='.2read ', exp1=expect_1)
    # the chart is in between now:
    assert vim_cmds[1] == '17,19d'
    assert vim_cmds[2] == '42'   # we jumped back
    assert share.ctx.prev_mod_line == ('<!--', 2, '<!-- plantuml')
