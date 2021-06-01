from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class Student(models.Model):

    _inherit = "mail.activity.mixin"
    _name = 'student'
    _description = 'Student Profile'

    name = fields.Char('Name', required=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')])
    enroll_num = fields.Char('Enrollment No')
    std = fields.Selection([(str(i), str(i))for i in range(1, 13)], 'Standard')
    dob = fields.Date('Date of Birth')
    current_date = fields.Date('Current Date', default=date.today())
    age = fields.Integer('Age', compute="_get_age")
    contact = fields.Char('Contact No')
    email = fields.Char('Email id')
    image = fields.Binary('Image')
    fees = fields.Float('Yearly Fees')
    ab_me = fields.Html('About Me')
    parent_name = fields.Char('Parents Name')

    # subject marks
    maths = fields.Integer('Maths')
    physics = fields.Integer('Physics')
    chemistry = fields.Integer('Chemistry')
    computer = fields.Integer('Computer')
    # total marks
    total_marks = fields.Float(string='Total')
    avg = fields.Float(string="Avg", compute="_get_avg", store=True)

    @api.depends('maths', 'physics', 'chemistry', 'computer')
    def _get_avg(self):
        """
        self is a recordset, means containing all the records we have in our database with respect to
        model. So we can iterate over each record from recordset. `student(1, 2, 3)`
        """
        for mark in self:
            mark.total_marks = mark.maths + mark.physics + mark.chemistry + mark.computer
            mark.avg = mark.total_marks / 4

    @api.onchange('dob')
    def _get_age(self):
        """
        Calculate age from birthdate
        """
        if self.dob:
            self.age = relativedelta(self.current_date, self.dob).years

    # Relational field
    school_id = fields.Many2one('student.school', string="School Name")
    skill_ids = fields.Many2many('student.skill', string="Student Skills")


class School(models.Model):

    _name = "student.school"
    _description = "School name of student's"

    name = fields.Char('School')
    city = fields.Selection([('ahmedabad', 'Ahmedabad'),
                             ('anand', 'Anand'),
                             ('surat', 'Surat'),
                             ('baroda', 'Baroda')], 'City')
    # relational field
    student_ids = fields.One2many('student', 'school_id', string="All Students")


class Skill(models.Model):

    _name = "student.skill"
    _rec_name = 'skill'  # recognize name

    skill = fields.Char('Skill')


# model inheritance
class StudentInherit(models.Model):

    _inherit = 'student'
    
    blood_grp = fields.Selection([('a+', 'A+'), ('a-', 'A-'),
                                  ('b+', 'B+'), ('b-', 'B-'),
                                  ('o+', 'O+'), ('o-', 'O-'),
                                  ('ab+', 'AB+'), ('ab-', 'AB-')], 'Blood Group')
