from odoo import fields, models, api

class PatientWizard(models.TransientModel):
	_name = 'patient.wizard'


	doctor_id = fields.Many2one('hospital_management.doctor',String="Doctor")

	def add_doctor(self):

		ids = self._context.get('active_ids')
		vals = {'doctor_id' : self.doctor_id }
		self.env['hospital_management.patient'].browse(ids).write(vals)


class CreateAppointment(models.TransientModel):
	_name = 'create_appointment.wizard'

	patient_id = fields.Many2one('hospital_management.patient',string='Patient')
	appointment_datetime = fields.Datetime(string ='Appointment Datetime')

	def create_appointment(self):
		
		vals = {
          'patient_id' : self.patient_id.id,
          'appointment_datetime' : self.appointment_datetime

		}

		new_appointment = self.env['hospital_management.appointment'].create(vals)





   


