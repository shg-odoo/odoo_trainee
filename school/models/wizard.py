from odoo import models, fields, api

class Wizard(models.TransientModel):
	_name = 'school.wizard'
	_description = "Wizard"

	age = fields.Integer(string="Age")
	company_id = fields.Many2one('school.student', string="Company")