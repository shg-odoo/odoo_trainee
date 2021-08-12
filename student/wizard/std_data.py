from odoo import fields,models,api


class  student_wizard(models.TransientModel):
	_name = "student.wizard"

	college_id = fields.Many2one('student.college')

	def add_college(self):
		ids = self._context.get('active_ids')
		self.env['student'].browse(ids).write({'college_id':self.college_id})
		
