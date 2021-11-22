from odoo import fields, models,api

class student(models.Model):
	_name = 'student' 
	_description = "Student Details"
	name = fields.Char(string="Name")
	city = fields.Char(string="City") 
	education = fields.Char(string="Education")  #string= "is table column name  display on screen" 
	age = fields.Integer(string="Age")
	salary = fields.Float(string="Salary")
	job = fields.Char(string="Job")
	sdate = fields.Date(string="Date Of Birth")
	gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
	current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
	image = fields.Binary(string='Image')
	college_id = fields.Many2one("student.college", string="College")
	hobbies_id = fields.Many2many("student.hobbies", string="Hobbies")
	math = fields.Integer(string="Math")
	chemistry = fields.Integer(string="Chemistry")
	physic = fields.Integer(string="Physic")
	total = fields.Integer(string="Total",compute="_get_total", store= True)
	avg = fields.Integer(string="AVG", compute="_s_avrage")
	add = fields.Integer(string="ADD", store=True)
	@api.depends('math','physic','chemistry')
	def _get_total(self):
	    for i in self:
	        i.total = i.math + i.chemistry +i.physic
	@api.onchange('math','physic','chemistry')
	def _s_avrage(self):
		for i in self:
			i.avg = (i.math + i.chemistry +i.physic)/3
	@api.onchange('math','physic','chemistry')
	def _a_add(self):
		for i in self:
			i.add = i.math+i.chemistry+i.physic
			print(i.add)
class college(models.Model):
	_name = 'student.college'
	_description = "College Details"
	name = fields.Char(string="College_Name")
	city = fields.Char(string="City")
	c_id = fields.One2many("student", "college_id", string="College Id")
class hobbies(models.Model):
	_name = 'student.hobbies'
	h_reading = fields.Char(string="Hobbies_Reading")
class demo(models.Model):
	_inherit = 'student'
	review = fields.Char(string="Review")








	

	
