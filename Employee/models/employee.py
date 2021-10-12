from odoo import models,fields

class Employee(models.Model):
	_name = "employee"
	_description = "employee details"

	first_name = fields.Char("FirstName",required = True)
	middle_name = fields.Char("MiddleName")
	last_name = fields.Char("LastName",required = True)
