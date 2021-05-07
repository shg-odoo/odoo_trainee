from odoo import api,fields,models

class StudentDetails(models.Model):
    _name = 'student.details'
    _description = 'student information'

    student_name = fields.Char(string="Name",required=True)
    student_age = fields.Integer()
    student_percentage = fields.Float(compute='_compute_pname',store=True)
    student_birthdate = fields.Date()
    current_date = fields.Date(default=fields.Date.today)
    branch = fields.Char()
    gender = fields.Selection([('male','Male'),('female','Female'),],string="Gender",default='male')
    image = fields.Binary(string="Profile",attachment=True)
    college_id = fields.Many2one('college.details',string="College")
    hobbies = fields.Many2many('student.hobbies')
    fy_marks = fields.Integer(string="First Year Marks")
    sy_marks = fields.Integer(string="Second Year Marks")
    ty_marks = fields.Integer(string="Third Year Marks")
    total_marks = fields.Integer(string="Total Marks")
    
    @api.onchange('fy_marks','sy_marks','ty_marks')
    def _onchange_total(self):
        self.total_marks = self.fy_marks + self.sy_marks + self.ty_marks
        print(self.total_marks)

    @api.depends('fy_marks','sy_marks','ty_marks')
    def _compute_pname(self):
        self.student_percentage = ((self.fy_marks + self.sy_marks + self.ty_marks)/300)*100


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
