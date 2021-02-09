from odoo import fields,models,api
from odoo.exceptions import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class student(models.Model):
    _name = 'student'
  #  _inherit = ['mail.thread',
   #             'mail.activity.mixin']
    _description = "Student Details"
    
    name = fields.Char(string="Name" )
    roll_no = fields.Integer(string='Roll No')
    birthdate = fields.Date(string='birth date')
    image = fields.Binary()
    gender = fields.Selection([('male','Male') ,('female','Female')],string='Gender', default="male")
    age = fields.Integer(string='age',compute="_get_age",store=True)
    html = fields.Html()
    branch = fields.Char(string="Branch")
    physics = fields.Integer(string='physics')
    maths = fields.Integer(string='maths')
    chemistry = fields.Integer(string='chemistry')
    Average = fields.Float(string='Average',store=True, compute='_get_total')
    Address = fields.Char(string='Address')
    current_date = fields.Date('Current Date',default = lambda cdate:fields.Date.today())
    contect_no = fields.Char(string='Contect No')
    total = fields.Integer(string='Total',store=True,compute='_get_total')
    total_compute = fields.Integer(compute='_get_total', string='Total Compute',store=True)
    college_id = fields.Many2one('student.college', string='College')

    @api.constrains('age')  
    def _constraints_age(self):
        for rec in self:
            if(rec.age < 18):
                raise ValidationError("Age must be 18 or above")

    @api.constrains('physics','maths','chemistry')
    def _constraints_marks(self):
        for rec in self:
            if(rec.maths > 100 or rec.maths < 0 ):
                raise ValidationError(" Maths marks should be in between 0 to 100 both included")
            if(rec.physics > 100 or rec.physics < 0 ):
                raise ValidationError(" Physics marks should be in between 0 to 100 both included")
            if(rec.chemistry > 100 or rec.chemistry < 0 ):
                raise ValidationError(" Chemistry marks should be in between 0 to 100 both included")

    @api.onchange('physics','maths','chemistry')
    def _onchange_Avg(self):
        for i in self:
            i.total = i.physics + i.chemistry + i.maths
            i.Average = (i.total)/3
         
    
    @api.depends('physics','maths','chemistry')
    def _get_total(self):
        for rec in self:
            rec.total = rec.maths+rec.physics+rec.chemistry
            rec.Average = rec.total/3
            rec.total_compute = rec.maths + rec.physics + rec.chemistry
    
    @api.depends("birthdate")
    def _get_age(self):
        for i in self:
            if i.birthdate:
                i.age = relativedelta(date.today(),i.birthdate).years
    


class college(models.Model):
    _name = 'student.college'

    college_name = fields.Char('College Name')
    college_city = fields.Char('College City')
    Student_record = fields.One2many('student','college_id',string="Student Record")
    