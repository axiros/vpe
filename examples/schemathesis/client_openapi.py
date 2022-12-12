#!/usr/bin/env python

# type: ignore
'''
Example API
openapi.json

An API to test Schemathesis, 1.0.0, 3.0.2
'''
result = 1
str_dflt = ''
timeout = 5
# -

class API:
    user, passw = '$user', '$password'
    host = 'https://example.schemathesis.io/{basePath}'
    base = ''
    hdrs = {}


key = str_dflt
id = 0
user_id = str_dflt

# fmt:off
methods = lambda: ( # :clear :doc :eval all :exec single :wrap p = Tools.send({})
 '🟩', success.get,
 '🟩', failure.get,
 '🟪', payload.post,
 '🟩', get_payload.get,
 '🟩', basic.get,
 '🟩', empty.get,
 '🟩', empty_string.get,
 '🟩', multiple_failures.get,
 '🟩', slow.get,
 '🟩', path_variable___key_.get,
 '🟪', unsatisfiable.post,
 '🟪', performance.post,
 '🟪', invalid.post,
 '🟩', flaky.get,
 '🟩', recursive.get,
 '🟪', multipart.post,
 '🟪', upload_file.post,
 '🟪', form.post,
 '🟪', teapot.post,
 '🟩', text.get,
 '🟪', text.post,
 '🟩', cp866.get,
 '🟪', csv.post,
 '🟩', malformed_json.get,
 '🟩', invalid_response.get,
 '🟩', custom_format.get,
 '🟪', credit_card.post,
 '🟩', invalid_path_parameter___id_.get,
 '🟩', missing_path_parameter___id_.get,
 '🟩', headers.get,
 '🟩', foo_bar.get,
 '🟩', not_checked_auth.get,
 '🟪', unexpected.post,
 '🟪', users__.post,
 '🟩', users___user_id_.get,
 '🟫', users___user_id_.patch,
) 
# fmt:on


class Defs:
    class components_links_UpdateUserById:
        """#/components/links/UpdateUserById"""
        class R:
            operationId = 'updateUser'
            _attrs = ['user_id']
            user_id = {'in': 'body', 'name': 'user_id', 'type': 'string', 'example': '$response.body#/id'}
        R.user_id = user_id
    class components_responses_ResponseWithLinks:
        """#/components/responses/ResponseWithLinks"""
        class R:
            description = 'OK'
            links = {'GetUserByUserId': {'operationId': 'getUser', 'parameters': {'path.user_id': '$response.body#/id', 'query.user_id': '$response.body#/id'}}, 'UpdateUserById': lambda: Defs.components_links_UpdateUserById}
    class x_definitions_Node:
        """#/x-definitions/Node"""
        class R:
            description = 'Recursive!'
            type = 'object'
            additionalProperties = False
            _attrs = ['children', 'value']
            children = {'type': 'array', 'items': lambda: Defs.x_definitions_Node}
            value = {'type': 'integer', 'maximum': 4, 'exclusiveMaximum': True}
        R.children = [lambda: Defs.x_definitions_Node]
        R.value = 0

class success:
    pth = "/success"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class failure:
    pth = "/failure"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class payload:
    pth = "/payload"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'age': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}, 'boolean': {'type': 'boolean'}, 'nested': {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}}, 'required': ['name'], 'example': {'name': 'John'}, 'additionalProperties': False}}}}}, 'mime': 'application/json'}
            name = {'type': 'string'}
            age = {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}
            boolean = {'type': 'boolean'}
            nested = {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}
            body = {'type': 'object', 'properties': {'name': {'type': 'string'}, 'age': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}, 'boolean': {'type': 'boolean'}, 'nested': {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}}, 'required': ['name'], 'additionalProperties': False}
        R.body = dict(name = str_dflt, age = 0, boolean = True, nested = [0])

class get_payload:
    pth = "/get_payload"

    class get:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}}, 'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'age': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}, 'boolean': {'type': 'boolean'}, 'nested': {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}}, 'required': ['name'], 'example': {'name': 'John'}, 'additionalProperties': False}}}}}, 'mime': 'application/json'}
            name = {'type': 'string'}
            age = {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}
            boolean = {'type': 'boolean'}
            nested = {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}
            body = {'type': 'object', 'properties': {'name': {'type': 'string'}, 'age': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True}, 'boolean': {'type': 'boolean'}, 'nested': {'type': 'array', 'items': {'type': 'integer', 'minimum': 0, 'exclusiveMinimum': True, 'maximum': 10, 'exclusiveMaximum': True}}}, 'required': ['name'], 'example': {'name': 'John'}, 'additionalProperties': False}
        R.body = {'name': 'John'},

class basic:
    pth = "/basic"

    class get:
        """ """
        class R:
            _ = {'security': [{'basicAuth': []}], 'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'secret': {'type': 'integer'}}}}}}}}

class empty:
    pth = "/empty"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class empty_string:
    pth = "/empty_string"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class multiple_failures:
    pth = "/multiple_failures"

    class get:
        """ """
        class R:
            _query = ['id'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            id = {'type': 'integer'}
        R.id = id

class slow:
    pth = "/slow"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class path_variable___key_:
    pth = "/path_variable/{key}"

    class get:
        """ """
        class R:
            _path = ['key'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            key = {'type': 'string', 'minLength': 1}
        R.key = key

class unsatisfiable:
    pth = "/unsatisfiable"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'required': True}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'application/json'}
            body = {'allOf': [{'type': 'integer'}, {'type': 'string'}]}
        R.body = str_dflt

class performance:
    pth = "/performance"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'required': True}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'application/json'}
            body = {'type': 'integer'}
        R.body = 0

class invalid:
    pth = "/invalid"

    class post:
        """ """
        class R:
            _query = ['id'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            id = {'type': 'int'}
        R.id = id

class flaky:
    pth = "/flaky"

    class get:
        """ """
        class R:
            _query = ['id'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            id = {'type': 'integer'}
        R.id = id

class recursive:
    pth = "/recursive"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': Defs.x_definitions_Node}}}}}

class multipart:
    pth = "/multipart"

    class post:
        """ """
        class R:
            _formData = ['form']; _mime = 'multipart/form-data';
            _ = {'requestBody': {'required': True, 'content': {}}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'multipart/form-data'}
            key = {'type': 'string'}
            value = {'type': 'integer'}
            maybe = {'type': 'boolean'}
            form = {'type': 'object', 'properties': {'key': {'type': 'string'}, 'value': {'type': 'integer'}, 'maybe': {'type': 'boolean'}}, 'required': ['key', 'value']}
        R.form = dict(key = key, value = 0, maybe = True)

class upload_file:
    pth = "/upload_file"

    class post:
        """ """
        class R:
            _formData = ['form']; _mime = 'multipart/form-data';
            _ = {'requestBody': {'required': True, 'content': {}}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'multipart/form-data'}
            data = {'type': 'string', 'format': 'binary'}
            note = {'type': 'string'}
            form = {'type': 'object', 'properties': {'data': {'type': 'string', 'format': 'binary'}, 'note': {'type': 'string'}}, 'required': ['data', 'note']}
        R.form = dict(data = str_dflt, note = str_dflt)

class form:
    pth = "/form"

    class post:
        """ """
        class R:
            _formData = ['form']; _mime = 'application/x-www-form-urlencoded';
            _ = {'requestBody': {'required': True, 'content': {}}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'application/x-www-form-urlencoded'}
            first_name = {'type': 'string'}
            last_name = {'type': 'string'}
            form = {'additionalProperties': False, 'type': 'object', 'properties': {'first_name': {'type': 'string'}, 'last_name': {'type': 'string'}}, 'required': ['first_name', 'last_name']}
        R.form = dict(first_name = str_dflt, last_name = str_dflt)

class teapot:
    pth = "/teapot"

    class post:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}}}

class text:
    pth = "/text"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

    class post:
        """ """
        class R:
            _mime = 'text/plain';
            _ = {'requestBody': {'content': {'text/plain': {'schema': {'type': 'string'}}}, 'required': True}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'text/plain'}
            content = {'name': 'content', 'type': 'string', 'mime': 'text/plain', 'in': 'mimetype'}
        R.content = str_dflt

class cp866:
    pth = "/cp866"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'text/plain': {'schema': {'type': 'integer'}}}}}}

class csv:
    pth = "/csv"

    class post:
        """ """
        class R:
            _mime = 'text/csv';
            _ = {'requestBody': {'required': True, 'content': {'text/csv': {'schema': {'type': 'array', 'items': {'additionalProperties': False, 'type': 'object', 'properties': {'first_name': {'type': 'string', 'pattern': '\\A[A-Za-z]*\\Z'}, 'last_name': {'type': 'string', 'pattern': '\\A[A-Za-z]*\\Z'}}, 'required': ['first_name', 'last_name']}}}}}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'text/csv'}
            content = {'name': 'content', 'type': 'string', 'mime': 'text/csv', 'in': 'mimetype'}
        R.content = str_dflt

class malformed_json:
    pth = "/malformed_json"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class invalid_response:
    pth = "/invalid_response"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class custom_format:
    pth = "/custom_format"

    class get:
        """ """
        class R:
            _query = ['id'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            id = {'type': 'string', 'format': 'digits'}
        R.id = id

class credit_card:
    pth = "/credit_card"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'required': True}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'application/json'}
            number = {'type': 'string', 'format': 'credit_card_number'}
            body = {'type': 'object', 'properties': {'number': {'type': 'string', 'format': 'credit_card_number'}}, 'required': ['number'], 'additionalProperties': False}
        R.body = dict(number = str_dflt)

class invalid_path_parameter___id_:
    pth = "/invalid_path_parameter/{id}"

    class get:
        """ """
        class R:
            _path = ['id'];
            _ = {'responses': {'200': {'description': 'OK'}}}
            id = {'type': 'integer'}
        R.id = id

class missing_path_parameter___id_:
    pth = "/missing_path_parameter/{id}"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class headers:
    pth = "/headers"

    class get:
        """ """
        class R:
            _ = {'security': [{'api_key': []}], 'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object'}}}, 'headers': {'X-Custom-Header': {'description': 'Custom header', 'schema': {'type': 'integer'}}}}, 'default': {'description': 'Default response'}}}

class foo_bar:
    pth = "/foo:bar"

    class get:
        """ """
        class R:
            _ = {'responses': {'200': {'description': 'OK', 'content': {'application/json': {'schema': {'type': 'object', 'properties': {'success': {'type': 'boolean'}}, 'required': ['success']}}}}, 'default': {'description': 'Default response', 'content': {'application/json': {'schema': {}}}}}}

class not_checked_auth:
    pth = "/not_checked_auth"

    class get:
        """ """
        class R:
            _ = {'security': [{'heisenAuth': []}], 'responses': {'200': {'description': 'OK'}}}

class unexpected:
    pth = "/unexpected"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'required': True}, 'responses': {'200': {'description': 'OK'}}, 'mime': 'application/json'}
            foo = {'type': 'string', 'minLength': 5}
            body = {'type': 'object', 'properties': {'foo': {'type': 'string', 'minLength': 5}}, 'required': ['foo'], 'additionalProperties': False}
        R.body = dict(foo = str_dflt)

class users__:
    pth = "/users/"

    class post:
        """ """
        class R:
            _body = ['body'];
            _ = {'requestBody': {'content': {}, 'required': True}, 'responses': {'201': Defs.components_responses_ResponseWithLinks}, 'mime': 'application/json'}
            first_name = {'type': 'string', 'minLength': 3}
            last_name = {'type': 'string', 'minLength': 3}
            body = {'type': 'object', 'properties': {'first_name': {'type': 'string', 'minLength': 3}, 'last_name': {'type': 'string', 'minLength': 3}}, 'required': ['first_name', 'last_name'], 'additionalProperties': False}
        R.body = dict(first_name = str_dflt, last_name = str_dflt)

class users___user_id_:
    pth = "/users/{user_id}"

    class get:
        """ """
        class R:
            _query = ['common', 'code', 'user_id']; _path = ['user_id'];
            _ = {'operationId': 'getUser', 'responses': {'200': {'description': 'OK', 'links': {'UpdateUserById': {'operationRef': '#/paths/~1users~1{user_id}/patch', 'parameters': {'user_id': '$response.body#/id'}, 'requestBody': {'first_name': 'foo', 'last_name': 'bar'}}}}, '404': {'description': 'Not found'}}}
            common = {'type': 'integer'}
            user_id = {'type': 'string'}
            code = {'type': 'integer'}
            user_id = {'type': 'string'}
        R.common = 0
        R.user_id = user_id
        R.code = 0
        R.user_id = user_id

    class patch:
        """ """
        class R:
            _query = ['common']; _path = ['user_id']; _body = ['body'];
            _ = {'operationId': 'updateUser', 'requestBody': {'content': {}, 'required': True}, 'responses': {'200': {'description': 'OK'}, '404': {'description': 'Not found'}}, 'mime': 'application/json'}
            common = {'type': 'integer'}
            user_id = {'type': 'string'}
            first_name = {'type': 'string', 'minLength': 3}
            last_name = {'type': 'string', 'minLength': 3, 'nullable': True}
            body = {'type': 'object', 'properties': {'first_name': {'type': 'string', 'minLength': 3}, 'last_name': {'type': 'string', 'minLength': 3, 'nullable': True}}, 'required': ['first_name', 'last_name'], 'additionalProperties': False}
        R.common = 0
        R.user_id = user_id
        R.body = dict(first_name = str_dflt, last_name = str_dflt)

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
    