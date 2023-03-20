from share import (
    uid,
    buf,
    os,
    sys,
    here,
    exists,
    setitem,
    read_file,
    ctx,
    notify,
    import_module,
    cli_mode,
    lib,
    get_this_and_block_after,
    vimcmd,
    all_mods,
)
from inspect import signature

# -------------------------------------------------------------------------------------------- "Modules"
d_vpe = f'/tmp/vpe.{uid}'
d_user = f'{os.environ["HOME"]}/.config/vpe'
for d in [d_vpe, here, d_user]:
    if exists(d) and d not in sys.path:
        sys.path.insert(0, d)
        os.makedirs(d, exist_ok=True)


def refresh_known_mods():
    for D in here, d_user:
        d = D + '/modules'
        if exists(d):
            [setitem(all_mods, k[:-3], None) for k in os.listdir(d) if k.endswith('.py')]


refresh_known_mods()

SEPS = [['<!--', '-->']]
[SEPS.append([s, s]) for s in ('"', '`', "'")]


def starts_with_sep(line):
    for i in SEPS:
        if line.startswith(i[0]):
            return i
    return ['', '']


# due to how mdtable currently works, the alias *has* to be single pipe. 'leo' does not need a mod, works like this
# with a `leo` cmd available:
aliases = {
    '|': 'mdtable ',
    ':': '_cmd ',
    'leo ': '_cmd !leo ',
    'tr ': 'translate ',
    'oai ': 'openai ',
}


def try_module(line):
    """line where ,r was pressed

    <module name> [args]

    [sep]<module name> [args]

    [sep]
    <module name> [args]

    Args may contain directives, e.g. after  # : example: "google foo # :here"
    Modules may return those directives as well, i.e. always: here

    Help we deliver
    - for vpe when line is completly empty.
    - for module when - h in args(some modules also return help when they need an arg)

    For the modules we deliver:
    Their block, which is bounded by - -> if line or previous line start with <!--
    Else: By first empty line

    Also we try deliver next block, for overwrites.


    """
    full_line = line
    sep = starts_with_sep(line)
    line = line[len(sep[0]):]
    if not sep and not cli_mode() and ctx.L1 > 1:
        sep = starts_with_sep(buf()[ctx.L1 - 2])

    line = line.strip()
    if not line:
        line = 'help'   # call help on empty

    # special case: ":!ls -lta" -> "_cmd !ls -lta"
    for k in aliases:
        if line.startswith(k):
            line = aliases[k] + line[len(k):]
    # if line[0] in aliases: line = aliases[line[0]] + ' ' + line[1:]
    modn = line.split(' ')[0]
    if modn not in all_mods:
        if ctx.prev_mod_line:
            psep, pl1, pl = ctx.prev_mod_line
            b = buf()
            # unchanged?
            if psep and b[pl1 - 1] == pl and ctx.L1 > pl1 and ctx.L1 - pl1 < 100:
                esep, is_below = dict(SEPS)[psep], False
                for k in range(pl1, ctx.L1):
                    if b[k].startswith(esep):
                        is_below = True
                if not is_below:
                    vimcmd(str(pl1 - ctx.L1))
                    line, ctx.L1 = pl, pl1
                    return try_module(line)
        ctx.prev_mod_line = False
        return False

    # directives off:
    line = line.rsplit('#', 1)[0]

    # this is a conventional feat: enrich the state beforehand:
    # see e.g. examples hetzner
    s = read_file('./mods.py')
    if s:
        m = {}
        exec(s, m, m)
        ctx.state.update(m)

    line = line.split(modn, 1)[1].strip()
    if not all_mods.get(modn):
        notify(msg=f'importing {modn}')
        #  show any exception in vim:
        all_mods[modn] = import_module(f'modules.{modn}')

    mod = ctx.mod = all_mods[modn]
    # help on -h --help OR just the module name with no seps involved:
    if (not sep[0] and not line.strip()) or ('-h' in line or '--help' in line):
        m = f'No help available for module {modn}'
        h = getattr(mod, 'try_help', getattr(mod, '__doc__', '') or m)
        l = h() if callable(h) else h
        m = {'lines': l, ':clear': True, ':ft': 'markdown', ':nofmt': True}
        return m if isinstance(l, str) else l
    params = signature(mod.try_load).parameters
    if 'block' in params or 'full_block' in params:
        # get the full block, mod may need it:
        f = get_this_and_block_after
        b, upsert_below, full_block = f(sep=sep[0], mod=mod, seps=SEPS, wanted=params)
    else:
        b, upsert_below, full_block = False, False, False
    r = mod.try_load(
        line=line,
        full_line=full_line,
        block=b,
        upsert_below=upsert_below,
        full_block=full_block,
    )
    ctx.prev_mod_line = None
    if b:
        ctx.prev_mod_line = sep[0], ctx.L1, full_line
    return r

    #
    # h = ['http://', 'https://']
    # if line.startswith(h[0]) or line.startswith(h[1]):
    #     s = lib('requests').get(line).text
    #
    # s = read_file(line)
    # if not s and line.split(':', 1)[0] in h:   # and url.endswith('.json'):
    #     s = lib('requests').get(line).text
