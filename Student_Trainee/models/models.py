from odoo import models,fields,api
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name='school.student'
    _description='Student Details'
    
    image=fields.Binary(string="Image")
    student_id=fields.Integer(string="Student ID")
    name=fields.Char(string="Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ],string="Gender", default='male') 
    birthDate=fields.Date(string="Birth Date")
    age=fields.Integer(string="Age",compute="_get_age",store=True)
            
    mobile_number=fields.Char(string="Mobile Number",size=10)
    email=fields.Char(string="Email ID")
    address=fields.Text(string="Address")
    
    bloodGroup=fields.Selection([("o+","O+"),("o-","O-"),("b+","B+"),("b-","B-"),("a+","A+"),("a-","A-"),("ab+","AB+"),("ab-","AB-")],string="Blood Group")
    height=fields.Float(string="Height")
    weight=fields.Integer(string="Weight")
    disabled=fields.Boolean(string="Physically Disabled?",default=False)
    
    intro=fields.Html('Introduction')
    
    date_today=fields.Date(default=lambda today:fields.date.today())
    
    @api.depends("birthDate")
    def _get_age(self):
        for i in self:
            if i.birthDate:
                i.age = relativedelta(date.today(),i.birthDate).years