from odoo import models, fields, api, _


class Doctor(models.Model):
	_name = "hospital_management.doctor"
	_description = 'hospital_management.doctor'
	_order = 'id desc'

	name = fields.Char(String = "Doctor Name")
	email = fields.Char(String = "Email")
	phone = fields.Char(String = "Phone",size=10)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
	date_of_birth = fields.Date(String = "Date Of Birth")
	name_of_clinic = fields.Char(String = "Name of Clinic")
	clinic_address = fields.Text(String = "Clinic Address")
	specilization = fields.Char(String = "Specilization")
	patient_id = fields.One2many('hospital_management.patient','doctor_id',String="Patient")


	@api.model
	def default_get(self, fields):
		res = super(Doctor, self).default_get(fields)
		res['name_of_clinic'] = "Xyz Hospital"
		return res

	@api.model
	def name_create(self,name):
		res = self.create({'name':name,'email':'dyu@Zsa.com'})
		return res.name_get()[0]

	# def write(self, vals):
	# 	vals['phone'] = '7894561236'
	# 	res = super(Doctor,self).write(vals)
	# 	print("\n write method..")
	# 	return res