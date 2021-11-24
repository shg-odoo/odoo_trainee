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
                Rule("/get_products", endpoint="get_products")
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

    def get_products(self, request, **kwargs):
        datas = ""
        with open("static/products.json", "r") as f:
            datas = f.read()

        mime = 'application/json'
        result = {'result': datas}
        body = json.dumps(result)
        return Response(
            body, status=200,
            headers=[('Content-Type', mime), ('Content-Length', len(body))]
        )

def create_app():
    app = Application()
    app.dispatch = SharedDataMiddleware(
        app.dispatch, {"/static": os.path.join(os.path.dirname(__file__), "static")}
    )
    return app

if __name__ == "__main__":
    from werkzeug.serving import run_simple

    application = create_app()
    run_simple("localhost", 5000, application, use_debugger=True, use_reloader=True)