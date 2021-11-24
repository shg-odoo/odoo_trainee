from odoo import fields,models,api
from datetime import date


class Teacher(models.Model):
	_name="teacher.details"
	_descriptions="Teacher details"
	_inherit="student.details"

	salary=fields.Float(string="Salary")

	def update_teacher_salary(self):
		return {'type': 'ir.actions.act_window',
				'res_model' : 'teacher.salary.update',
				'view_mode' : 'form',
				'target' : 'new'}

class TeacherCollege(models.Model):
	_inherit="student.college"

	principal=fields.Char(String="Principle")
