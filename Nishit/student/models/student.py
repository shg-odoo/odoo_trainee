from odoo import models,fields,api
from odoo.exceptions import ValidationError

class inheritstudent(models.Model):
    _name="inherit.student"
    _inherit="college.student"
     
    
    mentor=fields.Char(string="Mentor name") 
    ages=fields.Integer(string="AGE") 
    
    