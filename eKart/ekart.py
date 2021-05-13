import os
import json  # JavaScript Object Notation, data-interchange lan
from werkzeug.wrappers import Request, Response
from werkzeug.middleware.shared_data import SharedDataMiddleware  # serving static files to web server
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule


def home_page(request):
    """
    return a home_page of eKart web application.
    """
    html = open('home_page.html', 'r').read()
    data = open('products.json', 'r').read()

    cartData = 'false'
    if bool(int(request.session.__len__())):
        cartData = request.session['product_ids']
    response = Response(html % {'data': str(json.loads(data)),
                                'cartData': cartData})
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html'
    return response


def my_cart(request, product_id=None):
    """
    Add selected product to cart and return home_page.
    """
    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        request.session['product_ids'].update({product_id: product_id})
    return home_page(request)


def remove_from_cart(request, product_id=None):
    """
    Remove product from my_cart and return home_page.
    """
    if product_id and bool(int(request.session.__len__())):
        request.session['product_ids'].pop(product_id)
    return home_page(request)


# Map stores a bunch of URL rules.
url_map = Map([
    Rule("/", endpoint="home_page"),
    Rule("/add/<int:product_id>", endpoint="my_cart"),
    Rule("/remove/<int:product_id>", endpoint="remove_from_cart")
])

views = {
    "home_page": home_page,
    "my_cart": my_cart,
    "remove_from_cart": remove_from_cart,
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
    run_simple('localhost', 8000, application,  # start a WSGI application
               use_reloader=True,
               use_debugger=True)
