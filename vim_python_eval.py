#!/usr/bin/env python
"""
Tools to make use of python API.

API funcs are in Capitals. Currently only "ExecuteSelectedRange" - evaluating selected python code.

Most code is for swagger definition parsing, in namespace class "swagger".
"""

import sys, os, json, importlib, time, string
from functools import partial as P
from copy import deepcopy

debug = False
is_ = isinstance
try:
    import vim
except:
    # we can still parse swagger
    print('no vim api importable', file=sys.stderr)

out = P(print, file=sys.stderr)


class ctx:
    """Interface for the caller, setting us up
    Also transfers state over debug module reloads.
    """

    cur_cls: list = []
    cur_buffer = None
    prev_buffer = None
    L1 = 0   # selected first line in vim source buffer
    L2 = 0
    # transferred even over module reloads:
    state = {'_loaded_libs': {'yaml': 'pyyaml'}}
    docs = []


def read_file(fn):
    try:
        with open(fn) as fd:
            s = fd.read()
    except:
        s = ''
    return s


apostr = lambda s, a="'", b='"': f"'{s.replace(a, b)}'" if is_(s, str) else s


def lib(l, t={}):
    """we don't always require all libs"""
    c = ctx.state['_loaded_libs']
    v = c.get(l, l)
    if not is_(v, str):
        return v
    if not t.get(l):
        try:
            t[l] = True
            c[l] = importlib.import_module(l)
            return c[l]
        except:
            pass
    s = '\n' + '-' * 40 + '\n'
    print(f'{s}Please: pip install {l}{s}\n')


# Avoiding the infomous python indent bug for Treesitter...
BRKT = {'{', '['}


def log(s, **kw):
    """for debug only"""
    with open('/tmp/py_api', 'a') as fd:
        s = f'{s} {kw}\n'
        fd.write(s)


# ------------------------------------------------------------------------------------------------ "macros"
# some predefined code blocks, extensible by user:
m_r = """
if 'Sending requests to API endpoint':
    from requests import get, post, delete, patch
    from json import dumps
    from functools import partial
    headers = {'Content-Type': 'application/json'}
    Post = lambda url, data: post(url, data=data, headers=headers)

class R:
    # :clear
    # :cmt pastebin example
    url = 'http://httpbin.org/post'
    data = { "mydata": { "hello": "world" }}
    p = Post(url, data=data).text 
    # y = Post(url, data=data)

"""

m_rx = """

'Testing Reactive-X for Python'
import gevent

import rx as Rx
from rx import operators as rx  # noqa

# If you need subjects:
from rx import subject

# If you need a scheduler:
from rx.scheduler.eventloop import GEventScheduler  # noqa
GS = GEventScheduler(gevent)

# and an actual test:
s1 = Rx.from_([1, 2, 3])
s2 = Rx.from_(['a', 'b', 'c', 'd'])
s3 = Rx.from_(['A', 'B'])
p = []
s1.pipe(rx.combine_latest(s2, s3)).subscribe(lambda x: p.append(x))

"""

macros = {'r': m_r, 'rx': m_rx}
# custom ones:
fn_m = os.environ['HOME'] + '/.config/vpe/macros.py'
s = read_file(fn_m)
m = {}
if s:
    exec(s, m, m)
macros.update(m['macros'])


def help():
    """Display available macros"""
    r = 'Enter letter and hit evaluation hotkey on it:\n\n'
    for m, v in macros.items():
        v = '# ' + v.lstrip().split('\n', 1)[0].replace('if ', '')
        r += f'{m}: {v}\n'
    r += '\n\nResults you get by assigning "p" or "y" in code blocks.'
    return r


# ------------------------------------------------------------------------------------------------ Vim API tools


def clear_all(buffer):
    del buffer[0 : len(buffer)]


buf = lambda: vim.current.buffer
vimcmd = lambda cmd: vim.command(cmd)


def add_or_switch_to_window(buffername, remember_cur=False, b=None):
    """Create a split win, or, if present, switch to it
    Provides a remember feature to switch back using the convention name 'previous'
    """
    if buffername == 'previous':
        vim.current.window = ctx.prev_win
        return
    if remember_cur:
        ctx.prev_win = vim.current.window
    bid = vim.eval(f'bufwinnr("{buffername}")')
    if bid == '-1':
        vimcmd(f'rightbelow vsplit {buffername}')
        vimcmd(f'setlocal buftype=nofile nospell')
    else:
        vimcmd(f'{bid}wincmd w')
    return vim.current.buffer


# ------------------------------------------------------------------------------------------------ Result Formatting
def check_print_wanted(m):
    for k in formatters:
        v = m.pop(k, None)
        if v is not None:
            vs = formatters[k](v)
            return f'{k} = {vs}'
    clss = [k for k in m if not k[0] == '_' and k[0].upper() == k[0]]
    clss = [m[k] for k in clss if is_(m[k], type)]

    def check_cls(c):
        """class A: p= ... -> print p's value and delete the attr"""
        for k in formatters:
            v = getattr(c, k, None)
            if v is not None:
                delattr(c, k)
                vs = formatters[k](v)
                return f'{c.__name__} = {vs}'

    for c in clss:
        v = check_cls(c)
        if v:
            return v


def to_dict(*a, **kw):
    """Try to represent anything in valid python, avoiding tons of lsp errors in the result window

    This is the place where we apply hide and filter
    filter='foo,bar,1': only return kvs which match foo OR bar. if 1 is contained: All lists are first item only
    hide='foo,bar': x out values for those
    """
    d = _to_dict(*a, **kw)
    d = json.loads(json.dumps(d, default=str))
    nosh: str = ctx.state.get('hide', '')
    filter: str = ctx.state.get('filter', '')
    if not nosh and not filter:
        return d
    fnr = [0]

    def ns(d, nosh=nosh, filter=filter, fnr=fnr):
        f = [s.strip() for s in str(filter).split(',')] if filter else []
        list_1st = False
        if '1' in f:
            f.pop(f.index('1'))
            list_1st = True
        n = [s.strip() for s in nosh.split(',')]
        if is_(d, (list, tuple, set)):
            ll = [ns(i) for i in d]
            if list_1st and ll:
                ll = [ll[0], f'...[{len(ll)} items]']
            return type(d)(ll)
        if is_(d, dict):
            r = {}
            for k, v in d.items():
                s = f'{k}{v}'
                if f and not any([i for i in f if i in s]):
                    fnr[0] += 1
                    continue
                if any([i for i in n if i in k]):
                    v = 'xxx'
                else:
                    v = ns(v)
                r[k] = v
            return r
        return d

    r = ns(d)
    if fnr[0]:
        ctx.docs.append(f'# {fnr[0]} keys filtered, matching [{filter}]')
    return r


def _to_dict(obj, depth=0, maxd=5, have=None):
    depth += 1
    if depth > maxd:
        return str(obj)
    if is_(obj, str) and obj and obj.lstrip()[0] in BRKT:
        try:
            obj = json.loads(obj)
        except:
            pass

    if is_(obj, (dict, set, list, int, float, bool, str)):
        return obj
    have = set() if have is None else have
    try:
        if obj in have:
            return str(obj)
        have.add(obj)
    except Exception as ex:
        return str(obj)
    if callable(obj):
        return str(obj)
    r = {}
    for k in dir(obj):
        if not k[0] == '_':
            v = getattr(obj, k)
            if not callable(v):
                r[k] = _to_dict(v, depth, have=have)
    return r


formatters = {'p': to_dict}
for k in range(1, 6):
    formatters[f'p{k}'] = P(to_dict, maxd=k)


def to_y(o):
    d = to_dict(o)
    y = lib('yaml').safe_dump(d, default_flow_style=False)
    return f'''"""
{y}\n"""
    '''


formatters['y'] = to_y

deindent = lambda s, spec={}: s.replace(f'\n{" "*8}', '\n') % spec

# ------------------------------------------------------------------------------------------------ Being smart about one liners
pyallwd = set(string.digits + string.ascii_letters + '_')
# Currently only about swagger defs:
def try_load_file_or_url(url):
    s = read_file(url)
    h = {'http', 'https'}
    if not s and url.split(':', 1)[0] in h:   # and url.endswith('.json'):
        s = lib('requests').get(url).text
    return swagger.try_load(s, url=url)


class swagger:
    """namespace for all swagger handling related funcs"""

    icos = dict(put='🟧', post='🟪', get='🟩', delete='🟥', dflt='🟫')

    # nasty details: when params are named e.g. async we must convert to "async__", then replace before send
    forbidden_kw = {'async', 'for', 'if', 'while', 'from', 'import'}
    # path params. will be exposed globally
    pparams = {}
    # number of classes generated to that we can collapse after build:
    clses = 0
    # all definitions:
    definitions = {}
    # while in def we can't ref other defs, must put into lambdas:
    in_def_block = False
    now_datetime = time.strftime('%Y-%m-%d')
    now_time = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    if os.environ.get('testmode'):   # avoid test diffs
        now_datetime = '2020-12-12'
        now_time = '2020-12-12T%12:12:12Z'
    # the tooling:
    code = """
        # type: ignore
        '''
        %(title)s
        %(givenurl)s

        %(info)s
        '''
        %(pre_params)s
        # -

        class API:
            user, passw = '$user', '$password'
            host = '%(host)s'
            base = '%(basePath)s'
            hdrs = %(hdrs)s

        _PTHPARAMS_

        # fmt:off
        methods = lambda: ( # :clear :doc :eval file :exec single :wrap p = Tools.send({})
         _TOC_
        ) 
        # fmt:on


        """

    tools_code = """

        # ─────────────── Tools ─────────────────────
        import requests, json, functools, inspect, os

        class Tools:
            @staticmethod
            def build_req(meth):
                data, h, q = None, API.hdrs, {}
                g = lambda o, k, d=None: getattr(o, k, d)
                c = globals()[meth.__qualname__.split('.', 1)[0]]
                R = g(meth, 'R')
                if R:
                    h['Content-Type'] = m = g(R, '_mime', 'application/json')
                    if not 'form' in m and not 'json' in m and g(R, 'content'):
                        data = R.content
                    p = {a: g(R, a) for a in g(R, '_path', ())}
                    pth = c.pth.format(**p)
                    for a in g(R, '_query', ()):
                        v = g(R, a)
                        if v is not None:
                            q[a] = g(R, a)
                    b = g(R, 'body')
                    if b:
                        data = Tools.obj(b)
                    f = g(R, '_formData')
                    if f:
                        data = {k: Tools.obj(g(R, k)) for k in f}
                        data = data['form'] if f == ['form'] else data
                return meth.__name__, pth, q, data, h

            @staticmethod
            def obj(def_, is_=isinstance, g=getattr):
                if is_(def_, tuple):
                    return def_[0]
                if callable(def_):
                    if inspect.isfunction(def_):
                        def_ = def_()
                if is_(def_, str) and def_.startswith('obj:'):
                    def_ = getattr(Defs, def_[4:])
                if is_(def_, (float, int, bool, str)):
                    return def_
                obj = Tools.obj
                if is_(def_, list):
                    return [obj(def_[0])]
                if is_(def_, dict):
                    return {k: obj(v) for k, v in def_.items()}
                R = g(def_, 'R', 0)
                if R:
                    return obj(R)
                l = g(def_, '_attrs', [i for i in dir(def_) if not i[0] == '_'])
                return {k: obj(g(def_, k)) for k in l if not is_(g(def_, k), dict)}

            @staticmethod
            def send(meth, *args):
                if args:
                    meth = args[0]   # ico in line
                env = os.environ.get
                getenv = lambda v: env(v[1:], '') if (v and v[0] == '$') else v

                def repl(s, keyw={'for', 'async', 'from', 'if', 'import', 'while'}):
                    if isinstance(s, str):
                        for k in keyw:
                            s = s.replace(f'{k}__', k)
                    else:
                        s = json.loads(repl(json.dumps(s)))
                    return s

                # if '__user_id' in str(meth): breakpoint() # FIXME BREAKPOINT
                try:
                    methd, pth, params, data, h = Tools.build_req(meth)
                    host = f'{API.host}'
                    if not '://' in host:
                        host = 'https://' + host
                    url = repl(f'{host}{API.base}{pth}')
                    h = {k: getenv(v) for k, v in h.items()}
                    kw = {'params': params, 'headers': h, 'timeout': timeout}
                    if getenv(API.passw):
                        kw['auth'] = (getenv(API.user), getenv(API.passw))
                    if isinstance(data, (list, dict)):
                        kw['data'] = repl(data)
                    req = getattr(requests, methd)
                    if result == 0:   # no send
                        return [url, methd, kw]
                    if 'json' in h.get('Content-Type') and data is not None:
                        kw['data'] = json.dumps(kw['data'])
                    req = req(url, **kw)
                    if result == 3:
                        return req   # show all
                    r = {'status': req.status_code}
                    try:
                        r['resp'] = json.loads(req.text)
                    except:
                        r['resp'] = req.text
                except Exception as ex:
                    r = {'Exception': str(ex)}
                if result == 2:
                    r.update(dict(kw))
                    r['url'] = url
                return r


    """

    @staticmethod
    def repl_unallowed_pydef_chars(s):
        # seen this:
        # "ValueTuple[ListResultDto[FlexiformWithSubmitterNameAndTemplateNameDto],Int32]": {
        #   "type": "object",
        #   "properties": {
        #     "item1": {
        #       "$ref": "#/definitions/ListResultDto[FlexiformWithSubmitterNameAndTemplateNameDto]"
        return ''.join([c if c in pyallwd else '_' for c in s])

    @staticmethod
    def by_type(v: dict):
        if '$ref' in v:
            return 'ref', swagger.by_obj
        # sometimes missing:
        t = v.get('type', v.get('format', 'string'))
        if t == 'string':
            return t, swagger.by_str
        if 'int' in t:
            return t, swagger.by_int
        if 'bool' in t:
            return t, swagger.by_bool
        if 'number' in t:
            return t, swagger.by_number
        if 'arr' in t:
            return t, swagger.by_array
        if t == 'file':
            return t, swagger.by_file
        if t == 'object':
            swagger.by_obj
        if t == 'object':
            return t, swagger.by_obj
        return t, swagger.by_obj

    @staticmethod
    def by_obj(k, v, ex, descr):
        # https://stackoverflow.com/questions/46472543/specifying-multiple-types-for-additionalproperties-through-swagger-openapi?rq=1
        p = v.get('properties')
        a = v.get('additionalProperties')
        if p:
            d = []
            for k1, v1 in p.items():
                v2 = swagger.prop(k1, v1)[-1]
                if v2.startswith('R.'):
                    v2 = v2[2:]
                d.append(v2)
            d = 'dict(%s)' % ', '.join(d)
        elif a:
            d = '{}'
        else:
            d = swagger.get_ref(v)
            if not d:
                breakpoint()   # FIXME BREAKPOINT
        return ex or d, descr or k

    @staticmethod
    def by_int(k, v, ex, descr):
        return ex or v.get('default', 0), descr or k

    @staticmethod
    def by_number(k, v, ex, descr):
        return ex or v.get('default', 0.0), descr or k

    @staticmethod
    def by_str(k, v, ex, descr):
        f = v.get('format')
        if f == 'date-time':
            ex = ex or swagger.now_datetime
        elif f == 'date':
            ex = ex or swagger.now_time
        r = v.get('enum', ['str_dflt'])[0]
        r = apostr((ex or v.get('default', r)))
        r = r[1:-1] if r == "'str_dflt'" else r
        return r, descr or k

    @staticmethod
    def by_bool(k, v, ex, descr):
        return ex or v.get('default', True), descr or k

    @staticmethod
    def by_file(k, v, ex, descr):
        # TODO file upload not yet working, user must manually read in the content:
        return ex or v.get('default', "'~/my_file'"), descr or k

    @staticmethod
    def get_ref(i):
        r = i.get('$ref')
        if not r:
            return
        d = swagger.def_cls(r)
        if swagger.in_def_block:
            return f'lambda: Defs.{d}'
        return f'Defs.{swagger.definitions.get(r)}'

    @staticmethod
    def by_array(k, v, ex, descr):
        # if k == 'recordTypes': breakpoint()     # FIXME BREAKPOINT
        i = v['items']
        d = swagger.get_ref(i)
        if not d:
            if i.get('example'):
                d = i['example']
                # be robust against ill defined {'example': 'value of any type'}
                if is_(d, str) and (not d or d[0] not in {'"', "'"}):
                    d = f"'{d}'"
            else:
                d = swagger.by_type(i)[1](k, i, ex, descr)[0]
        d = v.get('default', f'[{d}]')
        r = ex or d
        sep = ''
        # given examples we simply take:
        if is_(r, list) and not ex:
            # https://swagger.io/docs/specification/2-0/describing-parameters/#query-parameters
            cf = v.get('collectionFormat', 'csv')
            if cf != 'multi':
                if cf == 'csv':
                    r, sep = ','.join(r), ','
                elif cf == 'pipes':
                    r, sep = '|'.join(r), '|'
                elif cf == 'tsv':
                    r, sep = '\t'.join(r), 'tab'
                elif cf == 'ssv':
                    r, sep = ' '.join(r), 'space'
        sep = f'sep: {sep}. ' if sep else ''
        return r, sep + (descr or k)

    @staticmethod
    def prop(k, v, no_ref=False):
        if not isinstance(v, dict):
            # schematics: '$response.body#/id'. not present in v3 it seems
            # only in response. so be... lazy:
            v = {'in': 'body', 'name': k, 'type': 'string', 'example': str(v)}
        else:
            v = dict(v)
        v.update(v.get('schema', {}))
        if not is_(v, dict):
            return [f'{k} = {apostr(v)}']
        t, cast = swagger.by_type(v)
        d = v.pop('description', '')
        r, d = cast(k, v, ex=v.get('example'), descr=d)
        v = v if v else ''
        if d and d != k:
            if is_(v, dict):
                v['descr'] = d
            else:
                v = [apostr(d), v]
        d = f'{k} = {v}'
        ctx.cur_cls.append(d)
        l = []
        d = ''
        if k in swagger.pparams and not no_ref:
            r = k
        cma = ',' if isinstance(r, dict) else ''
        l.append(f'R.{k} = {r}{cma}'.replace('\n', '\\n'))
        return l

    @staticmethod
    def def_cls(ref):
        return swagger.repl_unallowed_pydef_chars(ref[2:])

    @staticmethod
    def build_components(spec):
        """Setting up the Definitions class Tree"""
        debug and out('Building components and definitions')
        swagger.in_def_block = True
        r, i = ['class Defs:'], '    '
        add = r.append

        for n in sorted(swagger.definitions.keys()):
            # n like '#/components/links/UpdateUserById'
            d, parts = spec, n.split('/')[1:]
            while parts:
                part = parts.pop(0)
                d = d[part]
            debug and out('definition', n)
            # if n == 'IFormFile': breakpoint()   # FIXME BREAKPOINT
            N = swagger.definitions[n]
            d.pop('xml', 0)
            # Maybe we should gen those classes also for objects within methods?
            # try:
            #     assert d.pop('type') == 'object'
            # except Exception as ex:
            #     print('breakpoint set')
            #     breakpoint()
            #     keep_ctx = True
            props = d.pop('properties', d.pop('parameters', {}))
            add(f'{i}class {N}:')
            if N != n:
                add(f'{i}{i}"""{n}"""')
            ins = len(r)
            ctx.cur_cls = []
            if props:
                ctx.cur_cls.append(f'_attrs = {list(props.keys())}')
                for k, v in props.items():
                    if k in swagger.forbidden_kw:
                        k += '__'
                    debug and out('   ', n, 'prop', k)
                    for line in swagger.prop(k, v):
                        add(f'{i*2}{line}')
            elif not props and not d:
                add(f'{i}{i}"empty"')
            cl = ''
            if d:
                ind = 3
                for k, v in d.items():
                    if k == '$ref':
                        k = 'dollar_ref'
                    # add non relevant props, e.g. required with _ = ... after class:
                    cl += f'\n{i*ind}{k} = {apostr(v)}'
            cl = swagger.build_details_cls(2, cl)
            r.insert(ins, cl)
        swagger.in_def_block = False
        r = '\n'.join(r)
        r = swagger.repl_defs(r, 'lambda: ')
        return r

    @staticmethod
    def repl_defs(r, pre=''):
        for k, v in swagger.definitions.items():
            r = r.replace(f"{{'$ref': '{k}'}}", f'{pre}Defs.{v}')
            r = r.replace(f"'{k}'", f'{pre}Defs.{v}')
        return r

    @staticmethod
    def parse_infos_for_docstr(spec):
        i = spec.get('info', {})
        i['openapi'] = spec.get('openapi', i.get('swagger', '?'))
        spec['title'] = i.pop('title', 'Swagger API Tester')
        if not any([j for j in i.values() if is_(j, (dict, list))]):
            return json.dumps(list(i.values()))[1:-1].replace('"', '')
        return lib('yaml').safe_dump(i)

    @staticmethod
    def build_details_cls(ind, pre=''):
        C = ctx.cur_cls
        if not C and not pre:
            return ''
        i = '    ' * ind
        r = [f'{i}class R:']
        i += '    '
        if pre:
            r.append(f'{i}{pre.strip()}')
        [r.append(f'{i}{l}') for l in C]
        return '\n'.join(r)

    @staticmethod
    def get_host(spec, url):
        h = ctx.state.get('host')
        if h:
            return h
        h = spec.get('host', spec.get('servers', [{'url': '/'}])[0]['url'])
        if h.startswith('/'):
            if url.startswith('http'):
                r = url[:9] + url[9:].split('/', 1)[0]
                h = r + h
            else:
                h = 'http://127.0.0.1:8000' + h
        return h

    @staticmethod
    def try_load(s: str, url='n.a.'):
        """s the content of a swagger definition file"""
        s = s.encode().decode('utf-8-sig')
        if not s or (not 'swagger' in s and not 'openapi' in s):
            return
        try:
            if s.strip()[0] in BRKT:
                spec = json.loads(s)
            else:
                spec = lib('yaml').safe_load(s)
            assert isinstance(spec, dict)
        except:
            return
        # sp = mod.SwaggerParser(swagger_dict=d) # swagger parser did not cut it for us :-/
        # allows to predefine globals:
        spec['params'] = ctx.state.get('params', {})
        for p, v in spec['params'].items():
            swagger.pparams[p] = f'{p} = {apostr(v)}'
        spec['hdrs'] = ctx.state.get('hdrs', {})
        spec['givenurl'] = url
        spec['info'] = swagger.parse_infos_for_docstr(spec)
        spec['host'] = swagger.get_host(spec, url)
        spec['forbidden_kw'] = swagger.forbidden_kw

        if not spec.get('basePath'):
            spec['basePath'] = ''
        # fmt:off
        pp = {
            'hdrs'     : None,    # headers
            'hide'     : None,    # hide='foo,bar' =>  values for those keys are x-ed out
            'noicos'   : None,    # do not show the colored req method icons
            'params'   : None,    # dict of global params, in addition to path params parsed
            'sep'      : None,    # seperates lines in method list by this char
            'filter'   : None,    # only show keys/vals which match. '1': Show only first list item
            'result'   : 1,       # 0: Show only req, no API hit; 1: only result; 2 : both; 3 : full req object
            'str_dflt' : '',      # Sets default for all string params w/o an example
            'timeout'  : 5,       # Sets requests timeout
        }
        # fmt:on
        pp = [(k, ctx.state.get(k, pp[k])) for k in sorted(pp)]
        pp = [f'{k} = {apostr(v)}' for k, v in pp if v is not None]
        spec['pre_params'] = '\n'.join(pp)   # render them into src buffer
        r = deindent(swagger.code, spec)
        tools_cls = deindent(swagger.tools_code, spec)
        paths = spec['paths']

        def new_pparam(p, _=swagger.pparams):
            if p['name'] in _:
                return
            ctx.cur_cls = []
            v = swagger.prop(p['name'], p, no_ref=True)[-1]
            v = v.split('#', 1)[0].strip()   # comments differ => omit
            _[p['name']] = v

        def prepare_spec(methods, spec):
            """
            Walks the methods to
            - find path parameters, (will be global)
            - convert requestBody to swagger's params
            - find refs
            """
            for m in methods:
                #  "/users/{user_id}": method in schemathesis has top level params
                top_level_params = m.pop('parameters', [])
                for p1 in m.values():
                    params = p1['parameters'] = p1.get('parameters', [])
                    [params.insert(0, dict(f)) for f in top_level_params]
                    for p in params:
                        if p.get('in') == 'path':
                            new_pparam(p)
                    rb = p1.get('requestBody', {})
                    # cross ref to requestBody component:
                    ref = rb.get('$ref')
                    if ref:
                        m, parts = spec, ref.split('/')[1:]
                        while parts:
                            m = m[parts.pop(0)]
                        rb.update(deepcopy(m))
                    rb = rb.get('content')
                    if rb:
                        ct = ''
                        for f in [
                            'application/json',
                            'multipart/form-data',
                            'application/x-www-form-urlencoded',
                            #'application/octet-stream',
                        ]:
                            r = rb.pop(f, 0)
                            if r:
                                n = 'body' if 'json' in f else 'form'
                                i = 'body' if 'json' in f else 'formData'
                                r.update({'name': n, 'in': i})
                                ct = f
                                break
                        if not ct and rb:
                            # 'text/csv' or 'image/png' or 'application/octet-stream'
                            k = list(rb.keys())[0]
                            ct = k
                            r = {
                                'name': 'content',
                                'type': 'string',
                                'mime': k,
                                'in': 'mimetype',
                            }
                        if ct:
                            params.append(r)
                            p1['mime'] = ct

        prepare_spec(paths.values(), spec)

        refs = set()

        def find_refs(d, refs=refs):
            if is_(d, list):
                [find_refs(i) for i in d]
            if is_(d, dict):
                for k, v in d.items():
                    if k == '$ref':
                        swagger.definitions[v] = swagger.def_cls(v)
                    find_refs(v)

        find_refs(spec)
        if swagger.definitions:
            swagger.clses += 1
            r += swagger.build_components(spec)

        toc = []

        def extract_path_params(p):
            for k in swagger.pparams:
                p = p.replace('{%s}' % k, f'_{k}_')
            return p

        i = '    '
        pre = r
        r = ''
        for pth in paths:
            debug and out('path', pth)
            swagger.clses += 1
            P = paths[pth]
            p_orig = pth
            # '/pet/{petId}/uploadImage'
            p = extract_path_params(pth)
            pn = f'{p[1:].replace("/", "__")}'
            pn = swagger.repl_unallowed_pydef_chars(pn)
            r += f'\n\nclass {pn}:'
            r += f'\n{i}pth = "{p_orig}"'
            methods = paths[p_orig].keys()
            for m in methods:
                ctx.cur_cls = []
                # m = post, get, put, ...:
                debug and out(f'     {m}')
                if ctx.state.get('noicos'):
                    toc.append(f'{pn}.{m},')
                else:
                    ico = swagger.icos.get(m, swagger.icos['dflt'])
                    toc.append(f"'{ico}', {pn}.{m},")
                r += f'\n\n{i}class {m}:'
                pspec = P[m]
                params = pspec.pop('parameters', [])
                doc = f'{pspec.pop("description", "")} {pspec.pop("summary", "")}'
                if doc:
                    r += f'\n{i}{i}"""{doc}"""'
                if pspec:
                    ctx.cur_cls.append(f'_ = {pspec}')
                r += '\n_REPL_'
                for p in params:
                    for l in swagger.param(p, pspec):
                        r += f'\n{i}{i}{l}'
                s = ''
                for k in 'query', 'formData', 'path', 'body', 'mime':
                    l = pspec.get(k)
                    if not l:
                        continue
                    if k == 'mime':
                        if l == 'application/json':   # omit default
                            continue
                        l = apostr(l)
                    s += f'_{k} = {l}; '
                s = f'\n{i*3}{s}' if s else s
                s = swagger.build_details_cls(2, s)
                r = r.replace('_REPL_', s)
        r = swagger.repl_defs(r)
        r = pre + r
        P = ['']
        for p, d in swagger.pparams.items():
            P.append(d)
        # we indent methods ONE space, so that fold all does not close them:
        # but still we are in a block, so that directives are found and evaled
        sep = '\n '
        _ = ctx.state.get('sep')
        if _ != None:
            _ = f"'{_}'" if is_(_, str) else _
            sep = f'\n {_},{sep}'
        r = r.replace('_TOC_', sep.join(toc))
        r = r.replace('_PTHPARAMS_', '\n'.join(P).replace('\nR.', '\n'))
        r += tools_cls
        # r += '\nTools.send(pet___petId_.get)'

        return r, swagger.post_generate

    @staticmethod
    def param(p: dict, M: dict):
        # {'description': 'ID of pet to update', 'format': 'int64', 'in': 'path', 'name': 'petId', 'required': True, 'type': 'integer'}
        n = p['name']
        in_ = p['in']
        M.setdefault(in_, []).append(n)
        # sometimes missing
        p['type'] = p.get('type', p.get('format', 'string'))
        v = p.get('schema', p)
        l = swagger.prop(n, v)
        return l

    @staticmethod
    def post_generate(scb, rb):
        vimcmd(':1')
        for i in range(swagger.clses + 2):
            vimcmd('/\\nclass')
            vimcmd('normal 2j')
            vimcmd('foldclose')
        vimcmd(':1')
        vimcmd('/methods')


def ExecuteSelectedRange():
    """Called method when hotkey is pressed in vim"""
    src_buf = vim.current.buffer
    nrs = list(range(ctx.L1 - 1, ctx.L2))
    # check if we are within a block and go up:
    # we do this only if there is no visual range selected
    show_help = clear_buffer = clear_help = False

    def into_src_buffer(sb, lines):
        """sometimes we modify the source buffer. macros, swagger, ..."""
        for l in lines.strip().splitlines():
            l1 = l.strip()
            if l1.startswith('vim:'):
                vimcmd(f'{len(sb)}j')
                vimcmd(l1.split('vim:', 1)[1].strip())
            else:
                sb.append(l)

    # for hotkey on single lines we evaluate a few convenience statements
    # and extend the selected range the top of the block:
    orig_line = src_buf[nrs[0]]
    post_generate = False
    # just hotkey on a single line?
    if len(nrs) == 1:
        # in general, if not special handling is wanted we move up until the block starts, then go down:
        l = src_buf[nrs[0]].strip()
        v = try_load_file_or_url(l)   # load swagger specs
        if v:
            v, post_generate = v
            clear_all(buffer=src_buf)
            into_src_buffer(src_buf, v)
            clear_buffer = clear_help = True
        elif l == '':
            show_help = clear_buffer = True
        elif l in macros:
            vimcmd('delete')
            vimcmd('delete')
            v = macros[l]
            into_src_buffer(src_buf, v)
            clear_buffer = clear_help = True
        else:
            # move up:
            while (src_buf[nrs[0]] + ' ')[0] in {' ', ']', '}', ')'}:
                nrs.insert(0, nrs[0] - 1)
            nrs = [nrs[0]]

    # if there is just one selected, we now take the whole block:
    if len(nrs) == 1:
        try:
            while (src_buf[nrs[-1] + 1] + ' ')[0] in {' ', ']', '}', ')'}:
                nrs.append(nrs[-1] + 1)
        except:
            pass

    block = [src_buf[i] for i in nrs]

    # find statements like clear or doc:
    bs, docs, l1 = list(block), ctx.docs, []
    while bs:
        l = bs.pop()   # bottom to top
        l = l.strip()
        l = (l[1:] if l.startswith('#') else l).strip()
        if l.startswith(':cmt '):
            docs.insert(0, '# ' + l.split(':cmt ', 1)[1].strip())
        elif l == ':doc':
            docs.insert(0, l1)
        l1 = l

    block = '\n'.join(block)
    state = ctx.state

    if ':autodoc' in block:
        state['autodoc'] = True
    if ':noautodoc' in block:
        state.pop('autodoc', 0)
    if ':clear' in block:
        clear_buffer = True
    if ':eval file' in block:
        all_ = '\n'.join([src_buf[i] for i in range(0, len(src_buf))])
        exec(all_, state, state)
    wrap = doc_call = ''
    if ':wrap ' in block and '{}' in block.split(':wrap ', 1)[1]:
        wrap = block.split(':wrap ', 1)[1].split('\n', 1)[0].strip()
    if ':doc' in block:
        doc_call = True

    if ':exec single' in block:
        block = orig_line.strip()
        block = block[:-1] if block.strip().endswith(',') else block

    if wrap:
        block = wrap.replace('{}', block)
    dt = ''
    res_buf: list = add_or_switch_to_window('results.py', remember_cur=True)
    if not state:
        state.update(globals())
    if clear_buffer or state.get('autodoc'):
        clear_all(buffer=res_buf)
    if show_help:
        ress = help()
    elif clear_help:
        ress = ''
    else:
        try:
            t0 = time.time()
            exec(block, state, state)
            dt = round(time.time() - t0, 2)
        except Exception as ex:
            state['y'] = f'Evaluation error:\n{type(ex)}\n{str(ex)}'
        ress = check_print_wanted(state)   # res str
        # [b.append(l) for l in block.splitlines()]
    if doc_call or state.get('autodoc'):
        dt = f'[{dt}s]' if dt else ''
        [docs.insert(0, f'# {i} {dt}') for i in block.splitlines()]
    [res_buf.append(l) for l in docs]
    docs.clear()

    if ress:
        [res_buf.append(l) for l in ress.splitlines()]
    vimcmd(':Format')
    vimcmd(f'{len(res_buf)}j')
    res_buf = add_or_switch_to_window('previous')
    # vimcmd('delete') if clear_buffer else 0
    if post_generate:
        post_generate(src_buf, res_buf)


if __name__ == '__main__':
    # testing. call the module with a swagger file
    debug, a = True, sys.argv
    if len(a) == 1:
        print('call me on a swagger definition file or url.')
        sys.exit(1)
    s = read_file('./mods.py')
    if s:
        m = {}
        exec(s, m, m)
        ctx.state.update(m)

    fn = a[1].rsplit('/', 1)[-1]
    r = try_load_file_or_url(fn)[0]
    if not sys.stdout.isatty():
        sys.exit(print(r))
    for s in 'json', 'yaml', 'yml':
        fn = fn.replace(f'.{s}', '')
    fn = f'client_{fn}'   # I like to tab complete...
    fn += '.py'
    s = """
        if __name__ == '__main__':
            import sys, os
            match = '' if len(sys.argv) == 1 else sys.argv[1]
            a, result = ([1], 0) if 'testmode' in os.environ else ([0], 2)
            for m in methods():
                if callable(m) and match in m.__qualname__:
                    print(f'Calling {m.__qualname__}', file=sys.stderr)
                    if not a[0]:
                        y = input('Ok [y/a(lways)/N/q]? ').lower()
                        if y == 'q': sys.exit(0)
                        if y == 'a': a[0] = 1
                        if y not in {'y', 'a'}: continue
                    print(json.dumps(Tools.send(m), indent=4, sort_keys=True))
    """
    r = '#!/usr/bin/env python\n' + r
    r += '\n' + deindent(s)
    open(fn, 'w').write(r)
    os.system(f'chmod +x "{fn}"')
    print(f'Have written: {fn}')
