from odoo import models, fields, api, exceptions
from datetime import timedelta

class student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name = fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    html = fields.Html()
    bdate = fields.Date(string='Date of birth')
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    image = fields.Binary(string='Image')
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    percentage = fields.Float(string="Percentage", compute="_get_percentage")
    maths = fields.Integer(string="Maths")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    fees = fields.Integer(string="Fees")

    @api.depends('maths','physics','chemistry')
    def _get_percentage(self):
        for r in self:
            r.percentage = (r.maths + r.chemistry + r.physics)/3    