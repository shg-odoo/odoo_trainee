from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    
    name=fields.Char(string="Name" ,required=True)
    contactNo = fields.Char(string="Contact No")
    email=fields.Char(string="E-Mail")
    enrollmentNo = fields.Integer(string="Enrollment No")
    age=fields.Integer(string="Age")
    branch=fields.Char(string="Branch")
    fees=fields.Integer(string="Fees")
    image=fields.Binary(string="Image")
    gender=fields.Selection([('male','Male'),('female','Female'),],string="Gender",default='male')
    date=fields.Date(string="date")
    bdate=fields.Date(string="BDate" ,default=datetime.today())
    maths=fields.Integer(string="Maths")
    physics=fields.Integer(string="Physics")
    chemistry=fields.Integer(string="Chemistry")
    total=fields.Integer(string="Total" ,compute="_compute_total")
    percentage=fields.Integer(string="Percentage")
    college_id = fields.Many2one("student.college", string="College")
    clg_name=fields.Char(string="College name")
    clg_phno=fields.Char(string="college Ph.no ")
    clg_branch=fields.Char(string="Branch")
    clg_id=fields.Integer(string="College_id")
    hobbies_id = fields.Many2many("student.hobby", string="Person hobbies")

    @api.onchange('maths','chemistry','physics')
    def _compute_percentage(self):
       for r in self:
        r.percentage=(r.maths+r.physics+r.chemistry)/3 
       print(self.id) 
         
    @api.depends('maths','chemistry','physics')
    def _compute_total(self):
       for i in self:
        i.total=i.maths+i.physics+i.chemistry     

    @api.constrains('age')
    def _get_age(self):
       for j in self:
        if j.age <18:
            raise ValidationError("age must above 18")



class college(models.Model):
    _name = "student.college"
    _rec_name = "college_name"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    id1 = fields.One2many("student", "college_id", string="College Id")
 
class hobby(models.Model):
    _name="student.hobby"
    _rec_name="hobbies"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    hobbies=fields.Char(string="Hobbies")
    