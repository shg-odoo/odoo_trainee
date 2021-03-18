from odoo import http
from odoo.http import request


class PatientController(http.Controller):

	@http.route('/hospital_management/patient', type='http',auth='public', website=True)
	def patient_details(self , **kwargs):

		patient_data = request.env['hospital_management.patient'].sudo().search([])

		return request.render('hospital_management.patient_page', {
			'patient': patient_data
		})
	
	@http.route('/hospital_management/patient_add', type='http',auth='public', website=True)
	def patient_add(self , **kwargs):
		
		return request.render('hospital_management.patient_add_page', {})



	@http.route('/hospital_management/patient_add/submit', type='http',auth='public', website=True)
	def patient_add_submit(self , **kwargs):
		# patient_val = request.env['hospital_management.patient'].create({
		# 	'name': kwargs.get('name'),
		# 	'email': kwargs.get('email'),
		# 	'phone': kwargs.get('phone')
		# })
		request.env['hospital_management.patient'].create(kwargs)

		return request.redirect('/hospital_management/patient')


	# @http.route('/hospital_management/patient_update/<model("hospital_management.patient"):std>', type='http',auth='public', website=True)
	# def patient_update(self , std,**kwargs):

	# 	std.unlink()

	# 	return request.redirect('/hospital_management/patient')	


	@http.route('/hospital_management/patient_delete/<model("hospital_management.patient"):std>', type='http',auth='public', website=True)
	def patient_delete(self , std,**kwargs):

		std.unlink()

		return request.redirect('/hospital_management/patient')













