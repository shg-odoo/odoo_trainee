#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response


def index(request):
    html = open('shop.html', 'r').read()
    data = open('product.json', 'r').read()
    cartData = 'false'
    if bool(int(request.session.__len__())):
        cartData = request.session['product_ids']
    response = Response(html % {'data': str(json.loads(data)),
                                'cartData': cartData})
    response.status = '200 OK'
    response.headers['content-type'] = 'text/html'
    return response


def cart(request, product_id=None):
    if product_id and not bool(int(request.session.__len__())):
        request.session['product_ids'] = {product_id: product_id}
    else:
        request.session['product_ids'].update({product_id: product_id})
    return index(request)


def remove(request, product_id=None):
    if product_id and bool(int(request.session.__len__())):
        request.session['product_ids'].pop(product_id)
    return index(request)


url_map = Map([
    Rule("/", endpoint="index"),
    Rule("/add/to/cart/<int:product_id>", endpoint="cart"),
    Rule("/remove/<int:product_id>", endpoint="remove")
])

views = {
    "index": index,
    "cart": cart,
    "remove": remove
}


session_store = FilesystemSessionStore(path=gettempdir())

@Request.application
def application(request):
    sid = request.cookies.get("session_id")
    if sid is None:
        request.session = session_store.new()
    else:
        request.session = session_store.get(sid)
    url_adapter = url_map.bind_to_environ(request.environ)
    endpoint, values = url_adapter.match()
    response = views[endpoint](request, **values)
    session_store.save(request.session)
    response.set_cookie("session_id", request.session.sid)
    return response

if __name__ == '__main__':
    run_simple('localhost',3000, application)
