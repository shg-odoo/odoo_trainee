from odoo import fields,models

class collegeteacher(models.Model):
    _name="college.teacher"
    _description="teachers details"
    
    name=fields.Char(string="Name")
    t_id=fields.Many2one("college.student",string="techer id")
    age=fields.Integer(string="Age")

