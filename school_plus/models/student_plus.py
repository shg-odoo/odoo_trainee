from odoo import models, fields, api

class StudentPlus(models.Model):
    
    _name = "student.plus"
    _description = "Inherited student module and added extra features to module"
    _inherit = 'student'

    address = fields.Text('Address')