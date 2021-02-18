from odoo import fields,models,api,_
from odoo.exceptions import ValidationError

from datetime import date,datetime
from dateutil.relativedelta import relativedelta

class student(models.Model):
    _name = 'student'
    _inherit = ['mail.thread',
               'mail.activity.mixin']
    _description = "Student Details"
    _order = "id desc"
    _rec_name = "student_name"

   # @api.depends('Hobbies')
    def _gethobby_count(self):
        count = self.env['student.hobby'].search_count([('hobby_id','in',self.hobby_id)])
        self.Hobbies_count = count
    
    def _default_branch(self):
        return 'computer'
    
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' %(rec.name_seq,rec.student_name)))
        return res

    def email_template1(self):
        print("send mail")
        mail_data = self.env.ref("student.email_template_studentdata").id
        temp = self.env['mail.template'].browse(mail_data).send_mail(self.id,force_send=True)
        return temp

    @api.depends('student_name')
    def _get_upper_name(self):
        for rec in self:
            rec.student_name_up = rec.student_name.upper() if rec.student_name else False

    def _get_lower_name(self):
        for rec in self:
            rec.student_name_up = rec.student_name.lower() if rec.student_name else False
    
    student_name = fields.Char(string="Name" ,required=True)
    student_name_up = fields.Char(sstring="Uname" ,compute="_get_upper_name" ,inverse="_get_lower_name")
    roll_no = fields.Integer(string='Roll No' ,required=True)
    birthdate = fields.Date(string='birth date' ,required=True)
    image = fields.Binary('Image')
    gender = fields.Selection([('male','Male') ,('female','Female')],string='Gender', default="male")
    age = fields.Integer(string='age',compute="_get_age",store=True)
    html = fields.Html()
    branch = fields.Char(string="Branch",default=_default_branch)
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
    hobby_id = fields.Many2one('student.hobby', string='Hobby')
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,  index=True, default=lambda self: _('New'))
    Hobbies = fields.Many2many('student.hobby',string='Hobbies')
    Hobbies_count = fields.Integer(compute='_gethobby_count' ,store=True)
    state = fields.Selection(
        [('Dontknow','Dontknow'),('Good','Good') ,('bad','Bad')]
        ,string='Status', readonly=True, default='Dontknow')

    active = fields.Boolean(string="Active",default=True)
    email_id = fields.Char(string="Email id")
  

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
         
  #  @api.depends('Hobbies')
    

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
    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('Student_Sequence') or _('New')
        result = super(student, self).create(vals)
        return result

    def open_college(self):
        self.ensure_one()
        vals = {
            'name' : 'College',
            'view_type' : 'form' ,
            'rec_model' : 'student.college',
            'view_id' : False,
            'domain' : [('college_id','=',self.id)],
            'view_mode' : 'tree,form',
            'type' : 'ir.actions.act_window',

        }
        return vals

    def Action_status_good(self):
        for rec in self:
            rec.state = 'Good'

    def Action_status_bad(self):
        for rec in self:
            rec.state = 'bad'

    def Action_status_dontknow(self):
        for rec in self:
            rec.state = 'Dontknow'
    
class Hobby(models.Model):

    _name = 'student.hobby'

    hobby_id =fields.Integer('Hobby Id')
    name = fields.Char('Hobby')
    
class Extradetails(models.Model):
    _inherit = 'student'

    review = fields.Char(string="Review")