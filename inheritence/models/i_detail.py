from odoo import fields, models,api
from odoo.exceptions import ValidationError

class i_detail(models.Model):
	_name = 'i_model'
	_inherit = "student"
	_description="i_Details"

	total_sub = fields.Integer(string="Total Subjects")