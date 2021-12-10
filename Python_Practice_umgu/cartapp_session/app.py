from werkzeug.wrappers import Request, Response
import os
from werkzeug.middleware.shared_data import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from tempfile import gettempdir

# pip3 install werkzeug==0.16.0
from werkzeug.contrib.sessions import FilesystemSessionStore

# Reference  :: https://github.com/shg-odoo/odoo_trainee/blob/jido_python_practice/python_prac/application/app.py

class CartApp(object):
    """Implements a WSGI application for managing your web application"""
    def __init__(self):
        """Initializes the Jinja templating engine to render from the 'templates' folder."""
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)

        self.url_map = Map([
            Rule('/', endpoint='index'),
            Rule('/cart.html',endpoint='cart'),
        ])
        self.session_store = FilesystemSessionStore(path=gettempdir());

    def index(self,request):
        return self.render_template('shopping.html')

    def cart(self,request):
        return self.render_template('cart.html')

    def render_template(self, template_name, **context):
        """Renders the specified template file using the Jinja templating engine."""
        template = self.jinja_env.get_template(template_name)
        return Response(template.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        """Dispatches the request."""
        ses_id = request.cookies.get("items")
        print(ses_id)
        if ses_id is None:
            request.session = self.session_store.new()
            # print(request.session.sid)
        else:
            request.session = self.session_store.get(ses_id)
        # request.session['product_ids'] = {"name":"umesh"}
        # print(request.session)

        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            response=getattr(self, endpoint)(request, **values)
            if request.session.should_save:
                self.session_store.save(request.session)
                response.set_cookie("items", request.session.sid)
            return response
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
    run_simple('127.0.0.1', 5555, app, use_debugger=True, use_reloader=True)