from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Manufacturer(models.Model):
    _name = 'manufacturer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = """ Details of Car Manufacturers """
    _rec_name = 'manufacturer_name'
    

    # company_id = fields.Many2one('manufacturer.consumption', string="Company ID")
    manufacturer_name = fields.Char('Name', track_visibility="always")
    city = fields.Char('City', track_visibility="always")
    company_address = fields.Text('Address', track_visibility="always")
    contact = fields.Char('Contact Number', track_visibility="always")
    production = fields.Integer('Production(Mts.)', track_visibility="always")
    labourers_record = fields.One2many('manufacturer.labourers', 'labourer_id', string="Labourers Record")
    machines = fields.Integer('Number of Machines', track_visibility="always")
    turnover = fields.Float('Turnover(Rs.)', track_visibility="always")
    consumption_record = fields.One2many('manufacturer.consumption', 'consumption_id', string="Consumption Record")
    employee_count = fields.Integer(string="Employee Count", compute='emp_count')
    consumption_days_count = fields.Integer(string="Cloth Consumption", compute='consumption_days')
    active = fields.Boolean('Active', default=True)
    # clothtype_id = fields.Many2one('manufacturer.clothtype', string="Cloth Type ID")

    def emp_count(self):
        search = self.env['manufacturer.labourers'].search([('labourer_id.id', '=', self.id)])
        count = self.env['manufacturer.labourers'].search_count([('labourer_id.id', '=', self.id)])
        self.employee_count = count

    def consumption_days(self):
        search = self.env['manufacturer.consumption'].search([('consumption_id', '=', self.id)])
        count = self.env['manufacturer.consumption'].search_count([('consumption_id', '=', self.id)])
        self.consumption_days_count = count


class Consumption(models.Model):
    _name = 'manufacturer.consumption'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'consumption_id'

    consumption_id = fields.Many2one('manufacturer', string="Company Name", track_visibility="always")
    # manufacturer_name = fields.Char('Name')
    clothtype = fields.Many2one('manufacturer.clothtype', string="Clothtype", track_visibility="always")
    cloth = fields.Integer('Cloth(Mts.)', track_visibility="always")
    color = fields.Integer('Color(Kg)', track_visibility="always")
    electricity = fields.Integer('Electricity Consumption(kW)', track_visibility="always")
    date = fields.Date("Date", track_visibility="always")


class Labourers(models.Model):
    _name = 'manufacturer.labourers'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'labourer_name'

    labourer_id = fields.Many2one('manufacturer', string="Company")
    labourer_name = fields.Char('Name', track_visibility="always")
    role_id = fields.Many2one('labourers.roles', string="Role", track_visibility="always")
    skills = fields.Many2many('labourers.skills', string="Skills", track_visibility="always")
    salary = fields.Integer('Salary(Rs.)', track_visibility="always")
    join_date = fields.Date('Joining Date', track_visibility="always")
    labourer_address = fields.Text('Address', track_visibility="always")
    

class ClothType(models.Model):
    _name = 'manufacturer.clothtype'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'clothtype_quality'

    clothtype_id = fields.One2many('manufacturer.consumption', 'clothtype', string="Clothtype")
    clothtype_quality = fields.Char('Quality', track_visibility="always")
    # type_of_wear = fields.Char('Type of Wear')
    colors = fields.Many2many('manufacturer.colors', string="Colors", track_visibility="always")
    price = fields.Integer('Price(Rs./mt.)', track_visibility="always")


class Colors(models.Model):
    _name = 'manufacturer.colors'
    _rec_name = 'colors'

    colors = fields.Char('Color')


class Skills(models.Model):
    _name = 'labourers.skills'
    _rec_name='skills'

    skills = fields.Char('Skills')


class Roles(models.Model):
    _name = 'labourers.roles'
    _rec_name = 'role'

    role = fields.Char('Role')
    role_rec = fields.One2many('manufacturer.labourers', 'role_id', string="Record with same role")
    