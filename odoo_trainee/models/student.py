from odoo import models, fields, api, exceptions
from datetime import timedelta

class student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name = fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    per = fields.Integer(string="Percentage")
    html = fields.Html()
    bdate = fields.Date(string='Date of birth')
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    image = fields.Binary(string='Image')
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
   


    

