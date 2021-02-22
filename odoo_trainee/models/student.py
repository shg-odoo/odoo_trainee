from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError



class student(models.Model):
    _name = 'student'
    _description = "Student Details"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _order = "id desc"

    name = fields.Char(string="Name")
    enrollmentNo = fields.Integer(string="Enrollment No")
    contactNo = fields.Char(string="Contact No")
    email = fields.Char(string="Email Id")
    branch = fields.Char(string="Branch")
    html = fields.Html()
    bdate = fields.Date(string='Date of birth', track_visibility="always")
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),],'Gender', default='male')
    image = fields.Binary(string='Image')
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    percentage = fields.Integer(string="Percentage")
    maths = fields.Integer(string="Maths")
    physics = fields.Integer(string="Physics")
    chemistry = fields.Integer(string="Chemistry")
    fees = fields.Integer(string="Fees")
    age = fields.Integer(string="age",compute="_get_age",store=True, track_visibility="always")
    total = fields.Integer(string="total",compute="_get_total")
    college_id = fields.Many2one("student.college", string="College")
    hobbies_id = fields.Many2many("student.hobby", string="Person hobbies")
    name_seq = fields.Char(string="Student Sequence", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    state = fields.Selection([
            ('draft','Draft'),
            ('confirm','Confirm'),
            ('done','Done'),
            ('cancel','Cancelled'),
    ], string='Staus', readonly=True, default='draft')
    active = fields.Boolean('Active',default=True)



    @api.onchange('maths','physics','chemistry')
    def _get_percentage(self):
        for r in self:
            r.percentage = (r.maths + r.chemistry + r.physics)/3 
        print(self.id)

    @api.depends('maths','physics','chemistry')
    def _get_total(self):
        for i in self:
            i.total = i.maths + i.chemistry +i.physics

    
    @api.depends('bdate')
    def _get_age(self):
        for i in self:
            if i.bdate:
                i.age = relativedelta(date.today(),i.bdate).years


   
    @api.constrains('age')
    def _constraints_age(self):
       for rec in self:
           if(rec.age < 18):
               raise ValidationError("age must above 18")

    @api.constrains('maths','physics','chemistry')
    def _constraints_marks(self):
        for rec in self:
            if(rec.maths > 100 or rec.maths < 0):
                raise ValidationError("Maths marks should be in 0-100")
            if(rec.physics > 100 or rec.physics < 0):
                raise ValidationError("Physics marks should be in 0-100")
            if(rec.chemistry > 100 or rec.chemistry < 0):
                raise ValidationError("Chemistry marks should be in 0-100")

    @api.model
    def create(self,vals):
        if vals.get('name_seq',_('New')) == _('New'):
                vals['name_seq'] = self.env['ir.sequence'].next_by_code('student.sequence') or _('New')
        result = super(student, self).create(vals)
        return result

    
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Confirmed',
                    'type': 'rainbow_man',
                }
            }


    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def email_template1(self):
        print("send mail")
        mail_data = self.env.ref("odoo_trainee.email_template_studentdata").id
        temp = self.env['mail.template'].browse(mail_data).send_mail(self.id,force_send=True)
        return temp



class college(models.Model):
    _name = "student.college"
    _rec_name = "college_name"

    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="College city")
    id1 = fields.One2many("student", "college_id", string="College Id")



class hobby(models.Model):
    _name = "student.hobby"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "hobbies"

    hobbies = fields.Char(string="Hobbies")
   



class scholarship(models.Model):
    _inherit = "student"

    scholarship = fields.Integer(string="Scholarship")
   