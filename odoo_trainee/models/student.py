from odoo import models, fields, api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
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
    age = fields.Integer(string="age",compute="_get_age",store=True)
    total = fields.Integer(string="total",compute="_get_total")
    college_id = fields.Many2one("student.college", string="College")

    @api.onchange('maths','physics','chemistry')
    def _get_percentage(self):
        for r in self:
            r.percentage = (r.maths + r.chemistry + r.physics)/3 

    @api.depends('maths','physics','chemistry')
    def _get_total(self):
        for i in self:
            i.total = i.maths + i.chemistry +i.physics

    
    @api.depends('bdate')
    def _get_age(self):
        for i in self:
            if i.bdate:
                i.age = relativedelta(date.today(),i.bdate).years


   
    @api.constrains('age')
    def _constraints_age(self):
       for rec in self:
           if(rec.age < 18):
               raise ValidationError("age must above 18")

    @api.constrains('maths','physics','chemistry')
    def _constraints_marks(self):
        for rec in self:
            if(rec.maths > 100 or rec.maths < 0):
                raise ValidationError("Maths marks should be in 0-100")
            if(rec.physics > 100 or rec.physics < 0):
                raise ValidationError("Physics marks should be in 0-100")
            if(rec.chemistry > 100 or rec.chemistry < 0):
                raise ValidationError("Chemistry marks should be in 0-100")


class college(models.Model):
    _name = "student.college"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    id1 = fields.One2many("student", "college_id", string="College Id")