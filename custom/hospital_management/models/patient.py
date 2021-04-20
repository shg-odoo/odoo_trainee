from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import datetime,date
from odoo.exceptions import ValidationError

class Patient(models.Model):
	_name = "hospital_management.patient"
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'hospital_management.patient'

	name = fields.Char(String="Name",track_visibility="always")
	email = fields.Char(String="Email")
	phone = fields.Char(String="Phone",size=10)
	gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
	blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'),('o+', 'O+'), ('o-', 'O-'),('ab+', 'AB+'), ('ab-', 'AB-')],String="Blood Group")
	address = fields.Text(String="Address")
	date_of_birth = fields.Date(String="Date Of Birth")
	current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
	age = fields.Integer(String="Age",compute='_get_age_data',store=True)
	image = fields.Binary(String="Image", attachment=True)
	appointment_count = fields.Integer(String='Appointment', compute='get_appointment_count')
	doctor_id = fields.Many2one('hospital_management.doctor',String="Doctor")
	active = fields.Boolean('Active',default=True)
	

	@api.depends('date_of_birth')
	def _get_age_data(self):
		for rec in self:
			rec.age = relativedelta(date.today(),rec.date_of_birth).years


	def open_patient_appointments(self):
		return {
			'name': _('Appointment'),
			'domain': [('patient_id', '=', self.id)],
			'view_type': 'form',
			'res_model': 'hospital_management.appointment',
			'view_id': False,
			'view_mode': 'tree,form',
			'type': 'ir.actions.act_window',
		}


	def get_appointment_count(self):
		count = self.env['hospital_management.appointment'].search_count([('patient_id', '=', self.id)])
		self.appointment_count = count

	
	@api.constrains('name','email')
	def _check_name(self):
		for rec in self:
			if rec.name == rec.email:
				raise ValidationError("Name and Email can't be same...")


	def copy(self,default=None):
		default = {}
		copied_count = self.search_count([('name', '=like', u"Copy of {}%".format(self.name))])

		if not copied_count:
			new_name = u"Copy of {}".format(self.name)
		else:
			new_name = u"Copy of {} ({})".format(self.name, copied_count)	

		default['name'] = new_name
		res = super(Patient, self).copy(default)
		return res


	def name_get(self):
		res = []
		for rec in self:
			res.append((rec.id, '%s - %s' % (rec.id, rec.name)))
		return res


	@api.model
	def name_search(self,name='', args=None, operator='ilike', limit=100):
		if args is None:
			args = []
		domain = args + ['|', ('id', operator, name), ('name', operator, name)]
		return super(Patient, self).search(domain, limit=limit).name_get()
	


class PatientInherit(models.Model):
	_inherit = "hospital_management.patient"

	extra_details = fields.Html(String="Extra Details")
