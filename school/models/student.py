from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class Student(models.Model):

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
    avg = fields.Float(string="Avg", compute="_get_avg")

    @api.depends('maths', 'physics', 'chemistry', 'computer')
    def _get_avg(self):
        """
        self is a recordset, means containing all the records we have in our database with respect to
        model. So we can iterate over each record from recordset. `student(1, 2, 3)`
        """
        self.total_marks = self.maths + self.physics + self.chemistry + self.computer
        self.avg = self.total_marks / 4

    @api.onchange('dob')
    def _get_age(self):
        """
        Calculate age from birthdate
        """
        if self.dob:
                self.age = relativedelta(self.current_date, self.dob).years
                