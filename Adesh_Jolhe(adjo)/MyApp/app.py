import os
import json  
from werkzeug.wrappers import Request, Response
from werkzeug.wsgi import SharedDataMiddleware
#from werkzeug.middleware.shared_data import SharedDataMiddleware  
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule

def home_page(request):
    html = open("index.html",'r').read()
    data = open("items.json",'r').read()

    cartData='false'
    if bool(int(request.session.__len__())):
        cartData = request.session['product_ids']
        

    response = Response(html % {'data':str(json.loads(data)),'cartData':cartData,'cart':request.session['product_ids']})
    response.status = '200 ok'
    response.headers['content-type'] = 'text/html'
    return response

def add_to_cart(request,product_id=None):

    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        request.session['product_ids'].update({product_id: product_id})
    
    return Response(json.dumps({'cart':request.session},sort_keys=True),content_type="application/json")

def remove_from_cart(request,product_id=None):  
    
    if product_id and bool(int(request.session.__len__()) and request.session['product_ids'].get(product_id) != None):
        del request.session['product_ids'][product_id]
    # print(request.session['product_ids'])
    return Response(json.dumps(request.session,sort_keys=True),content_type="application/json")

def get_cart(request):
    return Response(json.dumps(request.session,sort_keys=True),content_type="application/json")




url_map = Map([
    Rule("/", endpoint="home_page"),
    Rule("/add/<int:product_id>", endpoint="add_to_cart"),
    Rule("/remove/<int:product_id>", endpoint="remove_from_cart"),
    Rule("/get-cart",endpoint="get_cart")
])

views = {
    "home_page": home_page,
    "add_to_cart": add_to_cart,
    "remove_from_cart": remove_from_cart,
    "get_cart": get_cart,
}

session_store = FilesystemSessionStore(path=gettempdir())


@Request.application
def application(request):
    """
    WSGI application 
    """
    session_id = request.cookies.get("session_id")
    if session_id is None:
        request.session = session_store.new()
    else:
        request.session = session_store.get(session_id)

    url_adapter = url_map.bind_to_environ(request.environ)

    endpoint, values = url_adapter.match()  
    response = views[endpoint](request, **values)
    
    session_store.save(request.session)
    
    response.set_cookie("session_id", request.session.sid)
    return response


def create_app():
    my_app = SharedDataMiddleware(application, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    return my_app


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple('localhost', 8000, application,  # start a WSGI application
               use_reloader=True,
               use_debugger=True)
