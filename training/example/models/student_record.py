from odoo import fields,models,api

class Student(models.Model):
	_name = 'student'
	_description = "record for student details"


	name = fields.Char(string="Name")
	email = fields.Char(string="Email Id")
	address = fields.Char(string="address")
	age = fields.Integer(string='Age')
	enrollment_no = fields.Integer(string = 'Enrollment Number') 
	gender = fields.Selection([
			('male','Male'),
			('female','Female'),
			('other','Other'),
		],default="female")
	note = fields.Text(string='Description')
	
