#!/usr/bin/env python

# type: ignore
'''
Swagger Petstore - OpenAPI 3.0
openapi.json

contact:
  email: apiteam@swagger.io
description: 'This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You
  can find out more about

  Swagger at [http://swagger.io](http://swagger.io). In the third iteration of the
  pet store, we''ve switched to the design first approach!

  You can now help us improve the API whether it''s by making changes to the definition
  itself or to the code.

  That way, with time, we can improve the API in general, and expose some of the new
  features in OAS3.


  Some useful links:

  - [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)

  - [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)'
license:
  name: Apache 2.0
  url: http://www.apache.org/licenses/LICENSE-2.0.html
openapi: 3.0.2
termsOfService: http://swagger.io/terms/
version: 1.0.17

'''
result = 0
timeout = 5
# -

class API:
    user, passw = '$user', '$password'
    host = 'http://127.0.0.1:8000/api/v3'
    base = ''
    hdrs = {}


petId = 0
orderId = 0
username = 'str'

# fmt:off
methods = lambda: ( # :clear :doc :all :single :wrap p = Tools.send({})
 '🟧', pet.put,
 '🟪', pet.post,
 '🟩', pet__findByStatus.get,
 '🟩', pet__findByTags.get,
 '🟩', pet___petId_.get,
 '🟪', pet___petId_.post,
 '🟥', pet___petId_.delete,
 '🟪', pet___petId___uploadImage.post,
 '🟩', store__inventory.get,
 '🟪', store__order.post,
 '🟩', store__order___orderId_.get,
 '🟥', store__order___orderId_.delete,
 '🟪', user.post,
 '🟪', user__createWithList.post,
 '🟩', user__login.get,
 '🟩', user__logout.get,
 '🟩', user___username_.get,
 '🟧', user___username_.put,
 '🟥', user___username_.delete,
) 
# fmt:on


class Defs:
    class components_schemas_Address:
        """#/components/schemas/Address"""
        class R:
            type='object'
            _attrs = ['street', 'city', 'state', 'zip']
            street = {'type': 'string', 'example': '437 Lytton'}
            city = {'type': 'string', 'example': 'Palo Alto'}
            state = {'type': 'string', 'example': 'CA'}
            zip = {'type': 'string', 'example': '94301'}
        R.street = '437 Lytton'
        R.city = 'Palo Alto'
        R.state = 'CA'
        R.zip = '94301'
    class components_schemas_ApiResponse:
        """#/components/schemas/ApiResponse"""
        class R:
            type='object'
            _attrs = ['code', 'type', 'message']
            code = {'type': 'integer', 'format': 'int32'}
            type = {'type': 'string'}
            message = {'type': 'string'}
        R.code = 0
        R.type = 'str'
        R.message = 'str'
    class components_schemas_Category:
        """#/components/schemas/Category"""
        class R:
            type='object'
            _attrs = ['id', 'name']
            id = {'type': 'integer', 'format': 'int64', 'example': 1}
            name = {'type': 'string', 'example': 'Dogs'}
        R.id = 1
        R.name = 'Dogs'
    class components_schemas_Order:
        """#/components/schemas/Order"""
        class R:
            type='object'
            _attrs = ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete']
            id = {'type': 'integer', 'format': 'int64', 'example': 10}
            petId = {'type': 'integer', 'format': 'int64', 'example': 198772}
            quantity = {'type': 'integer', 'format': 'int32', 'example': 7}
            shipDate = {'type': 'string', 'format': 'date-time'}
            status = {'type': 'string', 'example': 'approved', 'enum': ['placed', 'approved', 'delivered'], 'descr': 'Order Status'}
            complete = {'type': 'boolean'}
        R.id = 10
        R.petId = petId
        R.quantity = 7
        R.shipDate = '2022-12-11T00:30:27Z'
        R.status = 'approved'
        R.complete = True
    class components_schemas_Pet:
        """#/components/schemas/Pet"""
        class R:
            required=['name', 'photoUrls']
            type='object'
            _attrs = ['id', 'name', 'category', 'photoUrls', 'tags', 'status']
            id = {'type': 'integer', 'format': 'int64', 'example': 10}
            name = {'type': 'string', 'example': 'doggie'}
            category = lambda: Defs.components_schemas_Category
            photoUrls = {'type': 'array', 'xml': {'wrapped': True}, 'items': {'type': 'string', 'xml': {'name': 'photoUrl'}}}
            tags = {'type': 'array', 'xml': {'wrapped': True}, 'items': lambda: Defs.components_schemas_Tag}
            status = {'type': 'string', 'enum': ['available', 'pending', 'sold'], 'descr': 'pet status in the store'}
        R.id = 10
        R.name = 'doggie'
        R.category = lambda: Defs.components_schemas_Category
        R.photoUrls = ['str']
        R.tags = [lambda: Defs.components_schemas_Tag]
        R.status = 'available'
    class components_schemas_Tag:
        """#/components/schemas/Tag"""
        class R:
            type='object'
            _attrs = ['id', 'name']
            id = {'type': 'integer', 'format': 'int64'}
            name = {'type': 'string'}
        R.id = 0
        R.name = 'str'
    class components_schemas_User:
        """#/components/schemas/User"""
        class R:
            type='object'
            _attrs = ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus']
            id = {'type': 'integer', 'format': 'int64', 'example': 10}
            username = {'type': 'string', 'example': 'theUser'}
            firstName = {'type': 'string', 'example': 'John'}
            lastName = {'type': 'string', 'example': 'James'}
            email = {'type': 'string', 'example': 'john@email.com'}
            password = {'type': 'string', 'example': '12345'}
            phone = {'type': 'string', 'example': '12345'}
            userStatus = {'type': 'integer', 'format': 'int32', 'example': 1, 'descr': 'User Status'}
        R.id = 10
        R.username = username
        R.firstName = 'John'
        R.lastName = 'James'
        R.email = 'john@email.com'
        R.password = '12345'
        R.phone = '12345'
        R.userStatus = 1

class pet:
    pth = "/pet"

    class put:
        """Update an existing pet by Id Update an existing pet"""
        class R:
            _body = ['body'];
            _ = {'tags': ['pet'], 'operationId': 'updatePet', 'requestBody': {'description': 'Update an existent pet in the store', 'content': {'application/xml': {'schema': Defs.components_schemas_Pet}, 'application/x-www-form-urlencoded': {'schema': Defs.components_schemas_Pet}}, 'required': True}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_Pet}, 'application/json': {'schema': Defs.components_schemas_Pet}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}, '405': {'description': 'Validation exception'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}], 'mime': 'application/json'}
            body = Defs.components_schemas_Pet
        R.body = Defs.components_schemas_Pet

    class post:
        """Add a new pet to the store Add a new pet to the store"""
        class R:
            _body = ['body'];
            _ = {'tags': ['pet'], 'operationId': 'addPet', 'requestBody': {'description': 'Create a new pet in the store', 'content': {'application/xml': {'schema': Defs.components_schemas_Pet}, 'application/x-www-form-urlencoded': {'schema': Defs.components_schemas_Pet}}, 'required': True}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_Pet}, 'application/json': {'schema': Defs.components_schemas_Pet}}}, '405': {'description': 'Invalid input'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}], 'mime': 'application/json'}
            body = Defs.components_schemas_Pet
        R.body = Defs.components_schemas_Pet

class pet__findByStatus:
    pth = "/pet/findByStatus"

    class get:
        """Multiple status values can be provided with comma separated strings Finds Pets by status"""
        class R:
            _query = ['status'];
            _ = {'tags': ['pet'], 'operationId': 'findPetsByStatus', 'responses': {'200': {'description': 'successful operation', 'content': {'application/xml': {'schema': {'type': 'array', 'items': Defs.components_schemas_Pet}}, 'application/json': {'schema': {'type': 'array', 'items': Defs.components_schemas_Pet}}}}, '400': {'description': 'Invalid status value'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            status = {'type': 'string', 'default': 'available', 'enum': ['available', 'pending', 'sold']}
        R.status = 'available'

class pet__findByTags:
    pth = "/pet/findByTags"

    class get:
        """Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. Finds Pets by tags"""
        class R:
            _query = ['tags'];
            _ = {'tags': ['pet'], 'operationId': 'findPetsByTags', 'responses': {'200': {'description': 'successful operation', 'content': {'application/xml': {'schema': {'type': 'array', 'items': Defs.components_schemas_Pet}}, 'application/json': {'schema': {'type': 'array', 'items': Defs.components_schemas_Pet}}}}, '400': {'description': 'Invalid tag value'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            tags = {'type': 'array', 'items': {'type': 'string'}}
        R.tags = ['str']

class pet___petId_:
    pth = "/pet/{petId}"

    class get:
        """Returns a single pet Find pet by ID"""
        class R:
            _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'getPetById', 'responses': {'200': {'description': 'successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_Pet}, 'application/json': {'schema': Defs.components_schemas_Pet}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Pet not found'}}, 'security': [{'api_key': []}, {'petstore_auth': ['write:pets', 'read:pets']}]}
            petId = {'type': 'integer', 'format': 'int64'}
        R.petId = petId

    class post:
        """ Updates a pet in the store with form data"""
        class R:
            _query = ['name', 'status']; _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'updatePetWithForm', 'responses': {'405': {'description': 'Invalid input'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            petId = {'type': 'integer', 'format': 'int64'}
            name = {'type': 'string'}
            status = {'type': 'string'}
        R.petId = petId
        R.name = 'str'
        R.status = 'str'

    class delete:
        """ Deletes a pet"""
        class R:
            _path = ['petId'];
            _ = {'tags': ['pet'], 'operationId': 'deletePet', 'responses': {'400': {'description': 'Invalid pet value'}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}]}
            api_key = {'type': 'string'}
            petId = {'type': 'integer', 'format': 'int64'}
        R.api_key = 'str'
        R.petId = petId

class pet___petId___uploadImage:
    pth = "/pet/{petId}/uploadImage"

    class post:
        """ uploads an image"""
        class R:
            _query = ['additionalMetadata']; _path = ['petId']; _mime = 'application/octet-stream';
            _ = {'tags': ['pet'], 'operationId': 'uploadFile', 'requestBody': {'content': {'application/octet-stream': {'schema': {'type': 'string', 'format': 'binary'}}}}, 'responses': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': Defs.components_schemas_ApiResponse}}}}, 'security': [{'petstore_auth': ['write:pets', 'read:pets']}], 'mime': 'application/octet-stream'}
            petId = {'type': 'integer', 'format': 'int64'}
            additionalMetadata = {'type': 'string'}
            content = {'name': 'content', 'type': 'string', 'mime': 'application/octet-stream', 'in': 'mimetype'}
        R.petId = petId
        R.additionalMetadata = 'str'
        R.content = 'str'

class store__inventory:
    pth = "/store/inventory"

    class get:
        """Returns a map of status codes to quantities Returns pet inventories by status"""
        class R:
            _ = {'tags': ['store'], 'operationId': 'getInventory', 'responses': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': {'type': 'object', 'additionalProperties': {'type': 'integer', 'format': 'int32'}}}}}}, 'security': [{'api_key': []}]}

class store__order:
    pth = "/store/order"

    class post:
        """Place a new order in the store Place an order for a pet"""
        class R:
            _body = ['body'];
            _ = {'tags': ['store'], 'operationId': 'placeOrder', 'requestBody': {'content': {'application/xml': {'schema': Defs.components_schemas_Order}, 'application/x-www-form-urlencoded': {'schema': Defs.components_schemas_Order}}}, 'responses': {'200': {'description': 'successful operation', 'content': {'application/json': {'schema': Defs.components_schemas_Order}}}, '405': {'description': 'Invalid input'}}, 'mime': 'application/json'}
            body = Defs.components_schemas_Order
        R.body = Defs.components_schemas_Order

class store__order___orderId_:
    pth = "/store/order/{orderId}"

    class get:
        """For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions. Find purchase order by ID"""
        class R:
            _path = ['orderId'];
            _ = {'tags': ['store'], 'operationId': 'getOrderById', 'responses': {'200': {'description': 'successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_Order}, 'application/json': {'schema': Defs.components_schemas_Order}}}, '400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}}}
            orderId = {'type': 'integer', 'format': 'int64'}
        R.orderId = orderId

    class delete:
        """For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors Delete purchase order by ID"""
        class R:
            _path = ['orderId'];
            _ = {'tags': ['store'], 'operationId': 'deleteOrder', 'responses': {'400': {'description': 'Invalid ID supplied'}, '404': {'description': 'Order not found'}}}
            orderId = {'type': 'integer', 'format': 'int64'}
        R.orderId = orderId

class user:
    pth = "/user"

    class post:
        """This can only be done by the logged in user. Create user"""
        class R:
            _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'createUser', 'requestBody': {'description': 'Created user object', 'content': {'application/xml': {'schema': Defs.components_schemas_User}, 'application/x-www-form-urlencoded': {'schema': Defs.components_schemas_User}}}, 'responses': {'default': {'description': 'successful operation', 'content': {'application/json': {'schema': Defs.components_schemas_User}, 'application/xml': {'schema': Defs.components_schemas_User}}}}, 'mime': 'application/json'}
            body = Defs.components_schemas_User
        R.body = Defs.components_schemas_User

class user__createWithList:
    pth = "/user/createWithList"

    class post:
        """Creates list of users with given input array Creates list of users with given input array"""
        class R:
            _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'createUsersWithListInput', 'requestBody': {'content': {}}, 'responses': {'200': {'description': 'Successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_User}, 'application/json': {'schema': Defs.components_schemas_User}}}, 'default': {'description': 'successful operation'}}, 'mime': 'application/json'}
            body = {'type': 'array', 'items': Defs.components_schemas_User}
        R.body = [Defs.components_schemas_User]

class user__login:
    pth = "/user/login"

    class get:
        """ Logs user into the system"""
        class R:
            _query = ['username', 'password'];
            _ = {'tags': ['user'], 'operationId': 'loginUser', 'responses': {'200': {'description': 'successful operation', 'headers': {'X-Rate-Limit': {'description': 'calls per hour allowed by the user', 'schema': {'type': 'integer', 'format': 'int32'}}, 'X-Expires-After': {'description': 'date in UTC when token expires', 'schema': {'type': 'string', 'format': 'date-time'}}}, 'content': {'application/xml': {'schema': {'type': 'string'}}, 'application/json': {'schema': {'type': 'string'}}}}, '400': {'description': 'Invalid username/password supplied'}}}
            username = {'type': 'string'}
            password = {'type': 'string'}
        R.username = username
        R.password = 'str'

class user__logout:
    pth = "/user/logout"

    class get:
        """ Logs out current logged in user session"""
        class R:
            _ = {'tags': ['user'], 'operationId': 'logoutUser', 'responses': {'default': {'description': 'successful operation'}}}

class user___username_:
    pth = "/user/{username}"

    class get:
        """ Get user by user name"""
        class R:
            _path = ['username'];
            _ = {'tags': ['user'], 'operationId': 'getUserByName', 'responses': {'200': {'description': 'successful operation', 'content': {'application/xml': {'schema': Defs.components_schemas_User}, 'application/json': {'schema': Defs.components_schemas_User}}}, '400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}}}
            username = {'type': 'string'}
        R.username = username

    class put:
        """This can only be done by the logged in user. Update user"""
        class R:
            _path = ['username']; _body = ['body'];
            _ = {'tags': ['user'], 'operationId': 'updateUser', 'requestBody': {'description': 'Update an existent user in the store', 'content': {'application/xml': {'schema': Defs.components_schemas_User}, 'application/x-www-form-urlencoded': {'schema': Defs.components_schemas_User}}}, 'responses': {'default': {'description': 'successful operation'}}, 'mime': 'application/json'}
            username = {'type': 'string'}
            body = Defs.components_schemas_User
        R.username = username
        R.body = Defs.components_schemas_User

    class delete:
        """This can only be done by the logged in user. Delete user"""
        class R:
            _path = ['username'];
            _ = {'tags': ['user'], 'operationId': 'deleteUser', 'responses': {'400': {'description': 'Invalid username supplied'}, '404': {'description': 'User not found'}}}
            username = {'type': 'string'}
        R.username = username

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
        return meth.__name__, pth, q, data, h

    @staticmethod
    def obj(def_, is_=isinstance):
        if callable(def_):
            if inspect.isfunction(def_):
                def_ = def_()
        if is_(def_, str) and def_.startswith('obj:'):
            def_ = getattr(Defs, def_[4:])
        if is_(def_, (float, int, bool, str)):
            return def_
        me = Tools.obj
        if is_(def_, list):
            return [me(def_[0])]
        if is_(def_, dict):
            return {k: me(v) for k, v in def_.items()}
        R = getattr(def_, 'R', 0)
        if R:
            return me(R)
        l = getattr(def_, '_attrs', [i for i in dir(def_) if not i[0] == '_'])
        return {k: me(getattr(def_, k)) for k in l}

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
    import sys
    for m in methods():
        if callable(m):
            print(f'Calling {m}', file=sys.stderr)
            print(json.dumps(Tools.send(m), indent=4, sort_keys=True))
    