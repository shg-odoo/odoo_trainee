from werkzeug.wrappers import Request, Response
from jinja2 import Environment, FileSystemLoader
import os
from werkzeug.middleware.shared_data import SharedDataMiddleware


class MovieApp(object):
    """Implements a WSGI application for managing your favorite movies."""
    def __init__(self):
        """Initializes the Jinja templating engine to render from the 'templates' folder."""
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),autoescape=True)

    def render_template(self, template_name, **context):
        """Renders the specified template file using the Jinja templating engine."""
        template = self.jinja_env.get_template(template_name)
        return Response(template.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        """Dispatches the request."""
        return self.render_template('index.html')

    def wsgi_app(self, environ, start_response):
        """WSGI application that processes requests and returns responses."""
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        """The WSGI server calls this method as the WSGI application."""
        return self.wsgi_app(environ, start_response)


def create_app():
    """Application factory function that returns an instance of MovieApp."""
    app = MovieApp()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    return app

if __name__ == '__main__':
    # Run the Werkzeug development server to serve the WSGI application (MovieApp)
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)