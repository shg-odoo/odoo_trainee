from odoo import http
from odoo.http import request

class Student(http.Controller):

	@http.route('/school/student/', website=True, auth='user')
	def school_student(self,**kw):
		#return "Hello World"
		students = request.env['school.student'].sudo().search([])
		return request.render("school.students_id", {
				'students': students
			})