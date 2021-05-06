from odoo import api,fields,models

class StudentDetails(models.Model):
    _name = 'student.details'
    _description = 'student information'

    student_name = fields.Char(string="Name",required=True)
    student_age = fields.Integer()
    student_percentage = fields.Float()
    student_birthdate = fields.Date()
    current_date = fields.Date(default=fields.Date.today)
    branch = fields.Char()
    gender = fields.Selection([('male','Male'),('female','Female'),],string="Gender",default='male')
    image = fields.Binary(string="Profile",attachment=True)
    college_id = fields.Many2one('college.details',string="College")
    hobbies = fields.Many2many('student.hobbies')

class CollegeDetails(models.Model):
    _name = 'college.details'
    _description = 'College information is stored here'
    _rec_name = 'college_name'
    
    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="City")
    stud_record = fields.One2many('student.details','college_id',string="Student Records")

class StudentHobbies(models.Model):
    _name = 'student.hobbies'

    name = fields.Char(string="Hobbies")
