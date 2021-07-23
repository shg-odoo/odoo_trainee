from typing import DefaultDict
from odoo import  fields, models, api , _
from datetime import date
from dateutil.relativedelta import relativedelta
class Student(models.Model):
    _name = 'student'
    _description = "Student Details"

    name            = fields.Char(string="Name")
    enrollmentNo    = fields.Integer(string="Enrollment No")
    contactNo       = fields.Char(string="Contact No")
    email           = fields.Char(string="Email Id")
    address         = fields.Char(string="address")
    branch          = fields.Char(string="Branch")
    birthday        = fields.Date(string="birthday")
    gender          = fields.Selection([('male','Male'),('female','Female'),],'Gender',default='male')
    image           = fields.Binary(string='Image')
    current_date    = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    age             = fields.Integer(string="age",compute="_calculate_age",store=True)
    maths           = fields.Integer(string="Maths")
    physics         = fields.Integer(string="Physics")
    chemistry       = fields.Integer(string="Chemistry")
    total           = fields.Integer(string="Total",compute="_cal_total")
    average         = fields.Integer(string="Average",compute="_cal_average")
    college_id      = fields.Many2one("student.college",string="College")
    hobbies      = fields.Many2many("student.hobby",string="Person hobbies")


    @api.onchange('maths','physics','chemistry')
    def _cal_average(self):
        for x in self :
            x.average = (x.maths + x.physics + x.chemistry)/3

    @api.depends('maths','physics','chemistry')
    def _cal_total(self):
        for j in self:
            j.total  = j.maths + j.chemistry + j.physics 

    @api.depends('birthday')
    def _calculate_age(self):
        for k in self :
            if k.birthday:
                k.age = relativedelta(date.today(),k.birthday).years


class College(models.Model):
    _name        = "student.college"
    _rec_name    = "college_id"

    college_id   = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    id1          = fields.One2many("student","college_id",string="College Id")

class Hobby(models.Model):
    _name     = "student.hobby"
    _rec_name = "hobbies"

    hobbies = fields.Char(string="Hobbies") 









