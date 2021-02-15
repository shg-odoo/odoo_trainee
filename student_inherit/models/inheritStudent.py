from odoo import models, fields, api

class inherit_student(models.Model):
    _name = 'student.inherit'
    _inherit = 'student'

    review = fields.Char("Review")