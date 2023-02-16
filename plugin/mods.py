from share import (
    uid,
    os,
    sys,
    here,
    exists,
    setitem,
    read_file,
    ctx,
    notify,
    import_module,
    lib,
)

# -------------------------------------------------------------------------------------------- "Modules"
d_vpe = f'/tmp/vpe.{uid}'
d_user = f'{os.environ["HOME"]}/.config/vpe'
for d in [d_vpe, here, d_user]:
    if exists(d) and d not in sys.path:
        sys.path.insert(0, d)
        os.makedirs(d, exist_ok=True)

all_mods = {}


def refresh_known_mods():
    for D in here, d_user:
        d = D + '/modules'
        if exists(d):
            [setitem(all_mods, k[:-3], None) for k in os.listdir(d) if k.endswith('.py')]


refresh_known_mods()


def try_module(line):
    line = line.strip()
    # Currently only about swagger defs:
    if not line:
        line = 'help'
    # special case: ":!ls -lta" -> "colon !ls -lta"
    if line[0] == ':':
        line = f'cmd {line[1:]}'
    modn = line.split(' ')[0]
    if modn not in all_mods:
        return False
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
        all_mods[modn] = import_module(f'modules.{modn}')
    mod = ctx.mod = all_mods[modn]
    if not line.strip() or '-h' in line or '--help' in line:
        m = f'No help available for module {modn}'
        h = getattr(mod, 'try_help', getattr(mod, '__doc__', '') or m)
        l = h() if callable(h) else h
        m = {'lines': l, ':clear': True, ':ft': 'markdown', ':nofmt': True}
        return m if isinstance(l, str) else l
    h = {'http', 'https'}
    s = read_file(line)
    if not s and line.split(':', 1)[0] in h:   # and url.endswith('.json'):
        s = lib('requests').get(line).text
    r = mod.try_load(s, line=line)
    return r
