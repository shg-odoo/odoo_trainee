import json
import logging
import os
from collections import OrderedDict
import werkzeug
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound
try:
    from werkzeug.middleware.shared_data import SharedDataMiddleware
except ImportError:
    from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.routing import Map
from werkzeug.routing import Rule
from werkzeug.urls import url_parse
from werkzeug.utils import redirect
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response

_logger = logging.getLogger(__name__)

class Application:

    def __init__(self):
        self.template_dict = OrderedDict()
        self.url_map = Map(
            [
                Rule("/", endpoint="index"),
                Rule("/shoping_page", endpoint="shoping_page"),
                Rule("/searchproducts", endpoint="searchProducts")
            ]
        )

    def __call__(self, environ, start_response):
        return self.dispatch(environ, start_response)

    def dispatch(self, environ, start_response):
        request = Request(environ)
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            response = getattr(self, endpoint)(request, **values)
            return response(environ, start_response)
        except HTTPException as e:
            return e

    def index(self, request):
        html = open("templates/index.html", 'r').read()
        return Response(html, mimetype='text/html')

    def shoping_page(self, request, **kwargs):
        data = ""
        with open("static/items.json", "r") as f:
            data = f.read()

        mime = 'application/json'
        result = {'result': data}
        body = json.dumps(result)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

    def searchProducts(self,request):
        data = request.get_data().decode('utf-8')
        data = json.loads(data)        
        searchText=data.get('params')
        value = searchText.get('val')
        products = ""
        with open("static/items.json") as f:
            products = json.load(f)
        searchedResult = []
        if value:
            for product in products:
                if(product.get('name').lower() == value.lower()):
                    searchedResult.append(product)
        else:
            searchedResult = products
        print(searchedResult)
        result = {'result': searchedResult}
        products = json.dumps(result)
        return Response(products, status=200, mimetype='application/json')

def create_app():
    app = Application()
    app.dispatch = SharedDataMiddleware(
        app.dispatch, {"/static": os.path.join(os.path.dirname(__file__), "static")}
    )
    return app

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    application = create_app()
    run_simple("127.0.0.1", 4000, application, use_debugger=True, use_reloader=True)