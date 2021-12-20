from werkzeug.wrappers import Request, Response
import os
from werkzeug.middleware.shared_data import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from tempfile import gettempdir
import json

class CartApp(object):
    """Implements a WSGI application for managing your web application"""
    def __init__(self):
        """Initializes the Jinja templating engine to render from the 'templates' folder."""
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/products', endpoint='setProducts'),
            Rule('/search', endpoint='searchProducts')
            
        ])
        # self.session_store = FilesystemSessionStore(path=gettempdir());

    def index(self,request):
        return self.render_template('index.html')

    def setProducts(self, request):
        products = ""
        with open("static/json/products.json") as f:
            products = f.read()

        result = {'result': products}
        products = json.dumps(result)
        return Response(products, status=200, mimetype='application/json')

    def searchProducts(self,request):
        searchText=request.args['searchText'].lower()
        products = ""
        with open("static/json/products.json") as f:
            products = json.load(f)

        searchedResult=json.dumps({})
        for category in products:
            if(searchText == category):
                searchedResult = json.dumps({category : products[category]})
        result = {'result': searchedResult}
        products = json.dumps(result)

        return Response(products, status=200, mimetype='application/json')

    def render_template(self, template_name, **context):
        """Renders the specified template file using the Jinja templating engine."""
        template = self.jinja_env.get_template(template_name)
        return Response(template.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        """Dispatches the request."""
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        """WSGI application that processes requests and returns responses."""
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        """The WSGI server calls this method as the WSGI application."""
        return self.wsgi_app(environ, start_response)


def create_app():
    """Application factory function that returns an instance of CartApp"""
    app = CartApp()
    app.wsgi_app=SharedDataMiddleware(app.wsgi_app, {'/static' : os.path.join(os.path.dirname(__file__),'static')})
    return app

if __name__ == '__main__':
    # Run the Werkzeug development server to serve the WSGI application ()
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 8001, app, use_debugger=True, use_reloader=True)
