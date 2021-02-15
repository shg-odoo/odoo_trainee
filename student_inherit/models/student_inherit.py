from odoo import fields,models,api

class student(models.Model):
    _name = 'student_inherit'
    _inherit = 'student'
    _description = "Student Inherit Details"


    update_new = fields.Char(string="Update New")
   