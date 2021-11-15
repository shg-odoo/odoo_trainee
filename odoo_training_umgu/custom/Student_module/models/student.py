from odoo import models,fields

class Student(models.Model):
	_name="student.details"
	_description="Student details"

	name=fields.Char(string="Name")
	enrollment_no=fields.Integer(string="Enrollment No")
	contact_no=fields.Char(string="Contact No")
	email=fields.Char(string="Email id")
	branch=fields.Char(string="Branch")
	dob=fields.Date(string="DOB")
	gender=fields.Selection([('male','Male'),('female','Female')],'Gender',default='male')
	age=fields.Integer(String="Age",compute="calculate_age")
	age_group=fields.Selection([('minor','Minor'),('major','Major')],string="Age Group",compute="calculate_age_group")
	percentage=fields.Float(string="Percentage")
	image=fields.Binary(string="Photo")
	address=fields.Text(string="Address");
	brief_intro=fields.Html(string="Brief Introduction");



	@api.depends('dob')
	def calculate_age(self):
		for rec in self:
			if rec.dob:
				curr_date=date.today()
				curr_year=curr_date.year
				rec.age=curr_year-rec.dob.year


	@api.depends('age')
	def calculate_age_group(self):
		for rec in self:
			if rec.age:
				if rec.age>=18:
					rec.age_group='major'
				else:
					rec.age_group='minor'