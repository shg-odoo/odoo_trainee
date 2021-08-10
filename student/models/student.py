from odoo import fields,models

class  student(models.Model):
	_name = "student"
	_description = "student model"

	name = fields.Char(string="name")
	percentage = fields.Float(string="percentage")
	place = fields.Char(string="place")
	image = fields.Binary(string="Image", attachment = True)
	gender = fields.Selection([('male','male'),
							   ('female','female')],string="gender")
	birth_date = fields.Date(string="birth_date")
	maths = fields.Integer(string="maths")
	science = fields.Integer(string="science")
	english = fields.Integer(string="english")
	total = fields.Float(string="total")
	start_date = fields.Date(string="start_date")
	end_date = fields.Date(string="end_date")