from odoo import models, fields, api

class student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name = fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
