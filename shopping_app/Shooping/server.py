import os
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.wrappers import Request, Response
from jinja2 import Environment, FileSystemLoader
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
import json
from werkzeug.utils import redirect

cart_file = "/home/gautami/odoo_trainee/shopping_app/Shooping/static/json_file/cart.json"
items_file = "/home/gautami/odoo_trainee/shopping_app/Shooping/static/json_file/items.json"

class ShoppingApp:
    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                 autoescape=True)

        self.url_map = Map([
        Rule('/', endpoint='index'),
        Rule('/add_items', endpoint='add_items',methods=['GET','POST']),
        Rule('/save_data', endpoint='save_data',methods=['GET','POST']),
        Rule('/cart',endpoint='cart',methods=['GET','POST']),
        Rule('/update',endpoint='update',methods=['GET','POST']),
        Rule('/delete',endpoint='delete',methods=['GET','POST']),
        Rule('/save_update', endpoint='save_update', methods=['GET', 'POST']),
        Rule('/new_user_form', endpoint='new_user_form', methods=['GET', 'POST']),
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(request, **values)
        except NotFound:
            return self.error_404()
        except HTTPException as e:
            return e

    #----Reading JSON file ---

    def read_json(self,request,file_path):
        with open(file_path,"r") as f:
            try:
                temp = json.load(f)
                return temp
            except Exception as e:
                return "empty"

    #----writing JSON file---

    def write_json(self,request,id,name,price,fun_type,qty=None,new_qty=None):
        item_list = {}
        item_list["id"] = id
        item_list["name"] = name
        item_list["price"] = price

        def write_append_data(file_name,data):
            with open(file_name, "w") as fp:
                json.dump(data, fp, indent=4)

        if fun_type == "cart" and qty!= None:
            item_list["quantity"] = qty
            total_price = int(price) * int(qty)
            item_list["total_price"] = str(total_price)
            temp = self.read_json(request,file_path=cart_file)
            if temp == "empty":
                data = [item_list]
                write_append_data(cart_file,data)
            else:
                temp.append(item_list)
                write_append_data(cart_file,temp)

        elif fun_type == 'add_items' and qty == None:
            temp = self.read_json(request,file_path=items_file)
            if temp == "empty":
                data = [item_list]
                write_append_data(items_file,data)
            else:
                temp.append(item_list)
                write_append_data(items_file,temp)
        else:
            new_data = []
            idnum = id
            name = name
            price = price
            qty = qty
            newqty = new_qty
            temp = self.read_json(request, file_path=cart_file)
            if fun_type == 'update':
                for x in temp:
                    if x['id'] == idnum and x['name'] == name and x['price'] == price and x['quantity'] == qty:
                        new_data.append({"id": idnum, "name": name, "price": price, "quantity": newqty})
                    else:
                        new_data.append(x)
                write_append_data(cart_file, new_data)
            else:
                for x in temp:
                    if x['id'] == idnum and x['name'] == name and x['price'] == price and x['quantity'] == qty:
                        del x
                    else:
                        new_data.append(x)
                write_append_data(cart_file, new_data)


    def index(self, request):
        d1 = self.read_json(request,file_path=items_file)
        if d1 == 'empty':
            msg = "Sorry data is not available"
            return self.render_template('base.html', msg = msg)
        else:
            return self.render_template('base.html',data=d1)

    def add_items(self, request):
        if request.method == 'POST':
            self.write_json(request, id=request.form['id'], name=request.form['name'], price=request.form['price'],
                            fun_type="add_items")
                            
            return self.render_template('add_items.html')
        else:
            return self.render_template('add_items.html')

    def cart(self,request):
        def total(data):
            total= sum(int(item['total_price']) for item in data)
            return total

        if request.method == 'POST':
            self.write_json(request,id=request.form['id'],name=request.form['name'],price=request.form['price'],fun_type="cart",qty=request.form['Quantity'])
            temp = self.read_json(request, file_path=cart_file)
            total_amt = total(temp)
            return self.render_template('cart.html', data=temp,total=total_amt)
        else:
            temp = self.read_json(request, file_path=cart_file)
            if temp == 'empty':
                msg = "Sorry your cart is empty"
                total_amt = total(temp)
                return self.render_template('cart.html', msg=msg,total=total_amt)
            else:
                total_amt = total(temp)
                return self.render_template('cart.html', data=temp,total=total_amt)

    def update(self,request):
        if request.method == 'POST':
            idnum = request.form['idnum']
            name = request.form['name']
            price = request.form['price']
            qty = request.form['qty']
            return self.render_template('update_cart.html', idnum=idnum,name=name,price=price,qty=qty)

    def save_update(self,request):
        self.write_json(request, id=request.form['idnum'], name=request.form['name'], price=request.form['price'],
                        fun_type="update",qty=request.form['qty'],new_qty = request.form['new_qty'])
        return redirect('/cart')

    def delete(self,request):
        self.write_json(request, id=request.form['idnum'], name=request.form['name'], price=request.form['price'],
                            fun_type="delete", qty=request.form['qty'])
        return redirect('/cart')

    def new_user_form(self,request):
        if request.method == 'POST':
            name = request.form['id']
            price = request.form['name']
            idnum = request.form['price']
            print(name,"-----",price,"----",idnum)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def render_template(self, template_name, **context):
        template = self.jinja_env.get_template(template_name)
        return Response(template.render(context), mimetype='text/html')

    def error_404(self):
        response = self.render_template("404.html")
        response.status_code = 404
        return response

def create_app():
    app = ShoppingApp()
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 8000, app, use_debugger=True, use_reloader=True)