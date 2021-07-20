from odoo import  fields, models, api

class Student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name = fields.Char(string="name")
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    branch = fields.Char(string="branch")
    birthday = fields.Date(string="birthday")
    email = fields.Char(string="email")
    enrollment_no = fields.Integer('enrollment_no')
    contact_no = fields.Integer('contact_no')
    address = fields.Char(string="address")