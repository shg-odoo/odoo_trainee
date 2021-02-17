from odoo import models, fields, api
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "school.student"
    _description = "Student Details"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    nameseq = fields.Char(
        string="Student Sequence",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default="New",
    )

    image = fields.Binary(string="Image")
    student_id = fields.Integer(string="Student ID", required=True)
    name = fields.Char(string="Name", required=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        default="male",
    )
    birthDate = fields.Date(string="Birth Date", required=True)
    age = fields.Integer(string="Age", compute="_get_age", store=True)
    hobby_id = fields.Many2many("student.hobbies", string="Hobbies")

    mobile_number = fields.Char(string="Mobile Number", size=10, required=True)
    email = fields.Char(string="Email ID", required=True)
    address = fields.Text(string="Address", required=True)
    city = fields.Char(string="City", required=True)

    bloodGroup = fields.Selection(
        [
            ("o+", "O+"),
            ("o-", "O-"),
            ("b+", "B+"),
            ("b-", "B-"),
            ("a+", "A+"),
            ("a-", "A-"),
            ("ab+", "AB+"),
            ("ab-", "AB-"),
        ],
        string="Blood Group",
    )
    height = fields.Float(string="Height")
    weight = fields.Integer(string="Weight")
    disabled = fields.Boolean(string="Physically Disabled?", default=False)

    intro = fields.Html("Introduction")

    date_today = fields.Date(default=lambda today: fields.date.today())

    maths = fields.Integer(string="Maths", required=True)
    chemistry = fields.Integer(string="Chemistry", required=True)
    physics = fields.Integer(string="Physics", required=True)
    total = fields.Integer(string="Total", store=True)
    average = fields.Float(string="Average", store=True)

    school_id = fields.Many2one("student.school", string="School", required=True)

    @api.depends("birthDate")
    def _get_age(self):
        for i in self:
            if i.birthDate:
                i.age = relativedelta(date.today(), i.birthDate).years

    @api.constrains("age")
    def _ageValidator(self):
        if self.age < 18:
            raise ValidationError("Age Must Be 18 Or 18+")

    @api.onchange("maths", "chemistry", "physics")
    def _calculateResult(self):
        for i in self:
            i.total = i.maths + i.chemistry + i.physics
            i.average = (i.total) / 3

    @api.model
    def create(self, vals):
        if vals.get("nameseq", "New") == "New":
            vals["nameseq"] = (
                self.env["ir.sequence"].next_by_code("school.student.sequence") or "New"
            )
        result = super(Student, self).create(vals)
        return result


class School(models.Model):
    _name = "student.school"
    _description = "School Details"
    _rec_name = "school_name"

    school_name = fields.Char(string="School Name", required=True)
    school_city = fields.Char(string="City", required=True)
    student_record = fields.One2many(
        "school.student", "school_id", string="Student Record"
    )


class Hobbies(models.Model):
    _name = "student.hobbies"
    _description = "Student Hobbies"
    _rec_name = "student_hobby"

    student_hobby = fields.Char(string="Hobbies")


class Scholarship(models.Model):
    _inherit = "school.student"

    eligible = fields.Boolean(string="Eligible For Scholarship",compute="_Eligible",store=True)
    
    @api.depends("average")
    def _Eligible(self):
        for i in self:
            if i.average>90:
                i.eligible=True
            else:
                i.eligible=False
    


