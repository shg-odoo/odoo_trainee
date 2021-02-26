from odoo import models, fields, api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class sales(models.Model):
	_name = "sales"
	_description="Sales Model"
	_rec_name="company_id"

  
	# _description = "Sales Model"

	name=fields.Char(string="Name")
	sales_person = fields.Char(string="Sales Person")
	total = fields.Integer(string="Total")
	image = fields.Binary(string="Image")
	order_date=fields.Date(string="create_date")
	company_id=fields.Char(string="Company")


	
# class test(models.Model):
# 	_inherit = "sales"
# 	review = fields.Char(string="Review")