from odoo import models,fields

class Student(models.Model):
    _name='school.student'
    _description='Student Details'
    
    name=fields.Char(string='Name')
    age=fields.Integer(string='Age')
    height=fields.Float(string='Height')
    birthDate=fields.Date(string='Birth Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ],string='Gender', default='male')
    image=fields.Binary(string="Image")
    html=fields.Html('Description')