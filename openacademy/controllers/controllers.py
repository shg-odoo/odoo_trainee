# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#from community.odoo.tests import Form


class Openacademy(http.Controller):
	@http.route('/openacademy/', auth='public', website=True)
	def index(self, **kw):
		session = request.env['openacademy.session'].sudo().search([])
		return request.render("openacademy.newhome", {
			'session': session
		})



	@http.route(['''/delete_rec/<model("openacademy.session"):id>''', ] , type='http', auth="public", website=True, sitemap=True)
	def delete_rec(self, **post):
		post.get("id").unlink()
		return request.redirect('/openacademy/')


	@http.route('''/update_rec/<model("openacademy.session"):id>''', type="http", auth="public", website=True)
	def edit_rec(self,**post):
		data = post.get('id')
		#print(data)
		up = request.env['openacademy.session'].search([('id', '=', data.id)])
		return request.render('openacademy.update_session',
			{"session_data":data})


	@http.route('/update/session' , auth="user", website=True)
	def update_rec(self,**post):
		print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Student Update Controller Called <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		id_n = post.pop('id')
		session = request.env['openacademy.session'].browse(id_n)
		session.write(post)

		return request.redirect('/openacademy/')
	



	@http.route('/add_session', type="http", auth="user", website=True)
	def create_form(self,**post):
		print(">>>>>>>>>>>>>>>ss add session")
		return request.render('openacademy.create_session',{})




	@http.route('/create/session' , auth="user", website=True)
	def create_save_rec(self,**post):
		print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Student Create Controller Called <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
		request.env['openacademy.session'].sudo().create(post)
		#print(">>>>>>>sss \n\n\n",mm)
		return request.redirect('/openacademy/')
		




		
