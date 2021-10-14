from odoo import models,fields
from datetime import datetime,date
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
	current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
	indian = fields.Boolean('Indian', readonly=True)
	contact = fields.Char("Contact Number")
	Salary = fields.Float("Salary")
	experiance = fields.Float("Experiance")
