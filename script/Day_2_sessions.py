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
	sid = request.cookies.get("session_id")

	if sid is None:
		request.session = session_store.new()
	else:
		request.session = session_store.get(sid)
	# response = get_the_response_object(request)
	if request.session.should_save:
		session_store.save(request.session)
		request.set_cookie("session_id", request.session.sid)
	print(request.session.sid)

	# sid = request.session.sid
	# print(get(sid))
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
		# print(new_dict)
		# print(product)
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
	sid = request.cookies.get("session_id")
	conn = psycopg2.connect("dbname=kbs user=kbs password=karanbos31..")
	cursor = conn.cursor()
	cursor.execute("set search_path to products;")
	cursor.execute("SELECT COUNT(SESSIONID) FROM USERS WHERE SESSIONID='{}';".format(sid))
	sess = cursor.fetchone()
	if sess[0] == 0;
		cursor.execute("SELECT COUNT(_ID) FROM USERS;")
		count = cursor.fetchall()
		cursor.execute("INSERT INTO USERS(_ID, SESSIONID) VALUES({0}, '{1}');".format(count[0]+1, sid))
		cursor.execute("SELECT COUNT(_ID) FROM ORDERS;")
		count_orderid = cursor.fetchone()
		cursor.execute("INSERT INTO ORDERS(_ID, DATE, USERID) VALUES({0}, {1}, {2});".format(count_orderid[0]+1, DATE, count[0]+1))
		cursor.execute("INSERT INTO ORDERDET(_ID, ORDERID, QUANTITY, PRODUCTID) VALUES({0}, {1}, {2}, {3});".format(count[0]+1, count_orderid[0]+1,  1, b['product-id']))
	elif sess[0] == 1;
		cursor.execute("SELECT * FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDER._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='{}';".format(sid))
		cursor.execute("SELECT COUNT(ORDERDET._ID) FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDERS._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='{}';".format(sid))
		count= cursor.fetchone()
		if count[0]>0:
			cursor.execute("SELECT ORDERDET.ORDERID, ORDERDET.QUANTITY FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDERS._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='{}';".format(sid))
			quantity = cursor.fetchone()
			cursor.execute("UPDATE ORDERDET SET QUANTITY= {0} where orderid={1};".format(quantity[1]+1, quantity[0]))
		elif count[0]==0:
			cursor.execute("SELECT COUNT(_ID) FROM ORDERS;")
			count_orderid = cursor.fetchone()
			cursor.execute("INSERT INTO ORDERDET(_ID, ORDERID, QUANTITY, PRODUCTID) VALUES({0}, {1}, {2}, {3});".format(count[0]+1, count_orderid[0]+1,  1, b['product-id']))
	conn.commit()

	# cursor.execute("SELECT * FROM USERS inner join orders on orders.userid = users._id inner join orderdet on orderdet.orderid = orders._id inner join product on product._id = orderdet.productid;")
	cursor.close()
	conn.close()
	# print(b)

	# text='<!DOCTYPE html><html><style>body{color: red;}</style><body><b><u>Welcome to the %s</u></b></body></html>' % request.args.get('name', 'homepage')
	response=Response(b, mimetype='text/json')
	return response


if __name__ =='__main__':
	from werkzeug.serving import run_simple
	application = SharedDataMiddleware(application, {'/Static': os.path.join(os.path.dirname(__file__), 'Static')})
	run_simple('localhost', 8080, application, use_reloader=True)
