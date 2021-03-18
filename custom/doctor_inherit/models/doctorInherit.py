from odoo import models, fields, api


class DoctorInherit(models.Model):
	_name = "doctor.inherit"

	_inherit = "hospital_management.doctor"


	patient_id = fields.Many2one("hospital_management.patient",String="Patient")