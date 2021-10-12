from odoo import models,fields

class Employee(models.Model):
	_name = "employee"
	_description = "employee details"

	empcode =  fields.Integer("Employee Id",required = True)
	first_name = fields.Char("First Name",required = True)
	middle_name = fields.Char("Middle Name")
	last_name = fields.Char("Last Name",required = True)
	Gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')])
	dob = fields.Date('Date of Birth')
	Salary = fields.Float("Salary")
