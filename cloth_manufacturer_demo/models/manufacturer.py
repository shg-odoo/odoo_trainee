from odoo import models, fields, api

class Manufacturer(models.Model):
	_name = 'manufacturer'
	_description = """ Details of Car Manufacturers """
	_rec_name = 'manufacturer_name'

	# company_id = fields.Many2one('manufacturer.consumption', string="Company ID")
	manufacturer_name = fields.Char('Name')
	city = fields.Char('City')
	company_address = fields.Text('Address')
	contact = fields.Char('Contact Number')
	production = fields.Integer('Production(Mts.)')
	labourers_record = fields.One2many('manufacturer.labourers', 'labourer_id', string="Labourers Record")
	machines = fields.Integer('Number of Machines')
	turnover = fields.Float('Turnover(Rs.)')
	consumption_record = fields.One2many('manufacturer.consumption', 'consumption_id', string="Consumption Record")
	# clothtype_id = fields.Many2one('manufacturer.clothtype', string="Cloth Type ID")


class Consumption(models.Model):
	_name = 'manufacturer.consumption'
	_rec_name = 'consumption_id'

	consumption_id = fields.Many2one('manufacturer', string="Company Name")
	# manufacturer_name = fields.Char('Name')
	clothtype = fields.Many2one('manufacturer.clothtype', string="Clothtype")
	cloth = fields.Integer('Cloth(Mts.)')
	color = fields.Integer('Color(Kg)')
	electricity = fields.Integer('Electricity Consumption(kW)')
	date = fields.Date("Date")


class Labourers(models.Model):
	_name = 'manufacturer.labourers'
	_rec_name = 'labourer_name'

	labourer_id = fields.Many2one('manufacturer', string="Company")
	labourer_name = fields.Char('Name')
	role_id = fields.Many2one('labourers.roles', string="Role")
	skills = fields.Many2many('labourers.skills', "Skills")
	salary = fields.Integer('Salary(Rs.)')
	join_date = fields.Date('Joining Date')
	labourer_address = fields.Text('Address')
	

class ClothType(models.Model):
	_name = 'manufacturer.clothtype'
	_rec_name = 'clothtype_quality'

	clothtype_id = fields.One2many('manufacturer.consumption', 'clothtype', string="Clothtype")
	clothtype_quality = fields.Char('Quality')
	# type_of_wear = fields.Char('Type of Wear')
	colors = fields.Many2many('manufacturer.colors', string="Colors")
	price = fields.Integer('Price(Rs./mt.)')


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
	