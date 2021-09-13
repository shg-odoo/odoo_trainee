from odoo import fields, models,api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class st_detail(models.Model):
	_name = 'student'
	_description="Store Student Details"

	enrollmentNo = fields.Integer(string="Enrollment No")
	name = fields.Char(string="Name")
	current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
	branch = fields.Char(string="Branch")
	contactNo = fields.Char(string="Contact No")
	email = fields.Char(string="Email Id")
	html = fields.Html()
	image = fields.Binary(string='Image')
	bdate = fields.Date(string='Date of birth')
	gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='female')
	percentage = fields.Integer(string="Percentage")
	maths = fields.Integer(string="Maths")
	physics = fields.Integer(string="Physics")
	chemistry = fields.Integer(string="Chemistry")
	fees = fields.Integer(string="Fees")
	age = fields.Integer(string="age",compute="_get_age",store=True)
	total = fields.Integer(string="total",compute="_get_total")
	college_id = fields.Many2one("student.college", string="College_id")
	hobbies = fields.Many2many("student.hobby", string="Hobbies")
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
class college(models.Model):
    _name = "student.college"
    _rec_name = "college_name"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    nested = fields.One2many("student", "college_id", string="College Id")





class hobby(models.Model):
    _name = "student.hobby"
    
    _rec_name = "hobbies"

    hobbies = fields.Char(string="Hobbies")
    id1 = fields.Many2many("student", string="Hobbies")