from odoo import models, fields ,api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Employee(models.Model):
    _name = 'employee'
    _description = "Employee Full-Details"


    fname = fields.Char(string="FirstName")
    lname = fields.Char(string="Lastname")
    employmentNo = fields.Integer(string="Employment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    html = fields.Html()
    bdate = fields.Date(string='Date of birth')
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    image = fields.Binary(string='Image')
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    percentage = fields.Integer(string="Percentage",compute="_get_percentage", store=True)
    maths = fields.Integer(string="Maths")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    income = fields.Integer(string="Income")
    age = fields.Integer(string="age")
    total = fields.Integer(string="total",compute="_compute_total", store=True)
    working = fields.Boolean(string="Working",default=True)
    country_id = fields.Many2one('res.country', string='Country')
    company_id = fields.Many2one("employee.company", string="Company")
    hobbies_id = fields.Many2many("employee.hobbies", string="Hobbies")
    name_seq = fields.Char(string="Student Sequence", required=True, copy=False, readonly=True, index=True, default=lambda self:('New'))


@api.depends('maths','physics','chemistry')
def _compute_total(self):
    print("\n\n\n",self)
    for i in self:
        i.total = i.maths + i.physics + i.chemistry      
    # self.total = self.maths + self.physics + self.chemistry

@api.onchange('maths','physics','chemistry')
def _get_percentage(self):
    # print("\n\n\n",self)
    self.percentage = (self.maths + self.chemistry + self.physics)/3

@api.constrains('age')
def _constraints_age(self):
    for rec in self:
        if(rec.age < 18):
            raise ValidationError("age must above 18")


class Company(models.Model):
    _name = "employee.company"
    _rec_name = "company_name"

    company_name = fields.Char(string="Company Name")
    company_city = fields.Char(string="Company city")
    id1 = fields.One2many("employee", "company_id", string="Company Id")


class country(models.Model):
    _name = "employee.country"
    _rec_name = "country_name"

    country_name = fields.Char(string="Country Name")
    current_city = fields.Char(string="Current city")
    # current_state = fields.Char(string="Current State")
    id1 = fields.One2many("employee", "country_id", string="Country Id")

class Hobbies(models.Model):
    _name = "employee.hobbies"

    name = fields.Char(string="Hobbies Name")





