from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class studentinherit(models.Model):
	_name="studentinherit"
	_inherit="student"

	number=fields.Integer(string="Numbers" ,required=True)
	