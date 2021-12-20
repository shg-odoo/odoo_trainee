from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError

class Student(models.Model):
	_name = "student.details"
	_description = "Student details"
	# _rec_name="{we choose field as a rec name}"

	name = fields.Char(string="Student Name")
	college = fields.Many2one("student.college", string="College")
	enrollment_no=fields.Integer(string="Enrollment No")
	contact_no=fields.Char(string="Contact No")
	email=fields.Char(string="Email id")
	branch=fields.Char(string="Branch")
	subject=fields.Many2many("student.subject", string="Subject")
	dob=fields.Date(string="DOB")
	age=fields.Integer(String="Age", compute="compute_age", inverse="inverse_age")	
	gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',default='male')
	percentage=fields.Float(string="Percentage",required=True)
	image=fields.Image(string="Photo")
	address=fields.Text(string="Address");
	brief_intro=fields.Html(string="Brief Introduction");


	@api.onchange('dob')
	def onchange_dob(self):
		if self.dob:
			self.compute_age()
		else :
			self.age=False

	@api.depends('dob')
	def compute_age(self):
		for rec in self:
			if rec.dob:
				curr_date=date.today()
				curr_year=curr_date.year
				rec.age=curr_year-rec.dob.year

	def inverse_age(self):
		for rec in self:
			if rec.age:
				curr_year=date.today().year
				rec.dob=date(curr_year-rec.age,rec.dob.month,rec.dob.day)

	@api.constrains("percentage")
	def check_percentage(self):
		for rec in self:
			if rec.percentage<40:
				raise ValidationError("Percentage must be greater than or equal to 40")



class College(models.Model):
	_name="student.college"
	_description="college details"
	_rec_name="college_name"
   
	college_name=fields.Char(string="College Name")
	students=fields.One2many("student.details","college",string="Students")
	city=fields.Char(string="City")


class Subject(models.Model):
	_name="student.subject"
	_description="Subject Details"
	_rec_name="subject_name"

	subject_name=fields.Char(string="Subject Name")
	level=fields.Selection([('easy','Easy'),('medium','Meduim'),('hard','Hard')],string="Level",default="medium")


class CollegeReview(models.Model):
	_inherit="student.details"

	review=fields.Char(string="College Review",default="No Review")


class Other(models.Model):
	_name="other.task"
	_description="For administration"

	user_id=fields.Many2one("res.users", string="User")
	task=fields.Char(String="Task")
