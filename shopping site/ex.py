# Python Online shopping Web Application without using any framwork
# I used here the liabrary called werkzeug.

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
import pandas as pd
import json


def base36_encode(number):
    assert number >= 0, "positive integer required"
    if number == 0:
        return "0"
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append("0123456789abcdefghijklmnopqrstuvwxyz"[i])
    return "".join(reversed(base36))


def is_valid_url(url):
    parts = url_parse(url)
    return parts.scheme in ("http", "https")


def get_hostname(url):
    return url_parse(url).netloc

class Shortly:
    def __init__(self, config):
        self.redis = redis.Redis(config["redis_host"], config["redis_port"])
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        self.jinja_env = Environment(
            loader=FileSystemLoader(template_path), autoescape=True
        )
        self.jinja_env.filters["hostname"] = get_hostname

        self.url_map = Map(
            [
                Rule("/", endpoint="home"),
                Rule("/add", endpoint="add_item"),
                Rule("/fill", endpoint="fill_data")
            ]
        )

    
    def on_home(self, request):
    	df = pd.read_csv('static/data.csv')
    	image = []
    	title = []
    	desc = []
    	for i in df['image']:
    		image.append(i)
    	for i in df['title']:
    		title.append(i)
    	for i in df['desc']:
    		desc.append(i)
    	data = zip(image, title, desc)
    	return self.render_template("index.html", context=data)

    def on_add_item(self, request):
    	return self.render_template("add.html")

    def on_fill_data(self, request):
    	if request.method == "POST":
    		image = request.get["image"]
    		title = request.get["title"]
    		desc = request.get["desc"]
    		datas = {"image": image, "title": title, "desc": desc}
    		jsonString = json.dumps(datas)
    		jsonFile = open('static/data.json', 'w')
    		jsonFile.write(jsonString)
    		jsonFile.close()
    		return redirect("/")
    	return redirect("/")


    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype="text/html")

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f"on_{endpoint}")(request, **values)
        except NotFound:
            return self.error_404()
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app(redis_host="localhost", redis_port=6379, with_static=True):
    app = Shortly({"redis_host": redis_host, "redis_port": redis_port})
    if with_static:
        app.wsgi_app = SharedDataMiddleware(
            app.wsgi_app, {"/static": os.path.join(os.path.dirname(__file__), "static")}
        )
    return app


if __name__ == "__main__":
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)