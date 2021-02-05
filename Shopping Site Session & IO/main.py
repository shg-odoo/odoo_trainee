from werkzeug.contrib.sessions import FilesystemSessionStore
from tempfile import gettempdir
import json
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound
import os
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from werkzeug.middleware.shared_data import SharedDataMiddleware

def index(self):
    html = open('templates/index.html', 'r').read()
    data = open('item_list.json', 'r').read()
    cartData = 'false'

    if bool(int(self.session.__len__())):
        cartData = self.session['product_ids']
    
    response = Response(html % {'data': str(json.loads(data)),
                                 'cartData': cartData})
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html'
    return response

def cart(self, product_id=None): 
    dataTemp=json.loads(open('item_list.json','r').read())
    qty=0
    for i in dataTemp:
        if i['id']==product_id:
            qty=i['quantity']
            i['quantity']=qty+1
            
    with open('item_list.json','w+') as obj:
        json.dump(dataTemp,obj)
    
    if product_id and not bool(int(self.session.__len__())):
        self.session['product_ids'] = {product_id: product_id}    
    else:
        self.session['product_ids'].update({product_id: product_id})
        
    return index(self)

def remove(self, product_id=None):
    dataTemp=json.loads(open('item_list.json','r').read())
    for i in dataTemp:
        if i['id']==product_id:
            i['quantity']=0
            
    with open('item_list.json','w+') as obj:
        json.dump(dataTemp,obj)
    
    if product_id and bool(int(self.session.__len__())):
        self.session['product_ids'].pop(product_id)
        
    return index(self)

url_map = Map([
    Rule("/", endpoint="index"),
    Rule("/add/to/cart/<int:product_id>", endpoint="cart"),
    Rule("/remove/<int:product_id>", endpoint="remove")
])

views = {
    "index": index,
    "cart": cart,
    "remove": remove
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
    if with_static:
        app = SharedDataMiddleware(application, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app

if __name__ == "__main__":
    app = create_app()
    run_simple("127.0.0.1", 3000, app, use_debugger=True, use_reloader=True)