from typing import DefaultDict
from odoo import  fields, models, api

class Student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name                    = fields.Char(string="Name")
    dob                     = fields.Date(string="DOB")
    governmentID            = fields.Integer(string="Government ID")
    contactNo               = fields.Char(string="Contact No")
    email                   = fields.Char(string= "Email Id")
    occupation              = fields.Char(string="Occupation")
    gender                  = fields.Selection([('male','Male'),('female','Female'),],'Gender',default='male')
    image                   = fields.Binary(string="Image")
    address                 = fields.Char(string="Address")

