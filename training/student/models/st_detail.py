from odoo import fields, models

class st_detail(models.Model):
	_name = 'student'
	_description="Store Student Details"

	name = fields.Char(string="Name")
	branch = fields.Char(string="Branch")