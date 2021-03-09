from odoo import models, fields, api

class Manufacturer(models.Model):
	_name = 'manufacturer'
	_description = """ Details of Car Manufacturers """

	company_id = fields.Many2one('manufacturer.consumption', string="Company ID")
	manufacturer_name = fields.Char("Name")
	city = fields.Char("City")
	company_address = fields.Text("Address")
	contact = fields.Char("Contact Number")
	production = fields.Char("Production")
	labour = fields.Integer("Number of Labourers")
	machines = fields.Integer("Number of Machines")
	turnover = fields.Char("Turnover")
	clothtype_id = fields.Many2one('manufacturer.clothtype', string="Cloth Type ID")


class Consumption(models.Model):
	_name = 'manufacturer.consumption'

	consumption_record = fields.One2many('manufacturer', 'company_id', string="Company Name")
	cloth = fields.Integer("Cloth(Mts.)")
	color = fields.Integer("Color(Kg)")
	electricity = fields.Integer("Electricity Consumption")
	date = fields.Date("Date")


class Labourers(models.Model):
	_name = 'manufacturer.labourers'

	labourers_record = fields.One2many('manufacturer', 'company_id', string="Labourers Record")
	labourers_id = fields.Many2one('manufacturer.labourers', string="Labourers ID")
	labourer_name = fields.Char("Name")
	role = fields.Char("Role")
	skills = fields.Many2many('labourers.skills', "Skills")
	salary = fields.Integer("Salary")
	join_date = fields.Date("Joining Date")
	labourer_address = fields.Text("Address")

	

class ClothType(models.Model):
	_name = 'manufacturer.clothtype'

	clothtype_record = fields.One2many('manufacturer', 'clothtype_id', string="Clothtype ID")
	clothtype_quality = fields.Char("Quality")
	type_of_wear = fields.Char("Type")
	colors = fields.Many2many('manufacturer.colors', string="Colors")
	price = fields.Integer("Price")



class Colors(models.Model):
	_name = 'manufacturer.colors'

	color_name = fields.Char("Color")


class Skills(models.Model):
    _name = 'labourers.skills'
    _rec_name="skills"

    skills = fields.Char('Skills')