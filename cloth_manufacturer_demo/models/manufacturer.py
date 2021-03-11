from odoo import models, fields, api

class Manufacturer(models.Model):
	_name = 'manufacturer'
	_description = """ Details of Car Manufacturers """

	company_id = fields.Many2one('manufacturer.consumption', string="Company ID")
	manufacturer_name = fields.Char('Name')
	city = fields.Char('City')
	company_address = fields.Text('Address')
	contact = fields.Char('Contact Number')
	production = fields.Char('Production')
	labourers_record = fields.One2many('manufacturer.labourers', 'manufacturer_id', string="Labourers Record")
	machines = fields.Integer('Number of Machines')
	turnover = fields.Char('Turnover')
	consumption_record = fields.One2many('manufacturer.consumption', 'consumption_id', string="Consumption Record")
	# clothtype_id = fields.Many2one('manufacturer.clothtype', string="Cloth Type ID")


class Consumption(models.Model):
	_name = 'manufacturer.consumption'

	consumption_id = fields.Many2one('manufacturer', string="Company Name")
	# manufacturer_name = fields.Char('Name')
	clothtype_id = fields.Many2one('manufacturer.clothtype', string="Cloth type")
	cloth = fields.Integer('Cloth(Mts.)')
	color = fields.Integer('Color(Kg)')
	electricity = fields.Integer('Electricity Consumption')
	date = fields.Date("Date")


class Labourers(models.Model):
	_name = 'manufacturer.labourers'

	manufacturer_id = fields.Many2one('manufacturer', string="Labourers ID")
	labourer_name = fields.Char('Name')
	role = fields.Char('Role')
	skills = fields.Many2many('labourers.skills', "Skills")
	salary = fields.Integer('Salary')
	join_date = fields.Date('Joining Date')
	labourer_address = fields.Text('Address')
	

class ClothType(models.Model):
	_name = 'manufacturer.clothtype'

	clothtype_record = fields.One2many('manufacturer.consumption', 'clothtype_id', string="Clothtype ID")
	clothtype_quality = fields.Char('Quality')
	type_of_wear = fields.Char('Type of Wear')
	colors = fields.Many2many('manufacturer.colors', string="Colors")
	price = fields.Integer('Price')


class Colors(models.Model):
	_name = 'manufacturer.colors'
	_rec_name = 'colors'

	colors = fields.Char('Color')


class Skills(models.Model):
    _name = 'labourers.skills'
    _rec_name='skills'

    skills = fields.Char('Skills')