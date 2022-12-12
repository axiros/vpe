#!/usr/bin/env python

# type: ignore
'''
Swagger Petstore
openapi.json

contact:
  email: apiteam@swagger.io
description: 'This is a sample server Petstore server.  You can find out more about
  Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For
  this sample, you can use the api key `special-key` to test the authorization filters.'
license:
  name: Apache 2.0
  url: http://www.apache.org/licenses/LICENSE-2.0.html
openapi: '?'
termsOfService: http://swagger.io/terms/
version: 1.0.6

'''
result = 1
str_dflt = ''
timeout = 5
# -

class API:
    user, passw = '$user', '$password'
    host = 'petstore.swagger.io'
    base = '/v2'
    hdrs = {}


petId = 0
orderId = 0
username = str_dflt

# fmt:off
methods = lambda: ( # :clear :doc :all :single :wrap p = Tools.send({})
 '🟪', pet___petId___uploadImage.post,
 '🟪', pet.post,
 '🟧', pet.put,
 '🟩', pet__findByStatus.get,
 '🟩', pet__findByTags.get,
 '🟩', pet___petId_.get,
 '🟪', pet___petId_.post,
 '🟥', pet___petId_.delete,
 '🟪', store__order.post,
 '🟩', store__order___orderId_.get,
 '🟥', store__order___orderId_.delete,
 '🟩', store__inventory.get,
 '🟪', user__createWithArray.post,
 '🟪', user__createWithList.post,
 '🟩', user___username_.get,
 '🟧', user___username_.put,
 '🟥', user___username_.delete,
 '🟩', user__login.get,
 '🟩', user__logout.get,
 '🟪', user.post,
) 
# fmt:on


class Defs:
    class definitions_ApiResponse:
        """#/definitions/ApiResponse"""
        class R:
            type = 'object'
            _attrs = ['code', 'type', 'message']
            code = {'type': 'integer', 'format': 'int32'}
            type = {'type': 'string'}
            message = {'type': 'string'}
        R.code = 0
        R.type = str_dflt
        R.message = str_dflt
    class definitions_Category:
        """#/definitions/Category"""
        class R:
            type = 'object'
            _attrs = ['id', 'name']
            id = {'type': 'integer', 'format': 'int64'}
            name = {'type': 'string'}
        R.id = 0
        R.name = str_dflt
    class definitions_Order:
        """#/definitions/Order"""
        class R:
            type = 'object'
            _attrs = ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete']
            id = {'type': 'integer', 'format': 'int64'}
            petId = {'type': 'integer', 'format': 'int64'}
            quantity = {'type': 'integer', 'format': 'int32'}
            shipDate = {'type': 'string', 'format': 'date-time'}
            status = {'type': 'string', 'enum': ['placed', 'approved', 'delivered'], 'descr': 'Order Status'}
            complete = {'type': 'boolean'}
        R.id = 0
        R.petId = petId
        R.quantity = 0
        R.shipDate = '2020-12-12T%12:12:12Z'
        R.status = 'placed'
        R.complete = True
    class definitions_Pet:
        """#/definitions/Pet"""
        class R:
            type = 'object'
            required = ['name', 'photoUrls']
            _attrs = ['id', 'category', 'name', 'photoUrls', 'tags', 'status']
            id = {'type': 'integer', 'format': 'int64'}
            category = lambda: Defs.definitions_Category
            name = {'type': 'string', 'example': 'doggie'}
            photoUrls = {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}
            tags = {'type': 'array', 'xml': {'wrapped': True}, 'items': {'xml': {'name': 'tag'}, '$ref': lambda: Defs.definitions_Tag}}
            status = {'type': 'string', 'enum': ['available', 'pending', 'sold'], 'descr': 'pet status in the store'}
        R.id = 0
        R.category = lambda: Defs.definitions_Category
        R.name = 'doggie'
        R.photoUrls = [str_dflt]
        R.tags = [lambda: Defs.definitions_Tag]
        R.status = 'available'
    class definitions_Tag:
        """#/definitions/Tag"""
        class R:
            type = 'object'
            _attrs = ['id', 'name']
            id = {'type': 'integer', 'format': 'int64'}
            name = {'type': 'string'}
        R.id = 0
        R.name = str_dflt
    class definitions_User:
        """#/definitions/User"""
        class R:
            type = 'object'
            _attrs = ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus']
            id = {'type': 'integer', 'format': 'int64'}
            username = {'type': 'string'}
            firstName = {'type': 'string'}
            lastName = {'type': 'string'}
            email = {'type': 'string'}
            password = {'type': 'string'}
            phone = {'type': 'string'}
            userStatus = {'type': 'integer', 'format': 'int32', 'descr': 'User Status'}
        R.id = 0
        R.username = username
        R.firstName = str_dflt
        R.lastName = str_dflt
        R.email = str_dflt
        R.password = str_dflt
        R.phone = str_dflt
        R.userStatus = 0

class pet___petId___uploadImage:
    pth = "/pet/{petId}/uploadImage"

    class post:
        """ uploads an image"""
        class R:
            _formData = ['additionalMetadata', 'file']; _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'uploadFile', 'consumes': ['multipart/form-data'], 'produces': ['application/json'], 'responses': {'200': {'description': 'successful operation', 'schema': Defs.definitions_ApiResponse}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            petId = {'name': 'petId', 'in': 'path', 'required': True, 'type': 'integer', 'format': 'int64', 'descr': 'ID of pet to update'}
            additionalMetadata = {'name': 'additionalMetadata', 'in': 'formData', 'required': False, 'type': 'string', 'descr': 'Additional data to pass to server'}
            file = {'name': 'file', 'in': 'formData', 'required': False, 'type': 'file', 'descr': 'file to upload'}
        R.petId = petId
        R.additionalMetadata = str_dflt
        R.file = '~/my_file'

class pet:
    pth = "/pet"

    class post:
        """ Add a new pet to the store"""
        class R:
            _body = ['body'];
            _ = {'tags': ['pet'], 'operationId': 'addPet', 'consumes': ['application/json', 'application/xml'], 'produces': ['application/json', 'application/xml'], 'responses': {'405': {'description': 'Invalid input'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            body = Defs.definitions_Pet
        R.body = Defs.definitions_Pet

    class put:
        """ Update an existing pet"""
        class R:
            _body = ['body'];
            _ = {'tags': ['pet'], 'operationId': 'updatePet', 'consumes': ['application/json', 'application/xml'], 'produces': ['application/json', 'application/xml'], 'responses': {'400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '405': {'description': 'Validation exception'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            body = Defs.definitions_Pet
        R.body = Defs.definitions_Pet

class pet__findByStatus:
    pth = "/pet/findByStatus"

    class get:
        """Multiple status values can be provided with comma separated strings Finds Pets by status"""
        class R:
            _query = ['status'];
            _ = {'tags': ['pet'], 'operationId': 'findPetsByStatus', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': {'type': 'array', 'items': Defs.definitions_Pet}}, '400': {'description': 'Invalid status value'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            status = {'name': 'status', 'in': 'query', 'required': True, 'type': 'array', 'items': {'type': 'string', 'enum': ['available', 'pending', 'sold'], 'default': 'available'}, 'collectionFormat': 'multi', 'descr': 'Status values that need to be considered for filter'}
        R.status = ['available']

class pet__findByTags:
    pth = "/pet/findByTags"

    class get:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. Finds Pets by tags"""
        class R:
            _query = ['tags'];
            _ = {'tags': ['pet'], 'operationId': 'findPetsByTags', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': {'type': 'array', 'items': Defs.definitions_Pet}}, '400': {'description': 'Invalid tag value'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}], 'deprecated': True}
            tags = {'name': 'tags', 'in': 'query', 'required': True, 'type': 'array', 'items': {'type': 'string'}, 'collectionFormat': 'multi', 'descr': 'Tags to filter by'}
        R.tags = [str_dflt]

class pet___petId_:
    pth = "/pet/{petId}"

    class get:
        """Returns a single pet Find pet by ID"""
        class R:
            _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'getPetById', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': Defs.definitions_Pet}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}}, 'security': [{'api_key': []}]}
            petId = {'name': 'petId', 'in': 'path', 'required': True, 'type': 'integer', 'format': 'int64', 'descr': 'ID of pet to return'}
        R.petId = petId

    class post:
        """ Updates a pet in the store with form data"""
        class R:
            _formData = ['name', 'status']; _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'updatePetWithForm', 'consumes': ['application/x-www-form-urlencoded'], 'produces': ['application/json', 'application/xml'], 'responses': {'405': {'description': 'Invalid input'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            petId = {'name': 'petId', 'in': 'path', 'required': True, 'type': 'integer', 'format': 'int64', 'descr': 'ID of pet that needs to be updated'}
            name = {'name': 'name', 'in': 'formData', 'required': False, 'type': 'string', 'descr': 'Updated name of the pet'}
            status = {'name': 'status', 'in': 'formData', 'required': False, 'type': 'string', 'descr': 'Updated status of the pet'}
        R.petId = petId
        R.name = str_dflt
        R.status = str_dflt

    class delete:
        """ Deletes a pet"""
        class R:
            _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'deletePet', 'produces': ['application/json', 'application/xml'], 'responses': {'400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            api_key = {'name': 'api_key', 'in': 'header', 'required': False, 'type': 'string'}
            petId = {'name': 'petId', 'in': 'path', 'required': True, 'type': 'integer', 'format': 'int64', 'descr': 'Pet id to delete'}
        R.api_key = str_dflt
        R.petId = petId

class store__order:
    pth = "/store/order"

    class post:
        """ Place an order for a pet"""
        class R:
            _body = ['body'];
            _ = {'tags': ['store'], 'operationId': 'placeOrder', 'consumes': ['application/json'], 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': Defs.definitions_Order}, '400': {'description': 'Invalid Order'}}}
            body = Defs.definitions_Order
        R.body = Defs.definitions_Order

class store__order___orderId_:
    pth = "/store/order/{orderId}"

    class get:
        """For valid response try integer IDs with value >= 1 and <= 10. Other values will generated exceptions Find purchase order by ID"""
        class R:
            _path = ['orderId'];
            _ = {'tags': ['store'], 'operationId': 'getOrderById', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': Defs.definitions_Order}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}}}
            orderId = {'name': 'orderId', 'in': 'path', 'required': True, 'type': 'integer', 'maximum': 10, 'minimum': 1, 'format': 'int64', 'descr': 'ID of pet that needs to be fetched'}
        R.orderId = orderId

    class delete:
        """For valid response try integer IDs with positive integer value. Negative or non-integer values will generate API errors Delete purchase order by ID"""
        class R:
            _path = ['orderId'];
            _ = {'tags': ['store'], 'operationId': 'deleteOrder', 'produces': ['application/json', 'application/xml'], 'responses': {'400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}}}
            orderId = {'name': 'orderId', 'in': 'path', 'required': True, 'type': 'integer', 'minimum': 1, 'format': 'int64', 'descr': 'ID of the order that needs to be deleted'}
        R.orderId = orderId

class store__inventory:
    pth = "/store/inventory"

    class get:
        """Returns a map of status codes to quantities Returns pet inventories by status"""
        class R:
            _ = {'tags': ['store'], 'operationId': 'getInventory', 'produces': ['application/json'], 'responses': {'200': {'description': 'successful operation', 'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}, 'security': [{'api_key': []}]}

class user__createWithArray:
    pth = "/user/createWithArray"

    class post:
        """ Creates list of users with given input array"""
        class R:
            _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'createUsersWithArrayInput', 'consumes': ['application/json'], 'produces': ['application/json', 'application/xml'], 'responses': {'default': {'description': 'successful operation'}}}
            body = {'type': 'array', 'items': Defs.definitions_User}
        R.body = [Defs.definitions_User]

class user__createWithList:
    pth = "/user/createWithList"

    class post:
        """ Creates list of users with given input array"""
        class R:
            _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'createUsersWithListInput', 'consumes': ['application/json'], 'produces': ['application/json', 'application/xml'], 'responses': {'default': {'description': 'successful operation'}}}
            body = {'type': 'array', 'items': Defs.definitions_User}
        R.body = [Defs.definitions_User]

class user___username_:
    pth = "/user/{username}"

    class get:
        """ Get user by user name"""
        class R:
            _path = ['username'];
            _ = {'tags': ['user'], 'operationId': 'getUserByName', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'schema': Defs.definitions_User}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}}}
            username = {'name': 'username', 'in': 'path', 'required': True, 'type': 'string', 'descr': 'The name that needs to be fetched. Use user1 for testing. '}
        R.username = username

    class put:
        """This can only be done by the logged in user. Updated user"""
        class R:
            _path = ['username']; _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'updateUser', 'consumes': ['application/json'], 'produces': ['application/json', 'application/xml'], 'responses': {'400': {'description': 'Invalid user supplied'}, '404': {'description': 'User not found'}}}
            username = {'name': 'username', 'in': 'path', 'required': True, 'type': 'string', 'descr': 'name that need to be updated'}
            body = Defs.definitions_User
        R.username = username
        R.body = Defs.definitions_User

    class delete:
        """This can only be done by the logged in user. Delete user"""
        class R:
            _path = ['username'];
            _ = {'tags': ['user'], 'operationId': 'deleteUser', 'produces': ['application/json', 'application/xml'], 'responses': {'400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}}}
            username = {'name': 'username', 'in': 'path', 'required': True, 'type': 'string', 'descr': 'The name that needs to be deleted'}
        R.username = username

class user__login:
    pth = "/user/login"

    class get:
        """ Logs user into the system"""
        class R:
            _query = ['username', 'password'];
            _ = {'tags': ['user'], 'operationId': 'loginUser', 'produces': ['application/json', 'application/xml'], 'responses': {'200': {'description': 'successful operation', 'headers': {'X-Expires-After': {'type': 'string', 'format': 'date-time', 'description': 'date in UTC when token expires'}, 'X-Rate-Limit': {'type': 'integer', 'format': 'int32', 'description': 'calls per hour allowed by the user'}}, 'schema': {'type': 'string'}}, '400': {'description': 'Invalid username/password supplied'}}}
            username = {'name': 'username', 'in': 'query', 'required': True, 'type': 'string', 'descr': 'The user name for login'}
            password = {'name': 'password', 'in': 'query', 'required': True, 'type': 'string', 'descr': 'The password for login in clear text'}
        R.username = username
        R.password = str_dflt

class user__logout:
    pth = "/user/logout"

    class get:
        """ Logs out current logged in user session"""
        class R:
            _ = {'tags': ['user'], 'operationId': 'logoutUser', 'produces': ['application/json', 'application/xml'], 'responses': {'default': {'description': 'successful operation'}}}

class user:
    pth = "/user"

    class post:
        """This can only be done by the logged in user. Create user"""
        class R:
            _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'createUser', 'consumes': ['application/json'], 'produces': ['application/json', 'application/xml'], 'responses': {'default': {'description': 'successful operation'}}}
            body = Defs.definitions_User
        R.body = Defs.definitions_User

# ─────────────── Tools ─────────────────────
import requests, json, functools, inspect, os
keyw = {'while', 'async', 'import', 'from', 'not', 'raise', 'for', 'if', 'continue', 'except'}

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
        l = g(def_, '_attrs', [i for i in dir(def_) if not i[0] == '_'])
        r = {k: obj(g(def_, k)) for k in l if not is_(g(def_, k), dict)}
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
    