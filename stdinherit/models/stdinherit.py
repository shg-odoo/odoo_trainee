from odoo import models,fields,api

class stdinherit(models.Model):
    _name = 'student.inherit'
    _description = "Student Inherited Data"
    _inherit = 'student'

    review = fields.Char(string="review")
