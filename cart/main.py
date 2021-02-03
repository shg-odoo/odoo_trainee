import json
from tempfile import gettempdir
from werkzeug.contrib.sessions import FilesystemSessionStore
from werkzeug.routing import Map, Rule
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response



def index(self):
    html = open('/home/kpt/Desktop/odoo_trainee/cart/index.html', 'r').read()
    data = open('/home/kpt/Desktop/odoo_trainee/cart/items.json', 'r').read()
    cartData = 'false'
    if bool(int(self.session.__len__())):
        cartData = self.session['product_ids']
    response = Response(html % {'data': str(json.loads(data)),
                                'ids': cartData})
    response.headers['content-type'] = 'text/html'
    return response


def cart(self, product_id=None):
    if product_id and not bool(int(self.session.__len__())):
        self.session['product_ids'] = {product_id: product_id}
    else:
        self.session['product_ids'].update({product_id: product_id})
    return index(self)


def remove(self, product_id=None):
    if product_id and bool(int(self.session.__len__())):
        self.session['product_ids'].pop(product_id)
    return index(self)


url_map = Map([
    Rule("/", endpoint="index"),
    Rule("/add/to/cart/<int:product_id>", endpoint="cart"),
    Rule("/Remove/<int:product_id>", endpoint="remove")
])

views = {
    "index": index,
    "cart": cart,
    "remove": remove
}

session_store = FilesystemSessionStore(path=gettempdir())
# print(dir(session_store))


@Request.application
def application(self):
    sid = self.cookies.get("session_id")
    if sid is None:
        self.session = session_store.new()
    else:
        self.session = session_store.get(sid)
    url_adapter = url_map.bind_to_environ(self.environ)
    endpoint, values = url_adapter.match()
    response = views[endpoint](self, **values)
    session_store.save(self.session)
    response.set_cookie("session_id", self.session.sid)
    return response


if __name__ == '__main__':
    run_simple('localhost', 4040, application)
