from odoo import models, fields, api, _


class Appointment(models.Model):
	_name = "hospital_management.appointment"
	_description = "hospital_management.appointment"
 
	name_seq = fields.Char(string="Appointment Sequence", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
	patient_id = fields.Many2one('hospital_management.patient',string='Patient', required=True)
	doctor_id = fields.Many2one('hospital_management.doctor',string='Doctor')
	doctor_specilization = fields.Char('Specilization',related='doctor_id.specilization', store=True)
	patient_age = fields.Integer('Age',related ='patient_id.age', store=True)
	patient_phone = fields.Char('Phone',related ='patient_id.phone', store=True)
	patient_email = fields.Char('Email',related ='patient_id.email', store=True)
	appointment_reason = fields.Text(string="Appointment Reason")
	appointment_datetime = fields.Datetime(string ='Appointment Datetime')
	patient_count = fields.Integer('Patient Count',compute='_get_patient_count',store=True)
	state = fields.Selection([
			('draft', 'Draft'),
			('confirm', 'Confirm'),
			('done', 'Done'),
			('cancel', 'Cancelled'),
		], string='Status', readonly=True, default='draft')
	
	def action_confirm(self):
		for rec in self:
			rec.state = 'confirm'


	def action_done(self):
		for rec in self:
			rec.state = 'done'


	@api.depends('doctor_id')
	def _get_patient_count(self):
		for rec in self:
			print("\n len(rec.doctor_id)",len(rec.doctor_id))
			rec.patient_count = len(rec.doctor_id)


	@api.model
	def create(self,values):
		if values.get('name_seq',_('New')) == _('New'):
			values['name_seq'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or _('New')
		res = super(Appointment,self).create(values)
		return res
	

	def test_recordset(self):
		for rec in self:
			pd = rec.env['hospital_management.patient'].search([])
			print("\n Names mapped::::",pd.mapped('name'))
			print("\n Sorted method::::",pd.sorted(key=lambda r: r.create_date,reverse=True))
			print("\n Filterd method::;;:",pd.filtered(lambda r: r.blood_group == 'o+'))