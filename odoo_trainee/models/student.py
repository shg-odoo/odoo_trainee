from odoo import models, fields, api, exceptions
from datetime import timedelta, date
from odoo.exceptions import ValidationError

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
    percentage = fields.Integer(string="Percentage")
    maths = fields.Integer(string="Maths")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    fees = fields.Integer(string="Fees")
    age = fields.Integer(string="age")
    total = fields.Integer(string="total",compute="_get_total")
    college_name = fields.Many2one("student.college", string="College")

    @api.onchange('maths','physics','chemistry')
    def _get_percentage(self):
        for r in self:
            r.percentage = (r.maths + r.chemistry + r.physics)/3 

    @api.depends('maths','physics','chemistry')
    def _get_total(self):
        for i in self:
            i.total = i.maths + i.chemistry +i.physics


   
    @api.constrains('age','percentage','maths','physics','chemistry')
    def _check_age(self):
        for record in self:
            if record.age<18:
                raise ValidationError(f"your are not allowed: {record.age}")
            if record.percentage < 33:
                raise ValidationError(f"you are failed in exam {record.percentage} ")
            if((record.maths and record.physics and record.chemistry)>100 and (record.maths and record.physics and record.chemistry)< 0):
                raise ValidationError(f"you give wrong input marks should not greater than 100 and less than 0") 
            if record.chemistry <33:
                raise ValidationError(f"you are failed in chemistry {record.chemistry}") 
            if record.maths <33:
                raise ValidationError(f"you are failed in maths {record.maths}") 
            if record.physics <33:
                raise ValidationError(f"you are failed in physics {record.physics}") 



class college(models.Model):
    _name = "student.college"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")