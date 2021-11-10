from odoo import models,fields

class Student(models.Model):
	_name="student.details"
	_description="Student details"

	# first_name=fields.Char(string="First Name");
	# last_name=fields.Char(string="Last Name")

	name=fields.Char(string="Name")
	enrollment_no=fields.Integer(string="Enrollment No")
	contact_no=fields.Char(string="Contact No")
	email=fields.Char(string="Email id")
	branch=fields.Char(string="Branch")
	dob=fields.Date(string="DOB")
	gender=fields.Selection([('male','Male'),('female','Female')],'Gender',default='male')
	percentage=fields.Float(string="Percentage")

