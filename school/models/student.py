from odoo import models, fields
from datetime import date


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
    contact = fields.Char('Contact No')
    email = fields.Char('Email id')
    image = fields.Binary('Image')
    fees = fields.Float('Yearly Fees')
    ab_me = fields.Html('About Me')