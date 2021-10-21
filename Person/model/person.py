from odoo import models,fields,api

class Person(models.Model):
	_name = 'person'
	_inherit = 'employee'

	empcode =  fields.Integer("Person Id",required = True)
	address = fields.Char("Adress")