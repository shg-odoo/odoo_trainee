from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'
    _description = "Employee Full-Details"


    fname = fields.Char(string="FirstName")
    lname = fields.Char(string="Lastname")