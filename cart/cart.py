import os
import redis
from jinja2 import Environment
from jinja2 import FileSystemLoader
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.routing import Map
from werkzeug.routing import Rule
from werkzeug.urls import url_parse
from werkzeug.utils import redirect
from werkzeug.wrappers import Request
from werkzeug.wrappers import Response
import psycopg2

connection = psycopg2.connect(dbname='kpt', user='postgres',password='123456',host='localhost')

cursor = connection.cursor()
cursor.execute('select *  from products')
for item in cursor:
    print(item)




class Cart(object):
    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_path), autoescape=True)
        self.url_map = Map([
            Rule('/', endpoint='home'),
            # Rule('/', endpoint="search"),
            # Rule('/<short_id>+', endpoint='short_link_details')
        ])

    def on_home(self, request):
        resultSet = []
        # item = []
        error = None
        url = ''
        if request.method == 'POST':
            search_item = request.form['search']
            searchItem = search_item.capitalize()
            cursor.execute("select product_name, product_price from products where product_name= %s",[searchItem])
            for row in cursor:
                resultSet.append(row)
                print(resultSet)
            return self.render_template('index.html', resultset = resultSet, error=error, url=url)
        

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        try:
            adapter = self.url_map.bind_to_environ(request.environ)
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)




def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Cart({
        'redis_host':       redis_host,
        'redis_port':       redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)


cursor.close()
connection.close()