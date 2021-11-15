from odoo import fields, models


class Wizards(models.TransientModel):
	_name = "student.wizard"
	_description = "Register form of student.wizard"


	college_id = fields.Many2one('student.college', string="College")
	

	def add_college(self):
		var = self._context.get("active_ids")
		return self.env['student'].browse(var).write({'college_id':self.college_id})








