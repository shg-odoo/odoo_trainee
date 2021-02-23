from odoo import models, fields, api, exceptions
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", track_visibility='always')
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No", size=10, track_visibility='always') 
    age = fields.Integer(string="Age", compute='cal_age', store=True,)
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    image = fields.Binary(string = "image")
    birthdate = fields.Date(string = "Date of Birth")
    dateTo = fields.Date(string='Date', default=datetime.today())
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], string='Gender', default='male')
    city = fields.Char(string = "City")
    bloodGroup = fields.Selection([
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ], string='Blood Group', default='B+')

    address = fields.Text(string="Address")
    pincode = fields.Char(string="Pincode")
    country = fields.Char(string="Country")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height (cm)")
    disabled = fields.Boolean(string="Physically Disabled?", default=False)
    active = fields.Boolean('Active', default=True)


    college_ids = fields.Many2one('college', string='College')

    hobbies_ids = fields.Many2many('hobbies', string='Hobbies')
    
    maths = fields.Integer(string="Maths")
    chemistry = fields.Integer(string="Chemistry")
    physics = fields.Integer(string="Physics")
    total = fields.Integer(string="Total")
    average = fields.Integer(string="Average")

    sequenceName = fields.Char(
        string="Student Sequence",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default="New",
    )

    @api.model
    def create(self, vals):
        if vals.get("sequenceName", "New") == "New":
            vals["sequenceName"] = (
                self.env["ir.sequence"].next_by_code("student.sequence") or "New"
            )
        result = super(student, self).create(vals)
        return result


    @api.depends("birthdate")
    def cal_age(self):
        for i in self:
            if i.birthdate:
                i.age = relativedelta(date.today(), i.birthdate).years


    @api.onchange("maths", "chemistry", "physics")
    def _result(self):
        for i in self:
            i.total = i.maths + i.chemistry + i.physics
            i.average = (i.total)/3




class college(models.Model):
    _name = 'college'
    _description = "College Details"
    _rec_name = "collegeName"
    _inherit = "student"

    collegeName = fields.Char(string="College Name")
    collegeCity = fields.Char(string="College City")

    student_ids = fields.One2many('student','college_ids',string='Student')


class hobbies(models.Model):
    _name = 'hobbies'
    _description = "Student Hobbies"
    _rec_name = "hobbies"

    hobbies = fields.Char(string="Hobbies")


class admission(models.Model):
    _inherit = "student"

    eligible = fields.Boolean(
        string="Eligible For Admission", compute="_Eligible", store=True)

    @api.depends("age")
    def _Eligible(self):
        for i in self:
            if i.age >= 22:
                i.eligible = True
            else:
                i.eligible = False