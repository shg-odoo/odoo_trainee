from odoo import models,fields

class Student(models.Model):
    _name='student'
    _description='Student Details'
    
    name=fields.Char(string='Name')
    age=fields.Integer(string='Age')
    height=fields.Float(string='Height')
    birthDate=fields.Date(string='Birth Date')
    