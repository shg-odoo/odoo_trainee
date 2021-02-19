from odoo import models, fields, api,_
from datetime import datetime,date

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    
    name=fields.Char(string="Name" ,required=True)
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    age=fields.Integer(string="Age")
    branch=fields.Char(string="Branch")
    fees=fields.Integer(string="Fees")
    image=fields.Binary(string="Image")
    gender=fields.Selection([('male','Male'),('female','Female'),],string="Gender",default='male')
    date=fields.Date(string="date")
    bdate=fields.Date(string="BDate" ,default=datetime.today())

    