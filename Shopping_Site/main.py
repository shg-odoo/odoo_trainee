import json
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

def index(self):
    html = open('template/index.html', 'r').read()
    data = open('product.json', 'r').read()
    cartData = 'false'
    if bool(int(self.session.__len__())):
        cartData = self.session['product_ids']
    response = Response(html % {'data': str(json.loads(data)),
                                'cartData': cartData})
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html'
    return response

def cart(self, product_id=None):

    temp=open('product.json','r').read()
    dataTemp=json.loads(temp)
    qty=0
    
    for i in dataTemp:
        if i['id']==product_id:
            qty=i['qnt']
            i['qnt']=qty+1

    with open('product.json','w+') as obj:
        json.dump(dataTemp,obj)

    if product_id and not bool(int(self.session.__len__())):
        self.session['product_ids'] = {product_id: product_id}
    else:
        self.session['product_ids'].update({product_id: product_id})
    return index(self)

def decrease(self, product_id=None):
    
    dataTemp=json.loads(open('product.json','r').read())

    for i in dataTemp:
        if i['id']==product_id:
            if i['qnt']>1:    
                i['qnt']=i['qnt']-1
            
    with open('product.json','w+') as obj:
        json.dump(dataTemp,obj)
        
        
    if product_id and not bool(int(self.session.__len__())):
        self.session['product_ids'] = {product_id: product_id}    
    else:
        self.session['product_ids'].update({product_id: product_id})


    return index(self)



def remove(self, product_id=None):

    temp=open('product.json','r').read()
    dataTemp=json.loads(temp)
    for i in dataTemp:
        if i['id']==product_id:
            i['qnt']=0
            
    with open('product.json','w+') as obj:
        json.dump(dataTemp,obj)

    if product_id and bool(int(self.session.__len__())):
        self.session['product_ids'].pop(product_id)
    return index(self)


url_map = Map([
    Rule("/", endpoint="index"),
    Rule("/add/to/cart/<int:product_id>", endpoint="cart"),
    Rule("/remove/<int:product_id>", endpoint="remove"),
    Rule("/decrease/<int:product_id>", endpoint="decrease")
])

views = {
    "index": index,
    "cart": cart,
    "remove": remove,
    "decrease":decrease
}

session_store = FilesystemSessionStore(path=gettempdir())


@Request.application
def application(self):
    sid = self.cookies.get("session_id")
    if sid is None:
        self.session = session_store.new()
    else:
        self.session = session_store.get(sid)
    url_adapter = url_map.bind_to_environ(self.environ)
    endpoint, values = url_adapter.match()
    response = views[endpoint](self, **values)
    session_store.save(self.session)
    response.set_cookie("session_id", self.session.sid)
    return response
    
def create_app(with_static=True):
    from werkzeug.middleware.shared_data import SharedDataMiddleware
    import os
    from werkzeug.exceptions import NotFound
    if with_static:
        app = SharedDataMiddleware(application, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == '__main__':
    app = create_app()
    run_simple('localhost', 4041, application)
