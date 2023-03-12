"""
# Builds Swagger/OpenAPI Client

swagger <swagger URL|filename>

You can directly parametrize and call the APIs from within vim.
"""


import time
import sys
import os
import json
import string
from copy import deepcopy
from share import log, read_file, ctx, is_, debug   # noqa
from share import out, lib, BRKT, deindent, vim, vimcmd   # noqa

pyallwd = set(string.digits + string.ascii_letters + '_')


def try_help():
    return __doc__


def apostr(s, a="'", b='"', c='\n', d='\\n'):
    return (
        f"'{s.replace(a, b).replace(c, d)}'"
        if is_(s, str) and (not s or s[0] not in {'"', "'"})
        else s
    )


class swagger:
    """namespace for all swagger handling related funcs"""

    icos = dict(put='🟧', post='🟪', get='🟩', delete='🟥', dflt='🟫')

    # nasty details: when params are named e.g. async we must convert to "async__", then replace before send
    forbidden_kw = {
        'async',
        'continue',
        'not',
        'for',
        'if',
        'while',
        'from',
        'import',
        'except',
        'raise',
    }
    # path params. will be exposed globally
    pparams = {}
    # number of classes generated to that we can collapse after build:
    clses = 0
    # all definitions:
    definitions = {}
    # while in def we can't ref other defs, must put into lambdas:
    in_def_block = False
    now_date = time.strftime('%Y-%m-%d')
    now_datetime = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    if os.environ.get('testmode'):   # avoid test diffs
        now_date = '2020-12-12'
        now_datetime = '2020-12-12T%12:12:12Z'
    # the tooling:
    code = """
        # type: ignore
        '''
        %(title)s
        swagger %(givenurl)s

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
        methods = lambda: ( # :clear :doc :all :single :wrap p = Tools.send({})
         _TOC_
        ) 
        # fmt:on


        """

    tools_code = """

        # ─────────────── Tools ─────────────────────
        import requests, json, functools, inspect, os
        keyw = %(forbidden_kw)s

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
                if is_(def_, (float, int, bool, str)):
                    return def_
                obj = Tools.obj
                if is_(def_, list):
                    return [obj(def_[0])]
                dict_ = lambda d: d.get('__val__', d)
                if is_(def_, dict):
                    return dict_({k: obj(v) for k, v in def_.items()})
                R = g(def_, 'R', 0)
                if R:
                    return obj(R)
                l = g(def_, '_attrs', [
                      i for i in dir(def_) if not i[0] == '_'])
                r = {k: obj(g(def_, k))
                            for k in l if not is_(g(def_, k), dict)}
                return dict_(r)

            @staticmethod
            def send(meth, *args):
                if args:
                    meth = args[0]   # ico in line
                env = os.environ.get
                getenv = lambda v: env(v[1:], '') if (v and v[0] == '$') else v

                def repl(s):
                    if isinstance(s, str):
                        for k in keyw:
                            s = s.replace(f'{k}__', k)
                    else:
                        s = json.loads(repl(json.dumps(s)))
                    return s

                try:
                    methd, pth, params, data, h = Tools.build_req(meth)
                    params = repl(params)
                    host = f'{API.host}'
                    if not '://' in host:
                        host = 'https://' + host
                    url = repl(f'{host}{API.base}{pth}')
                    h = {k: getenv(v) for k, v in h.items()}
                    kw = {'params': params, 'headers': h, 'timeout': timeout}
                    if getenv(API.passw):
                        kw['auth'] = (getenv(API.user), getenv(API.passw))
                    if getattr(API, 'digest', 0):
                        kw['auth'] = requests.auth.HTTPDigestAuth(*kw['auth'])
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
                    except Exception:
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
                d = '{}'
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
        if f == 'datetime':
            ex = ex or swagger.now_date
        elif f == 'date-time':
            ex = ex or swagger.now_datetime
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
        if not isinstance(v, dict) or 'items' not in v:
            return ex or descr or None, ''
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
        if isinstance(r, str) and (not r or r[0] not in {'{', '['}):
            r = apostr(r)
        sep = ''
        # given examples we simply take:
        if ctx.mod_openapi_ver < 2 and is_(r, list) and not ex:
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
        if k.startswith('$'):
            k = 'dollar_' + k[1:]
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
        d = f'{k} = {apostr(v)}'
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
            if not props and 'type' in d:
                # d like {'description': '...', 'type': 'string'} (k8s)
                # i.e. this is a definition for a simple type
                props = {'__val__': d}
                d = {}
            add(f'{i}class {N}:')
            if N != n:
                add(f'{i}{i}"""{n}"""')
            ins = len(r)
            ctx.cur_cls = []
            if props:
                props = swagger.clean_dictkeys(props)
                ctx.cur_cls.append(f'_attrs = {list(props.keys())}')
                for k, v in props.items():
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
                    else:
                        k = swagger.repl_unallowed_pydef_chars(k)
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
        return lib('yaml').safe_dump(i) if lib('yaml') else json.dumps(i, indent=4)

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
        return h[:-1] if h.endswith('/') else h

    @staticmethod
    def try_load(line, **kw):
        """s the content of a swagger definition file"""

        h = ['http://', 'https://']
        if line.startswith(h[0]) or line.startswith(h[1]):
            s = lib('requests').get(line).text

        s = read_file(line)
        if not s and line.split(':', 1)[0] in h:   # and url.endswith('.json'):
            s = lib('requests').get(line).text

        url = line
        s = s.encode().decode('utf-8-sig')
        if not s or ('swagger' not in s and 'openapi' not in s):
            return
        try:
            if s.strip()[0] in BRKT:
                spec = json.loads(s)
            else:
                spec = lib('yaml').safe_load(s)
            assert isinstance(spec, dict)
        except Exception:
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
        _: str = spec.get('openapi', spec.get('swagger', 2))
        ctx.mod_openapi_ver = int(_.upper().replace('V', '').split('.')[0])
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
            'result'   : 2,       # 0: Show only req, no API hit; 1: only result; 2 : both; 3 : full req object
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
                            # 'application/octet-stream',
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
                    if k == '$ref' and isinstance(v, str):
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
                    ctx.cur_cls.append(f'# = {pspec}')
                    if len(ctx.cur_cls) == 1 and not params:
                        ctx.cur_cls.append('pass')
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
        if _ is not None:
            _ = f"'{_}'" if is_(_, str) else _
            sep = f'\n {_},{sep}'
        r = r.replace('_TOC_', sep.join(toc))
        r = r.replace('_PTHPARAMS_', '\n'.join(P).replace('\nR.', '\n'))
        r += tools_cls

        # # r += '\nTools.send(pet___petId_.get)'
        #     v = try_module(line)
        #     if v:
        #         v, post_generate = v
        #         clear_all(buffer=src_buf)
        #         into_src_buffer(src_buf, v)
        #         clear_buffer = clear_help = True

        return {
            'lines': r,
            'post_generate': swagger.post_generate,
            ':clear': True,
            ':here': True,
        }

    @staticmethod
    def clean_dictkeys(d):
        for k in list(d.keys()):
            if k in swagger.forbidden_kw:
                d[k + '__'] = d.pop(k)
            else:
                k1 = swagger.repl_unallowed_pydef_chars(k)
                if k1 != k:
                    d[k1] = d.pop(k)
        return d

    @staticmethod
    def param(p: dict, M: dict):
        # {'description': 'ID of pet to update', 'format': 'int64', 'in': 'path', 'name': 'petId', 'required': True, 'type': 'integer'}
        p = swagger.clean_dictkeys(p)
        n = p['name']
        n = swagger.repl_unallowed_pydef_chars(n)
        if n in swagger.forbidden_kw:
            n = n + '__'
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
            vimcmd('silent! foldclose')
        vimcmd(':1')
        vimcmd('/methods')


try_load = swagger.try_load


def cli_post(res):
    if not res or not 'host' in str(res['lines']):
        sys.exit(print('Client was not generated - error') or 1)
    r = res['lines']
    mod = sys.argv[1]
    if not mod in ['swagger', 'openapi']:
        sys.exit(print(f'no module {mod}') or 1)
    fn = sys.argv[2].rsplit('/', 1)[-1]
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
