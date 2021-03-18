from odoo import models, fields, api, _


class Doctor(models.Model):
	_name = "hospital_management.doctor"
	_description = 'hospital_management.doctor'

	name = fields.Char(String = "Doctor Name")
	email = fields.Char(String = "Email")
	phone = fields.Char(String = "Phone",size=10)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
	date_of_birth = fields.Date(String = "Date Of Birth")
	
	name_of_clinic = fields.Char(String = "Name of Clinic")
	clinic_address = fields.Text(String = "Clinic Address")
	specilization = fields.Char(String = "Specilization")
	patient_id = fields.One2many('hospital_management.patient','doctor_id',String="Patient")

# access_hospital_management_doctor,hospital_management.doctor,model_hospital_management_doctor,,1,1,1,1


	@api.model
	def default_get(self, fields):
		res = super(Doctor, self).default_get(fields)
		
		res['name_of_clinic'] = "Xyz Hospital"
		
		return res