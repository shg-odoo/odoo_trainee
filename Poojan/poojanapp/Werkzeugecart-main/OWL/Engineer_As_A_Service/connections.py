#!/usr/bin/env python3
import psycopg2
import datetime
from psycopg2 import Error


class Connection():

    def __init__(self):
        print('>>> connection')
        self.create_connection('postgres')
        self.db_name = 'engineer_as_a_service'
        db_check = "SELECT 1 FROM pg_database WHERE datname='%s'" % self.db_name
        self.cr.execute(db_check)
        if not len(self.cr.fetchall()):
            self.cr.execute('CREATE DATABASE %s' % self.db_name)
            self.connection.close()
            self.create_connection(self.db_name)
            user = '''CREATE TABLE users(
                user_id SERIAL PRIMARY KEY,
                role varchar NOT NULL,
                email varchar  NOT NULL unique,
                fname varchar NOT NULL,
                password varchar NOT NULL,
                address varchar NOT NULL,
                session varchar,
                mobile_no varchar NOT NULL,
                specialist varchar,
                experience varchar
            );'''
            self.cr.execute(user);

            orders = '''CREATE TABLE orders(
               order_id SERIAL,
               user_id INT NOT NULL,
               engineer_name varchar NOT NULL,
               client_name varchar NOT NULL ,
               created_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
               PRIMARY KEY(order_id),
                  FOREIGN KEY(user_id) 
                  REFERENCES users(user_id)
            );'''
            self.cr.execute(orders);

        else:
            self.create_connection(self.db_name)

    def create_connection(self, db_name):
        self.connection = psycopg2.connect(user="postgres", password="postgres", host="127.0.0.1", port="5432", database=db_name)
        self.connection.autocommit = True
        self.cr = self.connection.cursor()
    
    def chk_eml(self, data):
        self.cr.execute("SELECT user_id FROM users WHERE email='%s'" % (data['email']))
        return self.cr.fetchone()

    def chk_pass(self, data):
        self.cr.execute("SELECT user_id FROM users WHERE password='%s'" % (data['password']))
        return self.cr.fetchone()
        
    def create_user(self, dictn):
        user = """INSERT INTO users (role, email, fname, password, address, mobile_no) VALUES ('client','%s', '%s', '%s', '%s', '%s')""" % (dictn['email'], dictn['fname'], dictn['password'], dictn['address'], dictn['mobno'])
        self.cr.execute(user)

    def create_user_engineer(self,data):
        engineer = """INSERT INTO users (role, email, fname, password, address, mobile_no, specialist, experience) VALUES ('engineer', '%s', '%s', '%s', '%s','%s', '%s', '%s')""" % (data['email'], data['fname'], data['password'], data['address'], data['mobno'], data['specialist'], data['experience'])
        self.cr.execute(engineer)

    def user_exists(self, data):
        self.cr.execute("SELECT user_id FROM users WHERE email='%s' and password='%s'" % (data['email'], data['password']))
        return self.cr.fetchone()

# ----------Client Side---------------------------------

    def get_user_role(self, data):
        self.cr.execute("SELECT role FROM users WHERE email='%s' and password='%s'" % (data['email'], data['password']))
        return self.cr.fetchone()

    def get_username(self, data):
        self.cr.execute("SELECT fname FROM users WHERE email='%s' and password='%s'" % (data['email'], data['password']))
        return self.cr.fetchone()
        

    def get_fname(self, data):
        self.cr.execute("SELECT fname FROM users WHERE session='%s'" % (data['session_id']))
        return self.cr.fetchone()

    def get_user_role_session_val(self, data):
        self.cr.execute("SELECT role FROM users WHERE session='%s'" % (data['session_id']))
        return self.cr.fetchone()

    def create_user_session(self, session_id, user_id):
        self.cr.execute("UPDATE users set session='%s' where user_id=%s" % (session_id, user_id))

    def session_validate(self, data):
        self.cr.execute("SELECT user_id FROM users WHERE session='%s'" % (data['session_id']))
        return self.cr.fetchall()

    def user_logout(self, data):    
        self.cr.execute("UPDATE users set session=null where session='%s'" % (data['session_id']))

    def fetch_engineer_data(self):
        self.cr.execute("SELECT * FROM users WHERE role='engineer'")
        return self.cr.fetchall()

   

    # def get_engineer_list(self):
    #     self.cr.execute("SELECT * FROM users WHERE role='engineer'")
    #     return self.cr.fetchall()

    def get_engineer_info(self,data):
        self.cr.execute("SELECT * FROM users WHERE user_id=%s" % (data['eng_id']))
        return self.cr.fetchone()    

    def book_engineer(self,fname,get_engineer_info):
        book_engineer = """INSERT INTO orders (user_id,engineer_name,client_name) VALUES (%s,'%s','%s')""" % (get_engineer_info[0],get_engineer_info[3],fname[0])
        self.cr.execute(book_engineer)

    def fetch_order_list(self,fname):
        self.cr.execute("SELECT orders.order_id, orders.engineer_name, orders.created_date, users.email FROM Orders INNER JOIN users ON orders.user_id=users.user_id WHERE orders.client_name='%s'" % (fname))
        return self.cr.fetchall()
        
    def fetch_view_engineer_orders_detail(self,data):
        self.cr.execute("SELECT orders.order_id,orders.engineer_name,orders.created_date,users.mobile_no,users.specialist,users.experience,users.email FROM orders INNER JOIN users ON orders.user_id=users.user_id WHERE order_id=%s" % (data['order_id']))
        return self.cr.fetchall()

    def fetch_client_profile(self,data):
        self.cr.execute("SELECT * from users WHERE user_id='%s'"%(data['user_id']))
        return self.cr.fetchall()

    def fetch_view_engineer_detail(self,data):
        self.cr.execute("SELECT * FROM users WHERE user_id=%s" % (data['id']))
        return self.cr.fetchall()

# ----------Engineer Side---------------------------------

# fetch_arrives_jobs_data
        
    def fetch_arrives_jobs_data(self,data):
        res = self.cr.execute("SELECT orders.order_id, users.fname, users.mobile_no, users.address, orders.created_date FROM Orders INNER JOIN users ON orders.client_name=users.fname WHERE orders.user_id=%s" % (data['user_id']))
        return self.cr.fetchall()

    def fetch_engineer_profile(self,data):
        self.cr.execute("SELECT * from users WHERE user_id='%s'"%(data['user_id']))
        return self.cr.fetchall()

    def fetch_view_client_job_detail(self,data):
        self.cr.execute("SELECT orders.order_id,orders.client_name,orders.created_date,users.mobile_no,users.address,users.email FROM orders INNER JOIN users ON orders.user_id=users.user_id WHERE Orders.order_id=%s" % (data['order_id']))
        return self.cr.fetchall()
