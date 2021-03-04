from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Employee(models.Model):
    _name = 'employee'
    _description = "Employee Details"

    name = fields.Char('Employee Name', required=True)
    dept = fields.Char('Department')
    average = fields.Float(compute='_compute')
    age = fields.Integer('Age')
    number = fields.Char('Phone Number')
    address = fields.Text('Address')
    branch = fields.Char('Branch')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    profile = fields.Binary('Image')
    date = fields.Date(default=lambda self: fields.Date.today())
    email = fields.Char('Email')
    techmarks = fields.Integer('Technical Marks')
    rating = fields.Float(' Rating')
    phy = fields.Integer('Physics')
    chem = fields.Integer('Chem')
    math = fields.Integer('Maths')
    bday = fields.Date('Birthday Date')
    pr = fields.Float('Percentage')
    grade = fields.Char('Grade')
    total = fields.Integer('Total')    
    company = fields.Many2one('employee.company', string="Company")
    skills = fields.Many2many('employee.skills', string='Skills')


    @api.onchange('math', 'phy', 'chem')
    def _calculate_total(self):
        self.total = self.math + self.phy + self.chem
        self.average = self.total / 3

    @api.depends('math', 'phy', 'chem')
    def _compute(self):
        # self.total = self.math + self.phy + self.chem
        self.average = self.total / 3

    @api.constrains('age')
    def _age_constraint(self):
        if self.age < 18:
            raise ValidationError("Age should be more than 18")

    
class Company(models.Model):
    _name = 'employee.company'
    _rec_name = "company_name"

    company_name = fields.Char("Name")
    city = fields.Char("City")
    emp_record = fields.One2many('employee', 'company', string="Employee Records")


class Skills(models.Model):
    _name = 'employee.skills'
    _rec_name="skills"

    skills = fields.Char('Skills')