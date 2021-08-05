from odoo import fields,models

class  student(models.Model):
	_name = "student.model"
    _description = "First Model"


    Name = fields.Char(string="Name")
    Id = fields.Integer(string="id")
    percentage = fields.float(string="percentage")
