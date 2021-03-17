from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Employee Details"
    _order = 'name'

    emp_seq = fields.Char(string='Employee Reference', required=True, copy=False, readonly=True, index=True, default="New")
    name = fields.Char('Employee Name', required=True)
    dept = fields.Char('Department')
    average = fields.Float(compute='_compute_average')
    age = fields.Integer('Age')
    number = fields.Char('Phone Number')
    address = fields.Text('Address')
    branch = fields.Char('Branch')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default="male")
    profile = fields.Binary('Image')
    date = fields.Date(default=lambda self: fields.Date.today())
    email = fields.Char('Email')
    techmarks = fields.Integer('Technical Marks')
    phy = fields.Integer('Physics')
    chem = fields.Integer('Chem')
    math = fields.Integer('Maths')
    bday = fields.Date('Birthday Date')
    # pr = fields.Float('Percentage')
    grade = fields.Char('Grade')
    total = fields.Integer('Total')
    company_id = fields.Many2one('employee.company', string="Company", track_visibility="always")
    skills = fields.Many2many('employee.skills', string='Skills')
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('pending', 'Pending'),
        ('cancel', 'Cancelled')
        ], string="Status", index=True, readonly=True, default='draft')

    def test_record(self):
        # print(self.id)
        # print(self.name)
        for rec in self:
            search = self.env['employee'].search([])
            print(search.mapped('name'))
            print(search.sorted(lambda a: a.write_date, reverse=True))
            # print(search.mapped('gender'))
            # search_a = self.env['employee'].search([self.id])
            print(search.filtered(lambda o: o.gender == 'male'))
            print(search.filtered(lambda z: z.gender == 'female'))
            # record_to_copy = self.env['employee'].browse(self._context.get('self.id'))
            # print(search_a)

    # def name_get(self):
    #     ref = []
    #     for a in self:
    #         ref.append((a.id, '%s - %s' % (a.name, a.company_id)))
    #     return ref

    # @api.multi
    def company_details(self):
        # print(self.id)
        # print(self.company_id.id)
        # print(self.company_name)
        return{
            'name':('Company Details'),
            'domain': [('id', '=', self.company_id.id)],
            'view_type': 'form',
            'res_model': 'employee.company',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    @api.onchange('math', 'phy', 'chem')
    def _calculate_total(self):
        self.total = self.math + self.phy + self.chem
        self.average = self.total / 3

    @api.depends('total')
    def _compute_average(self):
        for rec in self:
            # self.total = self.math + self.phy + self.chem
            rec.average = rec.total / 3

    @api.constrains('age')
    def _age_constraint(self):
        if self.age < 18:
            raise ValidationError("Age should be more than 18")

    @api.model
    def create(self, vals):
        if vals.get('emp_seq',"New") == "New":
            vals['emp_seq'] = self.env['ir.sequence'].next_by_code('employee.empseq') or "New"
        result = super(Employee, self).create(vals)
        return result


class Company(models.Model):
    _name = 'employee.company'
    _rec_name = "company_name"

    company_name = fields.Char("Name")
    city = fields.Char("City")
    emp_record_id = fields.One2many('employee', 'company_id', string="Employee Records")
    employee_count = fields.Integer(string="Employee Count", compute='emp_count')

    def emp_count(self):
        search = self.env['employee'].search([('company_id.id', '=', self.id)])
        count = self.env['employee'].search_count([('company_id.id', '=', self.id)])
        self.employee_count = count
        # return{
        #     'name':('Employee Details'),
        #     'domain': [('id', '=', self.company_id.id)],
        #     'view_type': 'form',
        #     'res_model': 'employee.company',
        #     'view_id': False,
        #     'view_mode': 'tree,form',
        #     'type': 'ir.actions.act_window',
        # }


class Skills(models.Model):
    _name = 'employee.skills'
    _rec_name="skills"

    skills = fields.Char('Skills')


class EmployeeSurvey(models.Model):
    _inherit = 'employee'

    rating = fields.Float('Rating')
