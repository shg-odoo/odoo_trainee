from odoo import fields, models,api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class st_detail(models.Model):
	_name = 'student'
	_description="Store Student Details"

	name = fields.Char(string="Name")
	branch = fields.Char(string="Branch")
	enrollmentNo = fields.Integer(string="Enrollment No")
	contactNo = fields.Char(string="Contact No")
	email = fields.Char(string="Email Id")
	html = fields.Html()
	image = fields.Binary(string='Image')
	bdate = fields.Date(string='Date of birth')
	gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
	percentage = fields.Integer(string="Percentage")
	maths = fields.Integer(string="Maths")
	physics = fields.Integer(string="Physics")
	chemistry = fields.Integer(string="Chemistry")
	fees = fields.Integer(string="Fees")
	age = fields.Integer(string="age",compute="",store=True)
	total = fields.Integer(string="total",compute="_get_total")
	state = fields.Selection([
		('draft','Draft'),
		('confirm','Confirm'),
		('done','Done'),
		('cancel','Cancelled'),
		], string='Staus', readonly=True, default='draft')

	@api.onchange('maths','physics','chemistry')
	def _get_percentage(self):
		for r in self:
			r.percentage = (r.maths + r.chemistry + r.physics)/3 
			print(self.id)

	@api.depends('maths','physics','chemistry')
	def _get_total(self):
		for i in self:
			i.total = i.maths + i.chemistry +i.physics

	@api.depends('bdate')
	def _get_age(self):
		for i in self:
			if i.bdate:
				i.age = relativedelta(date.today(),i.bdate).years

	@api.constrains('age')
	def _constraints_age(self):
		for rec in self:
			if(rec.age < 18):
				raise ValidationError("age must above 18")

	@api.constrains('maths','physics','chemistry')
	def _constraints_marks(self):
		for rec in self:
			if(rec.maths > 100 or rec.maths < 0):
				raise ValidationError("Maths marks should be in 0-100")
			if(rec.physics > 100 or rec.physics < 0):
				raise ValidationError("Physics marks should be in 0-100")
			if(rec.chemistry > 100 or rec.chemistry < 0):
				raise ValidationError("Chemistry marks should be in 0-100")

	def action_confirm(self):
		for rec in self:
			rec.state = 'confirm'

	def action_done(self):
		for rec in self:
			rec.state = 'done'