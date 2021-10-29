from odoo import models, fields



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


	
