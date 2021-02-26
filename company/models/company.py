from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class company(models.Model):
	_name="company"
	_inherit="sales"
	_description="Company Details"

	name=fields.Char(string="Company Name")
	address=fields.Char(string="Adress")
	sales_id=fields.Many2one("sales",string="Sales")
    
