from odoo import fields,models,api

class TeacherSalaryUpdate(models.TransientModel):
	_name="teacher.salary.update"

	updated_salary=fields.Float(String="Enter salary :")


	def update_teacher_salary(self):
		print("Successfully updated")
		self.env["teacher.details"].browse(self._context.get("active_ids")).update({"salary" : self.updated_salary})
		return True;
