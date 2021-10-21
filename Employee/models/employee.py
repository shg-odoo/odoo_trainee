from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from datetime import datetime,date
from odoo.exceptions import ValidationError

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
	age = fields.Integer("Age",compute="_get_age",store = True)	
	indian = fields.Boolean('Indian')
	contact = fields.Char("Contact Number")
	skills_id = fields.Many2many("employee.skills", string="Employee Skills",)
	hire_date = fields.Date("Date of Joining")
	department_id = fields.Many2one("employee.department", string="Department")
	Salary = fields.Float("Salary")
	experiance = fields.Float("Experiance(In Months)",readonly=True)

	@api.depends('dob')
	def _get_age(self):
		for i in self:
			if i.dob:
				i.age = relativedelta(date.today(),i.dob).years



	@api.onchange('hire_date','current_date')
	def _get_experiance(self):
		for i in self:
			i.experiance = relativedelta(i.current_date,i.hire_date).years

	@api.constrains('age')
	def _check_age(self):
	    for i in self:
	        if (i.age < 18):
	            raise ValidationError("Age should be greater than or equal to18 ")

class Department(models.Model):
	_name = "employee.department"
	_rec_name = "department_name" 

	department_name = fields.Char(string="Department Name")
	id1 = fields.One2many("employee", inverse_name="department_id")

class Skills(models.Model):

    _name = "employee.skills"
    _rec_name = "skills"

    skills = fields.Char(string="Skills")
    emp_id = fields.Many2many("employee", string="Employee" )

class ProvidentFund(models.Model):
	_inherit = "employee"

	UAN = fields.Integer("UAN Number")