from odoo import models, fields, api,_
from datetime import datetime,date

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    
    name=fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    age=fields.Integer(string="Age")
    branch=fields.Char(string="Branch")

    