#!/usr/bin/env python3

import json
import psycopg2
import threading
import time
import uuid

from connections import Connection
from http.server import SimpleHTTPRequestHandler, HTTPServer
from psycopg2 import Error
from urllib.parse import parse_qs

class myHandler(SimpleHTTPRequestHandler):
    db_connection = Connection()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        if self.path == '/do_signup':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            chk_eml = self.db_connection.chk_eml(data)
            if chk_eml is None: 
                user_data = self.db_connection.create_user(data)
                return self.wfile.write(json.dumps({'credentials': True}).encode()) 
            else:
                return self.wfile.write(json.dumps({'credentials': False}).encode())    
        elif self.path == '/do_signup_engineer':  
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            chk_eml = self.db_connection.chk_eml(data)
            if chk_eml is None: 
                user_data = self.db_connection.create_user_engineer(data)
                return self.wfile.write(json.dumps({'credentials': True}).encode())
            else:
                return self.wfile.write(json.dumps({'credentials': False}).encode())     
        elif self.path == '/do_login': 
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user_data = self.db_connection.user_exists(data)
            get_user_role = self.db_connection.get_user_role(data)
            get_username = self.db_connection.get_username(data)
            if user_data is None:
                chk_eml = self.db_connection.chk_eml(data)
                chk_pass = self.db_connection.chk_pass(data)
                if chk_eml is None:
                    return self.wfile.write(json.dumps({'email': False}).encode())
                elif chk_pass is None:
                    return self.wfile.write(json.dumps({'pass': False}).encode())
            else:
                session_id = str(uuid.uuid4())
                self.db_connection.create_user_session(session_id, user_data[0])
                if "client" in get_user_role:
                    return self.wfile.write(json.dumps({'session_id': session_id, 'user_id': user_data[0],'fname': get_username, 'is_valid': True, 'role':"client"}).encode())
                else:
                    return self.wfile.write(json.dumps({'session_id': session_id, 'user_id': user_data[0],'fname': get_username, 'is_valid': True, 'role':"engineer"}).encode())


        elif self.path == '/session_validate':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user = self.db_connection.session_validate(data)
            if user is None:
                return self.wfile.write(json.dumps({'valid': True}).encode())
            else:
                return self.wfile.write(json.dumps({'valid': False}).encode())
        elif self.path == '/do_logout':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            user_data = self.db_connection.user_logout(data)
            return self.wfile.write(json.dumps({'logout': "success"}).encode())

# ----------------------Client Side-------------------------------------------------

        elif self.path == '/client_engineer_list':
            user_data = self.db_connection.fetch_engineer_data()
            data_list = list()  
            for engineer_list in user_data:                                
                engineer_list={
                    'engineer_id': engineer_list[0],
                    'email': engineer_list[2],
                    'mobile_no': engineer_list[7],
                    'specialist': engineer_list[8], 
                    'experience': engineer_list[9],
                }
                data_list.append(engineer_list)

            return self.wfile.write(json.dumps({'engineer_list': data_list}).encode())

        elif self.path == '/book_engineer':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            get_engineer_info = self.db_connection.get_engineer_info(data)
            book_engineer = self.db_connection.book_engineer(data['fname'],get_engineer_info)
            return self.wfile.write(json.dumps({'book_engineer': "success"}).encode())

        elif self.path == '/view_engineer_detail':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            result = self.db_connection.fetch_view_engineer_detail(data)
            result_data = list()
            for view_engineer_list in result:                                
                view_engineer_list={
                    'engineer_id': view_engineer_list[0],
                    'email': view_engineer_list[2],
                    'fname': view_engineer_list[3],
                    'mobile_no': view_engineer_list[7],
                    'specialist': view_engineer_list[8],
                    'experience': view_engineer_list[9],
                }
                result_data.append(view_engineer_list)
            return self.wfile.write(json.dumps({'view_engineer_detail': result_data}).encode())

        elif self.path == '/do_fetch_orders':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            order = self.db_connection.fetch_order_list(data['fname'])
            final_order_list = list()
            for order_list in order: 
                order_list={
                    'order_id': order_list[0],
                    'fname': order_list[1],
                    'created_day':order_list[2].day,
                    'created_month':order_list[2].month,
                    'created_year':order_list[2].year,
                    'created_hour':order_list[2].hour,
                    'created_minute':order_list[2].minute,

                }
                final_order_list.append(order_list)
            return self.wfile.write(json.dumps({'engineer_list': final_order_list}).encode())
        
        elif self.path == '/view_orders_detail':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            result = self.db_connection.fetch_view_engineer_orders_detail(data)
            result_data = list()
            for view_orders_list in result:                                
                view_orders_list={
                    'order_id': view_orders_list[0],
                    'eng_name': view_orders_list[1],
                    'created_day':view_orders_list[2].day,
                    'created_month':view_orders_list[2].month,
                    'created_year':view_orders_list[2].year,
                    'created_hour':view_orders_list[2].hour,
                    'created_minute':view_orders_list[2].minute,
                    'mobile_no': view_orders_list[3],
                    'specialist': view_orders_list[4],
                    'experience': view_orders_list[5],
                    'email': view_orders_list[6],
                }
                result_data.append(view_orders_list)
            return self.wfile.write(json.dumps({'view_orders_detail': result_data}).encode()) 

        elif self.path == '/do_fetch_client_profile':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            result = self.db_connection.fetch_client_profile(data)
            data_list = list()
            for client_profile in result:                                
                profile_list={
                    'id': client_profile[0],
                    'fname': client_profile[3],
                    'email': client_profile[2],
                    'address': client_profile[5],
                    'mobile_no': client_profile[7],
                }
                data_list.append(profile_list)

            return self.wfile.write(json.dumps({'client_profile': data_list}).encode())
            
# ----------------------Engineer Side-------------------------------------------------
        elif self.path == '/do_fetch_jobs':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            result = self.db_connection.fetch_arrives_jobs_data(data)
            data_list = list()
            for arrives_jobs in result:                                
                job_list={
                    'order_id':arrives_jobs[0],
                    'client_name': arrives_jobs[1],
                    'mobile_no': arrives_jobs[2],
                    'address': arrives_jobs[3],
                    'created_day':arrives_jobs[4].day,
                    'created_month':arrives_jobs[4].month,
                    'created_year':arrives_jobs[4].year,
                    'created_hour':arrives_jobs[4].hour,
                    'created_minute':arrives_jobs[4].minute,
                }
                data_list.append(job_list)

            return self.wfile.write(json.dumps({'arrives_jobs': data_list}).encode())
        
        elif self.path == '/do_fetch_engineer_profile':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            result = self.db_connection.fetch_engineer_profile(data)
            data_list = list()
            for engineer_profile in result:                                
                profile_list={
                    'id': engineer_profile[0],
                    'fname': engineer_profile[2],
                    'email': engineer_profile[3],
                    'address': engineer_profile[5],
                    'mobile_no': engineer_profile[7],
                    'specialist': engineer_profile[8],
                    'experience': engineer_profile[9],
                }
                data_list.append(profile_list)

            return self.wfile.write(json.dumps({'engineer_profile': data_list}).encode())

        elif self.path == '/view_job_detail':
            data = self.rfile.read(int(self.headers.get('Content-Length')))
            data = json.loads(data)
            print(data['order_id'])
            result = self.db_connection.fetch_view_client_job_detail(data)
            result_data = list()
            for view_job_list in result:                                
                view_job={
                    'order_id': view_job_list[0],
                    'client_name': view_job_list[1],
                    'created_day':view_job_list[2].day,
                    'created_month':view_job_list[2].month,
                    'created_year':view_job_list[2].year,
                    'created_hour':view_job_list[2].hour,
                    'created_minute':view_job_list[2].minute,
                    'mobile_no': view_job_list[3],
                    'address': view_job_list[4],
                    'email': view_job_list[5],
                }
                result_data.append(view_job)
            return self.wfile.write(json.dumps({'view_job_list': result_data}).encode()) 


    def do_GET(self):
        if self.path in ['/', '/signup', '/signupEngineer', '/login', '/homee', '/engineers', '/jobs', '/new_jobs', '/profile', '/home', '/engineerslist', '/engineerslist','/view_engineer_detail','/orders','/profilee','/view_orders_detail','/view_engineer_detail','/view_jobs_detail']:
            with open('index.html') as f:
                Cookie = self.headers.get('Cookie')
                session_id = False  
                html = f.read()
                session_info = {
                    'user_id': None,
                    'is_valid': False,
                }
                if Cookie:
                    session_cookie = parse_qs(Cookie.replace(' ', ''))
                    if session_cookie.get('session_id'):
                        session_id = session_cookie.get('session_id')[0]
                        user = self.db_connection.session_validate({'session_id': session_id})
                        role = self.db_connection.get_user_role_session_val({'session_id': session_id})
                        get_fname = self.db_connection.get_fname({'session_id': session_id})
                        # e_list = self.db_connection.get_engineer_list()
                        # order = self.db_connection.get_order_list()
                        if user and len(user):
                            session_info = {
                                'user_id': user[0],
                                'fname':get_fname,
                                'is_valid': True,
                                'session_id': session_id,
                                'role':role[0]
                            }
                        # if e_list and len(e_list):
                        #     data_list = list()
                        #     for engineer_list in e_list:                                
                        #         engineer_list={
                        #             'engineer_id': engineer_list[0],
                        #             'email': engineer_list[2],
                        #             'mobile_no': engineer_list[6],
                        #             'specialist': engineer_list[7],
                        #             'experience': engineer_list[8],
                        #         }
                        #         data_list.append(engineer_list)
                        # if order and len(order):
                        #     final_order_list = list()
                        #     for order_list in order: 
                        #         order_list={
                        #             'engineer_id': order_list[0],
                        #             'email': order_list[1],
                        #             'specialist': order_list[2],
                        #             'mobile_no': order_list[3],
                        #             'experience': order_list[4],
                        #         }
                        #         final_order_list.append(order_list)
                html = html.replace('$session_info', json.dumps(session_info))
                # html = html.replace('$data_list', json.dumps(data_list))
                # html = html.replace('$final_order_list', json.dumps(final_order_list))
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html.encode())
        else:
            super(myHandler, self).do_GET()
           
def start_server():
   SimpleHTTPRequestHandler.extensions_map['.js'] = 'application/javascript'
   httpd = HTTPServer(('0.0.0.0', 3600), myHandler)
   httpd.serve_forever()

url = 'http://127.0.0.1:3600'

if __name__ == "__main__":
   print("----------------------")
   print("----------------------")
   print("Server running on: {}".format(url))
   threading.Thread(target=start_server, daemon=True).start()

   while True:
       try:
           time.sleep(1)
       except KeyboardInterrupt:
           httpd.server_close()
           quit(0)