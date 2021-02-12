from odoo import fields,models,api,_
class college(models.Model):
    _name = 'student.college'
    _rec_name = "college_name"

    college_name = fields.Char('College Name')
    college_city = fields.Char('College City')
    Student_record = fields.One2many('student','college_id',string="Student Record")