from werkzeug.wrappers import Response, Request
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.contrib.sessions import SessionMiddleware, FilesystemSessionStore
import sys
import os
import json
import psycopg2
from werkzeug.wsgi import SharedDataMiddleware
# import time
# DATE = time.asctime(time.localtime(time.time()))
from datetime import *



session_store = FilesystemSessionStore()


url_map=Map([
	Rule('/', endpoint='home'),
	Rule('/index', endpoint='index'),
	Rule('/search', endpoint='search'),
	Rule('/add_to_cart', endpoint='cart'),
	Rule('/remove', endpoint='remove'),
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
	# print(request.session.sid)

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
	# print(b)
	sid = request.cookies.get("session_id")
	# print(sid)
	conn = psycopg2.connect("dbname=kbs user=kbs password=karanbos31..")
	cursor = conn.cursor()
	cursor.execute("set search_path to products;")
	cursor.execute("SELECT COUNT(SESSIONID) FROM USERS WHERE SESSIONID='{}';".format(sid))
	sess = cursor.fetchone()
	cart_f = []
	cart_f_dict={}
	if sess[0] == 0:
		if sid is None:
			request.session = session_store.new()
		else:
			if request.session.should_save:
				session_store.save(request.session)
				request.set_cookie("session_id", request.session.sid)
			
	# response = get_the_response_object(request)
		
		cursor.execute("SELECT COUNT(_ID) FROM USERS;")
		count = cursor.fetchone()
		cursor.execute("SELECT COUNT(_ID) FROM ORDERDET;")
		count_orderdetid = cursor.fetchone()
		cursor.execute("INSERT INTO USERS(_ID, SESSIONID) VALUES({0}, '{1}');".format(count[0]+1, sid))
		cursor.execute("SELECT COUNT(_ID) FROM ORDERS;")
		count_orderid = cursor.fetchone()
		# print(count_orderid)
		# now = datetime.now()

		# timestamp = datetime.timestamp(now)
		DATE = datetime.now()
		# DATE.strftime("%d-%m-%y")
		cursor.execute("INSERT INTO ORDERS(_ID, DATE, USERID) VALUES({0}, '{1}', {2});".format(count_orderid[0]+1, DATE.strftime("%d-%m-%y"), count[0]+1))
		cursor.execute("INSERT INTO ORDERDET(_ID, ORDERID, QUANTITY, PRODUCTID) VALUES({0}, {1}, {2}, {3});".format(count_orderdetid[0]+1, count_orderid[0]+1,  1, b['product-id']))
	elif sess[0] == 1:
		request.session = session_store
		sid = request.session.get("session_id")
		cursor.execute("SELECT * FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDERS._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='{}';".format(sid))
		cursor.execute("SELECT COUNT(ORDERDET._ID) FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDERS._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='{}';".format(sid))
		count= cursor.fetchone()
		# print(count)
		if count[0] != 0:
			cursor.execute("SELECT ORDERDET.ORDERID, ORDERDET.QUANTITY FROM ORDERDET INNER JOIN ORDERS ON ORDERDET.ORDERID = ORDERS._ID INNER JOIN PRODUCT ON ORDERDET.PRODUCTID = PRODUCT._ID INNER JOIN USERS ON ORDERS.USERID=USERS._ID WHERE USERS.SESSIONID='None';")
			quantity = cursor.fetchone()
			cursor.execute("UPDATE ORDERDET SET QUANTITY= {0} where orderid={1};".format(quantity[1]+1, quantity[0]))
		elif count[0] == 0:
			cursor.execute("SELECT COUNT(_ID) FROM ORDERS;")
			count_orderid = cursor.fetchone()
			cursor.execute("SELECT MAX(_ID) FROM ORDERDET;")
			count_orderdetid = cursor.fetchone()
			print(count_orderdetid[0])
			cursor.execute("INSERT INTO ORDERDET(_ID, ORDERID, QUANTITY, PRODUCTID) VALUES({0}, {1}, {2}, {3});".format(count_orderdetid[0]+1, count_orderid[0],  1, b['product-id']))
	conn.commit()
	# print(sid)
	cursor.execute("SELECT _ID FROM USERS where sessionid='f{sid}';")
	count_userid = cursor.fetchone()
	# print(count_userid)

	# cursor.execute("SELECT _ID FROM ORDERS WHERE USERID=`{}`;".format(count_userid[0]))
	# count_orderid = cursor.fetchone()
	# print(count_orderid)
	cursor.execute("SELECT ORDERDET.PRODUCTID, PRODUCT.NAME, SUM(ORDERDET.QUANTITY), SUM(PRODUCT.PRICE) from orderdet INNER JOIN PRODUCT ON ORDERDET.PRODUCTID= PRODUCT._ID where ORDERDET.ORDERID ={} GROUP BY ORDERDET.ORDERID, ORDERDET.PRODUCTID, PRODUCT.NAME, ORDERDET.QUANTITY ORDER BY ORDERDET.PRODUCTID;".format(count_orderid[0]))
	cart_det = cursor.fetchall()
	print(cart_det)
	for i in cart_det:
		zc = 0
		cart_f_dict["product_id"]=i[0]
		cart_f_dict["product_name"]=i[1]
		cart_f_dict["quantity"]=i[2]
		cart_f_dict["amount"]=i[3]
		cart_f.append(dict(cart_f_dict))
	print(cart_f)
	# cursor.execute("SELECT * FROM USERS inner join orders on orders.userid = users._id inner join orderdet on orderdet.orderid = orders._id inner join product on product._id = orderdet.productid;")
	text=json.dumps(cart_f)
	cursor.close()
	conn.close()
	# print(b)
	# print(text)
	# text='<!DOCTYPE html><html><style>body{color: red;}</style><body><b><u>Welcome to the %s</u></b></body></html>' % request.args.get('name', 'homepage')
	response=Response(text, mimetype='application/json')
	return response

def remove(request,args):
	a=json.loads(request.data)
	sid = request.cookies.get("session_id")
	print(a)
	cart_fr=[]
	cart_fr_dict={}
	conn = psycopg2.connect("dbname=kbs user=kbs password=karanbos31..")
	cursor = conn.cursor()
	cursor.execute("set search_path to products;")
	cursor.execute("SELECT ORDERS._ID FROM ORDERS INNER JOIN USERS ON ORDERS.USERID = USERS._ID WHERE USERS.SESSIONID='None';")
	order_id = cursor.fetchone()
	cursor.execute("SELECT _ID FROM ORDERDET WHERE ORDERID = {0} AND PRODUCTID = {1} ORDER BY _ID DESC LIMIT 1;".format(order_id[0], a['data-id']))
	removeid = cursor.fetchone()
	cursor.execute("DELETE FROM ORDERDET WHERE _ID = {0}".format(removeid[0]))
	# cursor.execute("SELECT SUM(ORDERDET.QUANTITY) from orderdet WHERE PRODUCTID = {} AND ORDERID ={} GROUP BY ORDERDET.ORDERID, ORDERDET.PRODUCTID, ORDERDET.QUANTITY;".format(a['data-id'], order_id[0]))
	cursor.execute("SELECT ORDERDET.PRODUCTID, PRODUCT.NAME, SUM(ORDERDET.QUANTITY), SUM(PRODUCT.PRICE) from orderdet INNER JOIN PRODUCT ON ORDERDET.PRODUCTID= PRODUCT._ID where ORDERDET.ORDERID ={} GROUP BY ORDERDET.ORDERID, ORDERDET.PRODUCTID, PRODUCT.NAME, ORDERDET.QUANTITY ORDER BY ORDERDET.PRODUCTID;".format(order_id[0]))
	line = cursor.fetchall()
	print(line)
	conn.commit()
	for i in line:
	 	cart_fr_dict["product_id"]=i[0]
	 	cart_fr_dict["product_name"]=i[1]
	 	cart_fr_dict["quantity"]=i[2]
	 	cart_fr_dict["amount"]=i[3]
	 	cart_fr.append(dict(cart_fr_dict))
	print(cart_fr)
	text=json.dumps(cart_fr)
	cursor.close()
	conn.close()

	# quantity_r = cursor.fetchone()
	# cursor.execute("UPDATE ORDERDET SET QUANTITY= {0} where orderid={1};".format(quantity_r[0]-1, order_id[0]))
	response=Response(text, mimetype='application/json')
	return response



if __name__ =='__main__':
	from werkzeug.serving import run_simple
	application = SharedDataMiddleware(application, {'/Static': os.path.join(os.path.dirname(__file__), 'Static')})
	run_simple('localhost', 8080, application, use_reloader=True)
