from odoo import api,fields,models

class StudentDetails(models.Model):
    _name = 'student.details'
    _description = 'student information'

    student_name = fields.Char(string="Name",required=True)
    student_age = fields.Integer()
    student_percentage = fields.Float()
    student_birthdate = fields.Date()
    current_date = fields.Date()
    gender = fields.Char()
    branch = fields.Char()