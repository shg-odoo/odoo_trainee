from odoo import api,models, fields, _
from odoo.exceptions import ValidationError
from datetime import datetime


class Session(models.Model):
	_name = 'openacademy.session'
	_description = "OpenAcademy Sessions"

	name = fields.Char(required=True)
	instructor_name = fields.Many2many('openacademy.instrustor', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")
	basic_knowledge = fields.Char()
	category = fields.Selection([('programming_lang','Programming Language'), ('designing','Designing')])
	start_date = fields.Date(required = True)
	end_date = fields.Date(constrains="Check_Date_Diff")

	@api.constrains('end_date','start_date')
	def Check_Date_Diff(self):
		if self.end_date <= self.start_date:
			raise ValidationError(_('The planned end date of the course cannot be prior to the planned start date.'))


	duration = fields.Float(digits=(6, 2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")

	
	   

	def name_get(self):
		result = []
		for record in self:
			name = record.name + ' ' + str(id)
			result.append((record.id, name))
		return result


	# def name_get(self):
	#     result = []
	#     for record in self:
	#         name = record.name
	#         result.append(name)
	#     return result


class Instructor(models.Model):
	_name = 'openacademy.instructor'
	_description = "OpenAcademy Instructor"

	instructor_name = fields.Char()
	# instructor_id = fields.Integer(required=True)
	instructor_field = fields.Char()
	instructor_course = fields.Many2many('openacademy.session', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")


	def name_get(self):
		result = []
		for record in self:
			name = record.instructor_name + ' ' + str(id)
			result.append((record.instructor_id, name))
		return result

	# def name_get(self):
	#     result = []
	#     for record in self:
	#         name = record.instructor_name + ' ' + str(record.instructor_id)
	#         result.append((record.id, name))
	#     return result

class Students(models.Model):
	_name = 'openacademy.student'
	_description = "OpenAcademy Students"
	

	student_name = fields.Char(required=True)
	student_email = fields.Char()
	student_course = fields.Many2many('openacademy.session', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")
	student_instructor = fields.Many2many('openacademy.instructor', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")

	student_attandance = fields.Integer()