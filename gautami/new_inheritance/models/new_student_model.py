from odoo import fields,models

class NewStudent(models.Model):
    _name = 'new.student'
    _description = 'student information'
    _inherit = 'student.details'

    city = fields.Char(string="City")
