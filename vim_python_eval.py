#!/usr/bin/env python
"""
Tools to make use of python API

API funcs are in Capitals
"""
# pyright: typeCheckingMode=off
import sys, os, json, vim, importlib, time
from functools import partial as P
from pprint import pformat

m_r = """
if 'Sending requests to API endpoint':
    from requests import get, post, delete, patch
    from json import dumps
    from functools import partial
    headers = {'Content-Type': 'application/json'}
    Post = lambda url, data: post(url, data=data, headers=headers)
    vim: foldclose

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


def read_file(fn):
    try:
        with open(fn) as fd:
            s = fd.read()
    except:
        s = ''
    return s


macros = {'r': m_r, 'rx': m_rx}
# custom ones:
fn_m = os.environ['HOME'] + '/.config/vpe/macros.py'
s = read_file(fn_m)
m = {}
if s:
    exec(s, m, m)
macros.update(m['macros'])

# Avoiding the infomous python indent bug for Treesitter...
BRKT = {'{', '['}


def lib(l, t={}) -> dict:
    c = ctx.state['_loaded_libs']
    v = c.get(l, l)
    if not isinstance(v, str):
        return v
    if not t.get(l):
        try:
            t[l] = True
            c[l] = importlib.import_module(l)
            return c[l]
        except:
            pass
    s = '\n' + '-' * 40 + '\n'
    return print(f'{s}Please: pip install {l}{s}\n')


def help():
    r = 'Enter letter and hit evaluation hotkey on it:\n\n'
    for m, v in macros.items():
        v = '# ' + v.lstrip().split('\n', 1)[0].replace('if ', '')
        r += f'{m}: {v}\n'
    r += '\n\nResults you get by assigning "p" or "y" in code blocks.'
    return r


# def get_sel_lines():
class ctx:
    """Interface for the caller, setting us up"""

    cur_buffer = None
    prev_buffer = None
    L1 = 0
    L2 = 0
    # transferred even over module reloads:
    state = {'_loaded_libs': {'yaml': 'pyyaml'}}


def log(s, **kw):
    with open('/tmp/py_api', 'a') as fd:
        s = f'{s} {kw}\n'
        fd.write(s)


def clear_all(buffer):
    del buffer[0 : len(buffer)]


buf = lambda: vim.current.buffer


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
        vim.command(f'rightbelow vsplit {buffername}')
        vim.command(f'setlocal buftype=nofile nospell')
    else:
        vim.command(f'{bid}wincmd w')
    return vim.current.buffer


def check_print_wanted(m):
    for k in formatters:
        v = m.pop(k, None)
        if v is not None:
            vs = formatters[k](v)
            return f'{k} = {vs}'
    clss = [k for k in m if not k[0] == '_' and k[0].upper() == k[0]]
    clss = [m[k] for k in clss if isinstance(m[k], type)]

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
    """Try to represent anything in valid python, avoiding tons of lsp errors in the result window"""
    d = _to_dict(*a, **kw)
    return json.loads(json.dumps(d, default=str))


def _to_dict(obj, depth=0, maxd=5, have=None):
    depth += 1
    if depth > maxd:
        return str(obj)
    if isinstance(obj, str) and obj and obj.lstrip()[0] in BRKT:
        try:
            obj = json.loads(obj)
        except:
            pass

    if isinstance(obj, (dict, set, list, int, float, bool, str)):
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
{y}
    """'''


formatters['y'] = to_y


def try_load_file_or_url(url):
    s = read_file(url)
    h = {'http', 'https'}
    if not s and url.split(':', 1)[0] in h:   # and url.endswith('.json'):
        s = lib('requests').get(url).text
    return swagger.try_load(s, url=url)


deindent = lambda s: s.replace('\n    ', '\n')


class swagger:
    """namespace for all swagger handling related funcs"""

    forbidden_kw = {'async', 'for', 'if', 'while'}
    pparams = {}
    clses = 0
    definitions = set()
    in_def_block = False
    code = """
        '''
        Swagger API (from %(givenurl)s)
        '''

        import requests, json, functools, inspect, os
        env = os.environ.get

        class API:
            proto = 'https'
            user, passw = env('user', ''), env('password', '')
            host = '%(host)s'
            base = '%(basePath)s'

        show_all = 0

        _PTHPARAMS_

        methods = lambda: (
            _TOC_
        ) # :clear :doc :eval file :exec single :wrap p = Tools.send({})


        class Tools:
            @staticmethod
            def build_req(meth):
                ins = ['_body', '_path', '_formData', '_query']
                ins = {k[1:]: getattr(meth, k, []) for k in ins}
                if ins['body'] and ins['formData']:
                    raise Exception('cannot send form AND json')
                Is = isinstance
                data, h, q, m = {}, {}, {}, {}
                c = globals()[meth.__qualname__.split('.', 1)[0]]
                for k in [k for k in dir(meth) if not k[0] == '_']:
                    v = getattr(meth, k)
                    v = Tools.obj(v)
                    if isinstance(v, dict):
                        m.update(v)
                    else:
                        m[k] = v
                    if k in ins['query']:
                        q[k] = v
                    if k in ins['formData'] or k in ins['body']:
                        if k == 'body':
                            data = v
                        else:
                            data[k] = v
                if ins['body']:
                    data = json.dumps(data)   # when dict requests should send form
                    h.update({'Content-Type': 'application/json'})
                pth = c.pth.format(**m) if chr(123) in c.pth else c.pth
                return meth.__name__, pth, q, data, h

            @staticmethod
            def send(meth):
                def repl(s, keyw=%(forbidden_kw)s):
                    if isinstance(s, str):
                        for k in keyw:
                            s = s.replace(f'{k}__', k)
                    else:
                        s = json.loads(Tools.repl(json.dumps(s)))
                    return s

                methd, pth, params, data, h = Tools.build_req(meth)
                url = repl(f'{API.proto}://{API.host}{API.base}{pth}')
                kw = {'params': params, 'headers': h}
                if API.passw:
                    kw['auth'] = (API.user, API.passw)
                if data:
                    kw['data'] = repl(data)
                req = getattr(requests, methd)
                req = req(url, **kw)
                if show_all:
                    return req   # show all
                r = {'status': req.status_code}
                try:
                    r['resp'] = json.loads(req.text)
                except:
                    r['resp'] = req.text
                return r
                # vim: foldclose

            @staticmethod
            def obj(def_):
                if callable(def_):
                    if inspect.isfunction(def_):
                        def_ = def_()
                if isinstance(def_, str) and def_.startswith('obj:'):
                    def_ = getattr(Defs, def_[4:])
                if isinstance(def_, (float, int, bool, str)):
                    return def_
                me = Tools.obj
                if isinstance(def_, list):
                    return [me(def_[0])]
                if isinstance(def_, dict):
                    return {k: me(v) for k, v in def_.items()}
                return {k: me(getattr(def_, k)) for k in dir(def_) if not k[0] == '_'}


        """

    @staticmethod
    def definition(ref: str):
        which = ref.rsplit('/', 1)[-1]
        return f'{which}'

    @staticmethod
    def by_type(v: dict):
        if '$ref' in v:
            return 'ref', swagger.by_obj
        # sometimes missing:
        t = v.pop('type', v.get('format', 'string'))
        if t == 'string':
            return t, swagger.by_str
        if 'int' in t:
            return t, swagger.by_int
        if 'bool' in t:
            return t, swagger.by_bool
        if 'float' in t:
            return t, swagger.by_float
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
        p = v.get('properties')
        if p:
            d = []
            for k1, v1 in p.items():
                v2 = swagger.prop(k1, v1)[-1]
                d.append(v2)
            d = 'dict(%s)' % ', '.join(d)
        else:
            d = swagger.get_ref(v)
            if not d:
                breakpoint()   # FIXME BREAKPOINT
        return ex or d, descr or k

    @staticmethod
    def by_int(k, v, ex, descr):
        return ex or v.get('default', 0), descr or k

    @staticmethod
    def by_str(k, v, ex, descr):
        f = v.get('format')
        if f == 'date-time':
            ex = ex or time.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif f == 'date':
            ex = ex or time.strftime('%Y-%m-%d')
        en = v.get('enum', ['str'])[0]
        return "'%s'" % (ex or v.get('default', en)), descr or k

    @staticmethod
    def by_bool(k, v, ex, descr):
        return ex or v.get('default', True), descr or k

    @staticmethod
    def by_file(k, v, ex, descr):
        return ex or v.get('default', "'~/my_file'"), descr or k

    @staticmethod
    def get_ref(i):
        r = i.get('$ref')
        if r:
            d = swagger.definition(r)
            if swagger.in_def_block:
                return f'lambda: Defs.{d}'
            return f'Defs.{d}' if d in swagger.definitions else f"'obj:{d}'"

    @staticmethod
    def by_array(k, v, ex, descr):
        i = v['items']
        d = swagger.get_ref(i)
        if not d:
            if i.get('example'):
                d = i['example']
                # be robust against ill defined {'example': 'value of any type'}
                if isinstance(d, str) and (not d or d[0] not in {'"', "'"}):
                    d = f"'{d}'"
            else:
                d = swagger.by_type(i)[1](k, i, ex, descr)[0]
        d = v.get('default', f'[{d}]')
        r = ex or d
        sep = ''
        if isinstance(r, list):
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
        # if k == 'username': breakpoint()   # FIXME BREAKPOINT
        t, f = swagger.by_type(v)
        # if v == {
        #     'description': 'Execution result',
        #     'items': {'example': 'value of any type'},
        # }:
        #     breakpoint()   # FIXME BREAKPOINT            'items': {'example': 'value of any type'},

        d = v.pop('description', '')
        if d:
            d += ' '
        # if 'value of any' in str(v.get('example')):
        #     breakpoint()   # FIXME BREAKPOINT
        #     return
        r, d = f(k, v, ex=v.get('example'), descr=d)
        v = v if v else ''
        v, d = r, f'# {d} {v}'
        l = []
        l.append(f'{d}')
        d = ''

        if k in swagger.pparams and not no_ref:
            v = k
        l.append(f'{k} = {v}')
        return l

    # return r, f'# {d} {v}'

    @staticmethod
    def defs(defs):
        """Setting up the Definitions class Tree"""
        swagger.in_def_block = True
        r, i = ['class Defs:'], '    '
        add = r.append

        for n, d in defs.items():
            # if 'GenericMethodRe' in n:
            #     breakpoint()   # FIXME BREAKPOINT
            swagger.definitions.add(n)
            d.pop('xml', 0)
            assert d.pop('type') == 'object'
            props = d.pop('properties')
            add(f'{i}class {n}:')
            # add non relevant props, e.g. required with _ = ... after class:
            [add(f'{i*2}_{k}={v}') for k, v in d.items()]
            if props:
                for k, v in props.items():
                    if k in swagger.forbidden_kw:
                        k += '__'
                    for line in swagger.prop(k, v):
                        add(f'{i*2}{line}')

                    # v, d = swagger.prop(k, v)
                    # if isinstance(v, list):
                    #     add(f'{i*2}{d}')
                    #     d = ''
                    # s = f'{k} = {v} '.ljust(40) + d
                    # add(f'{i*2}{s}')
        swagger.in_def_block = False
        return '\n'.join(r)

    @staticmethod
    def try_load(s: str, url='n.a.'):
        if not s or not 'swagger' in s:
            return
        try:
            if s.strip()[0] in BRKT:
                spec = json.loads(s)
            else:
                spec = lib('yaml').loads(s)
        except:
            return
        # sp = mod.SwaggerParser(swagger_dict=d)
        # allows to predefine globals:
        pp = ctx.state.get('params', {})
        for p, v in pp.items():
            v = f"'{v}'" if isinstance(v, str) else v
            swagger.pparams[p] = f'{p} = {v}'
        spec['givenurl'] = url
        spec['forbidden_kw'] = swagger.forbidden_kw
        r = deindent(swagger.code)
        r = r % spec
        r = r.replace('\n    ', '\n')
        paths = spec['paths']

        def new_pparam(p, _=swagger.pparams):
            v = swagger.prop(p['name'], p, no_ref=True)[-1]
            v = v.split('#', 1)[0].strip()   # comments differ => omit
            _[p['name']] = v

        def find_path_params(methods):
            for m in methods:
                for p1 in m.values():
                    for p in p1.get('parameters', []):
                        if p.get('in') == 'path':
                            new_pparam(p)

        find_path_params(paths.values())

        r += swagger.defs(spec['definitions'])

        toc = []

        def extract_path_params(p):
            for k in swagger.pparams:
                p = p.replace('{%s}' % k, f'_{k}_')
            return p

        i = '    '
        for p in paths:
            swagger.clses += 1
            P = paths[p]
            p_orig = p
            # '/pet/{petId}/uploadImage'
            p = extract_path_params(p)
            pn = f'{p[1:].replace("/", "__")}'
            r += f'\n\nclass {pn}:'
            r += f'\n{i}pth = "{p_orig}"'
            methods = paths[p_orig].keys()
            for m in methods:
                toc.append(f'{pn}.{m},')
                r += f'\n{i}class {m}:'
                M = P[m]
                params = M.pop('parameters')
                doc = f'{M.pop("description", "")} {M.pop("summary", "")}'
                r += f'\n{i}{i}"""{doc}"""'
                r += f'\n{i}{i}# _ = {M}'
                for p in params:
                    for l in swagger.param(p, M):
                        r += f'\n{i}{i}{l}'
                s = ''
                for k in 'query', 'formData', 'path', 'body':
                    l = M.get(k)
                    if not l:
                        continue
                    s += f'_{k} = {l}; '
                r += f'\n{i}{i}{s}'

        P = []
        for p, d in swagger.pparams.items():
            P.append(d)

        r = r.replace('_TOC_', '\n    '.join(toc))
        r = r.replace('_PTHPARAMS_', '\n'.join(P))
        # r += '\nTools.send(pet___petId_.get)'
        return r, swagger.src_post_generate

    @staticmethod
    def param(p: dict, M: dict):
        # {'description': 'ID of pet to update', 'format': 'int64', 'in': 'path', 'name': 'petId', 'required': True, 'type': 'integer'}
        n = p['name']
        in_ = p['in']
        M.setdefault(in_, []).append(n)
        # sometimes missing
        p['type'] = p.get('type', p.get('format', 'string'))
        sch = p.get('schema') or p
        l = swagger.prop(n, sch)

        return l

    def src_post_generate(scb, rb):
        vim.command(':1')
        for i in range(swagger.clses + 3):
            vim.command('/\\nclass')
            vim.command('normal 2j')
            vim.command('foldclose')
        vim.command(':1')
        vim.command('/methods')


def ExecuteSelectedRange():
    """Called method whan hotkey is pressed in vim"""
    src_buf = vim.current.buffer
    nrs = list(range(ctx.L1 - 1, ctx.L2))
    # check if we are within a block and go up:
    # we do this only if there is no visual range selected
    show_help = clear_buffer = clear_help = False

    def into_src_buffer(sb, lines):
        for l in lines.strip().splitlines():
            l1 = l.strip()
            if l1.startswith('vim:'):
                vim.command(f'{len(sb)}j')
                vim.command(l1.split('vim:', 1)[1].strip())
            else:
                sb.append(l)

    # for hotkey on single lines we evaluate a few convenience statements
    # and extend the selected range the top of the block:
    orig_line = src_buf[nrs[0]]
    post_generate = False
    if len(nrs) == 1:
        l = src_buf[nrs[0]].strip()
        # os.system(f'notify-send "{l}"')
        v = try_load_file_or_url(l)   # load swagger specs
        if v:
            v, post_generate = v
            clear_all(buffer=src_buf)
            into_src_buffer(src_buf, v)
            clear_buffer = clear_help = True
        elif l == '':
            show_help = clear_buffer = True
        elif l in macros:
            vim.command('delete')
            vim.command('delete')
            v = macros[l]
            into_src_buffer(src_buf, v)
            clear_buffer = clear_help = True
        else:
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
    bs, docs, l1 = list(block), [], ''
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
    m = ctx.state
    if ':autodoc' in block:
        m['autodoc'] = True
    if ':noautodoc' in block:
        m.pop('autodoc', 0)
    if ':clear' in block:
        clear_buffer = True
    if ':eval file' in block:
        all_ = '\n'.join([src_buf[i] for i in range(0, len(src_buf))])
        exec(all_, m, m)
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

    res_buf: list = add_or_switch_to_window('results.py', remember_cur=True)
    if not m:
        m.update(globals())
    if clear_buffer or m.get('autodoc'):
        clear_all(buffer=res_buf)
    if show_help:
        ress = help()
    elif clear_help:
        ress = ''
    else:
        try:
            exec(block, m, m)
        except Exception as ex:
            m['y'] = f'Evaluation error:\n{type(ex)}\n{str(ex)}'
        ress = check_print_wanted(m)   # res str
        # [b.append(l) for l in block.splitlines()]
    if doc_call or m.get('autodoc'):
        [docs.append(f'# {i}') for i in block.splitlines()]
    [res_buf.append(l) for l in docs]
    if ress:
        [res_buf.append(l) for l in ress.splitlines()]
    vim.command(':Format')
    vim.command(f'{len(res_buf)}j')
    res_buf = add_or_switch_to_window('previous')
    # vim.command('delete') if clear_buffer else 0
    if post_generate:
        post_generate(src_buf, res_buf)


if __name__ == '__main__':
    # testing. call the module with a swagger file
    r = try_load_file_or_url(sys.argv[1])[0]

    # r = try_load_file_or_url('./s.json')
    # r = try_load_file_or_url('http://httpbin.org/post')
    print(r)
