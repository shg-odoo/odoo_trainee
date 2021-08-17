from odoo import fields,models,api

class  student(models.Model):
    _name = "student"
    _description = "student model"

    name = fields.Char(string="name")
    average = fields.Float(compute='_compute_average',string="average")
    country = fields.Char(string="country")
    image = fields.Binary(string="Image", attachment = True)
    gender = fields.Selection([('male','male'),
                               ('female','female')],string="gender")
    birth_date = fields.Date(string="birth_date")
    maths = fields.Integer(string="maths")
    science = fields.Integer(string="science")
    english = fields.Integer(string="english")
    start_date = fields.Date(string="start_date")
    end_date = fields.Date(string="end_date")
    hobbies = fields.Many2many('student.hobbies')
    college_id = fields.Many2one('student.college',string="college_id")
    total = fields.Float(string="total")

    
    @api.onchange('maths','science','english')
    def _total(self):
        for i in self:
            i.total = i.maths+i.science+i.english
            print(self.id)


    @api.depends('maths','science','english')
    def _compute_average(self):
        for i in self:
            i.average = (i.maths+i.science+i.english)/3


class hobbies(models.Model):
    _name = "student.hobbies"

    name = fields.Char(string="hobbies")


class college(models.Model):
    _name= "student.college"

    name = fields.Char(string="name")
    city = fields.Char(string="city")
    std_record = fields.One2many('student','college_id',string="student_data") 

class contact_detail(models.Model):
    _inherit = 'student'

    address = fields.Char(string="Address")
