from odoo import fields, models, api

class PatientWizard(models.TransientModel):
	_name = 'patient.wizard'


	doctor_id = fields.Many2one('hospital_management.doctor',String="Doctor")


	def add_doctor(self):

		ids = self._context.get('active_ids')
		vals = {
         'doctor_id' : self.doctor_id

		}
		self.env['hospital_management.patient'].browse(ids).write(vals)


  

# class Student(models.TransientModel):
#     _name = 'student.wizard'

#     college_id = fields.Many2one('student.college')

#     def add_college(self):
#         ids = self._context.get('active_ids')
#         self.env['student'].browse(ids).write({'college_id': self.college_id})


   


