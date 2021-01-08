from odoo import models, fields, api

class Wizard(models.TransientModel):
	_name = "student.wiz"

	#name = fields.Char(string="Name", required=True)
	age = fields.Integer(string="Age")
	
	def updat_wiz(self):
		print("Successfull")
		self.env['school.student'].browse(self._context.get("active_ids")).update({'age':self.age})
		return True