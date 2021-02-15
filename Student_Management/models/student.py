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
    image = fields.Binary(string = "image")
    birthdate = fields.Date(string = "Date of Birth")
    date_from = fields.Datetime(string="From")
    date_to = fields.Datetime(string="To")
    