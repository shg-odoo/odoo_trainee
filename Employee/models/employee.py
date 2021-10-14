from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
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
	age = fields.Integer("Age",compute="_get_age",store=True)	
	indian = fields.Boolean('Indian')
	contact = fields.Char("Contact Number")
	hire_date = fields.Date("Date of Joining")
	branch = fields.Char("Department")
	Salary = fields.Float("Salary")
	experiance = fields.Float("Experiance")
	
	@api.depends('dob')
	def _get_age(self):
		for i in self:
			if i.dob:
				i.age = relativedelta(date.today(),i.dob).years



	@api.onchange('hire_date','current_date')
	def _get_experiance(self):
		for i in self:
			i.experiance = relativedelta(i.current_date,i.hire_date).years
