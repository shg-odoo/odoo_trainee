from werkzeug.wrappers import Response, Request
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.contrib.sessions import SessionMiddleware, FilesystemSessionStore
import sys
import os
import json
import psycopg2
from werkzeug.wsgi import SharedDataMiddleware
session_store = FilesystemSessionStore()


url_map=Map([
	Rule('/', endpoint='home'),
	Rule('/index', endpoint='index'),
	Rule('/search', endpoint='search'),
	Rule('/add_to_cart', endpoint='cart'),
	Rule('/javascr.js', endpoint='javascr')
	])


def application(environ, start_response):
	request = Request(environ)
	
	urls=url_map.bind_to_environ(environ)
	endpoint, args=urls.match()
	current_module = sys.modules[__name__]
	method_name = endpoint
	response = getattr(current_module, method_name)(request, args)
	#if endpoint=='index':
	#	response = do_index(request, args)
	#elif endpoint=='blog':
	#	response = do_blog(request, args)
	#elif endpoint=='karan':
	#	response = do_karan(request,args)
	#elif endpoint=='karanhome':
	#	response=do_karanhome(request,args)
	sid = request.cookies.get('cookie')
	if sid is None:
		request.session = session_store.new()
	else:
		request.session = session_store.get(sid)
	if request.session.should_save:
		session_store.save(request.session)
		response.set_cookie('cookie_name', request.session.sid)

	return response(environ, start_response)

# def javascr(request, args):
# 	text = '%s' %request.args.get('name', '<script type="text/javascript" src="javascr.js"></script>')
# 	response = Response(text, mimetype='text/plain')
# 	return response

def home(request, args):
	text = '<!DOCTYPE html><html><head><script type="text/javascript" src="Static/javascr.js"></script></head><body><div id="container"></div></body></html>'
	response = Response(text, mimetype='text/html')
	return response

def index(request,args):
	text='Hi, This is my %s' % request.args.get('name', 'blog')
	response = Response(text, mimetype='text/plain')
	return response

def search(request, args):
	product = []
	productdict={}
	new_dict={}
	conn = psycopg2.connect("dbname=kbs user=kbs password=karanbos31..")
	dat = json.loads(request.data)
	# print(args)
	cursor = conn.cursor()
	cursor.execute("set search_path to products;")
	cursor.execute("""SELECT * FROM Product where name like '%{}%' """.format(dat['value']))
	# conn.commit()
	product_s = cursor.fetchall()
	for row in product_s:
		i=0
		productdict["_id"]=row[0]
		productdict["name"] = row[1]
		productdict["price"] = row[2]
		# print(productdict)
		product.append(dict(productdict))
		new_dict[i] = row
		i+=1
		print(new_dict)
	# print(product)
	text=json.dumps(product)
	cursor.close()
	conn.close()
	# print(text)
	response = Response(text, mimetype='application/json')
	return response

def cart(request, args):
	a = request.data
	b = json.loads(a)
	print(b)
	text='<!DOCTYPE html><html><style>body{color: red;}</style><body><b><u>Welcome to the %s</u></b></body></html>' % request.args.get('name', 'homepage')
	response=Response(text, mimetype='text/html')
	return response


if __name__ =='__main__':
	from werkzeug.serving import run_simple
	application = SharedDataMiddleware(application, {'/Static': os.path.join(os.path.dirname(__file__), 'Static')})
	run_simple('localhost', 8080, application, use_reloader=True)
