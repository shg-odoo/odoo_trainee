import  os
import json  
from werkzeug.wrappers import Request, Response
from werkzeug.middleware.shared_data import SharedDataMiddleware  
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule

def home_page(request):
    html = open("index.html",'r').read()
    data = open("items.json",'r').read()

    cartData='false'
    if bool(int(request.session.__len__())):
        cartData = request.session['product_ids']

    response = Response(html % {'data':str(json.loads(data)),'cartData':cartData})
    response.status = '200 ok'
    response.headers['content-type'] = 'text/html'
    return response

def my_cart(request,product_id=None):

    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        request.session['product_ids'].update({product_id: product_id})
    return home_page(request)

def remove_from_cart(request,product_id=None):
    print("dsdsk")
    if product_id and bool(int(request.session.__len__())):
        request.session['product_ids'].pop(product_id)
    return home_page(request)
    

def add_in_cart(request,product_id=None):
    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        temp=open('items.json','r+').read()
        print(temp,"--------------------------------1")
        dataTemp=json.loads(temp)
        # product_id['quantity'] += 1
        for i in dataTemp:
            print(i,"-------------------------------2")
            if i['id']==product_id:
                i['quantity']+= 1
                jsonFile = open("items.json", "w")
                json.dump(dataTemp, jsonFile)
                jsonFile.close()
        request.session['product_ids'].update({product_id: product_id})
    return home_page(request)

def remove_in_cart(request,product_id=None):
    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        temp=open('items.json','r+').read()
        print(temp,"--------------------------------1")
        dataTemp=json.loads(temp)
        # product_id['quantity'] += 1
        for i in dataTemp:
            # print(i,"-------------------------------2")
            if i['id']==product_id:
                i['quantity']-= 1
                jsonFile = open("items.json", "w")
                json.dump(dataTemp, jsonFile)
                jsonFile.close()
        request.session['product_ids'].update({product_id: product_id})
    return home_page(request)


url_map = Map([
    Rule("/", endpoint="home_page"),
    Rule("/add/<int:product_id>", endpoint="my_cart"),
    Rule("/remove/<int:product_id>", endpoint="remove_from_cart"),
    Rule("/addin/<int:product_id>", endpoint="add_in_cart"),
    Rule("/removein/<int:product_id>", endpoint="remove_in_cart"),
])

views = {
    "home_page": home_page,
    "my_cart": my_cart,
    "remove_from_cart": remove_from_cart,
    "add_in_cart": add_in_cart,
    "remove_in_cart":remove_in_cart
}

session_store = FilesystemSessionStore(path=gettempdir())


@Request.application
def application(request):
    """
    WSGI application
    """
    ses_id = request.cookies.get("session_id")
    if ses_id is None:
        request.session = session_store.new()
    else:
        request.session = session_store.get(ses_id)

    url_adapter = url_map.bind_to_environ(request.environ)  # bind the url_map to the current request(request.environ)
    # which will return a new MapAdapter, This url_map adapter can then be used to match or build domains for
    # the current request.

    endpoint, values = url_adapter.match()  # match() method can then either return a tuple in the form (endpoint, args)
    # or raise one of the three exceptions NotFound, MethodNotAllowed, or RequestRedirect

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
    run_simple('localhost', 5000, application,  # start a WSGI application
               use_reloader=True,
               use_debugger=True)




    