from odoo import fields,models,api

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    
    name = fields.Char(string="Name")
    roll_no = fields.Integer(string='Roll No')
    birthdate = fields.Date(string='birth date')
    image = fields.Binary()
    gender = fields.Selection([('male','Male') ,('female','Female')],string='Gender', default='male')
    age = fields.Char(string='age')
    physics = fields.Integer(string='physics')
    maths = fields.Integer(string='maths')
    chemistry = fields.Integer(string='chemistry')
    Average = fields.Float(string='Average')
    Address = fields.Char(string='Address')
    current_date = fields.Date('Current Date',default = lambda cdate:fields.Date.today())
    contect_no = fields.Char(string='Contect No')
    
    