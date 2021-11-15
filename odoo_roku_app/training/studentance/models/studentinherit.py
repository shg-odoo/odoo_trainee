from odoo import fields, models



class studentdata(models.Model):
	_name = 'student.inherit'
	_description = "Student inherit "
	_inherit = 'student'
	_rec_name = 'job'



	passout = fields.Char(string="Passout")

