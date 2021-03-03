from odoo import fields, models, api

class Employee(models.Model):
	_name='employee'
	_description="Employee Details"

	name=fields.Char('Employee Name', required=True)
	dept=fields.Char('Department')
	average=fields.Float()
	age=fields.Integer('Age')
	number=fields.Char('Phone Number')
	address=fields.Text('Address')
	branch=fields.Char('Branch')
	gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
	profile=fields.Binary('Image')
	date = fields.Date(default=lambda self: fields.Date.today())
	email=fields.Char('Email')
	techmarks=fields.Integer('Technical Marks')
	rating=fields.Float('Rating')
	phy=fields.Integer('Physics')
	chem=fields.Integer('Chem')
	math=fields.Integer('Maths')
	bday=fields.Date('Birthday Date')
	pr=fields.Float('Percentage')
	grade=fields.Char("Grade")