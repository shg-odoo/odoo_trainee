from odoo import models, fields, api, exceptions
from datetime import timedelta, datetime, date

class student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name = fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No", size=10) 
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    image = fields.Binary(string = "image")
    birthdate = fields.Date(string = "Date of Birth")
    dateTo = fields.Date(string='Date', default=datetime.today())
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], string='Gender', default='male')
    city = fields.Char(string = "City")
    bloodGroup = fields.Selection([
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ], string='Blood Group', default='B+')

    qualification = fields.Selection([
            ('10th', '10th'),
            ('12th', '12th'),
            ('graduate', 'Graduate'),
            ('post-graduate', 'Post-Graduate'),
            ('phd', 'Phd'),
        ], string='Qualification', default='10th')

    address = fields.Text(string="Address")
    pincode = fields.Char(string="Pincode")
    country = fields.Char(string="Country")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    disabled = fields.Boolean(string="Disabled", default=False)
    