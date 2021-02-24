from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class sales(models.Model):
	_name="sales"
	_description="Sales Model"

	name=fields.Char(string="Number",require=True,readonly=True,
		                                 index=True,default=lambda self:_('New') )
	order_date=fields.Date(string="create_date")
	partner_id=fields.Many2one("sales.partner" ,string="Customer")
	sales_person=fields.Char(string="Sales Person")
	next_activity=fields.Char(string="Next Activity")
	total=fields.Integer(string="Total")


	@api.model
	def create(self,vals):
		if vals.get('name',_('New'))==_('New') :
			vals['name']=self.env['ir.sequence'].next_by_code('sales') or _('New') 

		result=super(sales,self).create(vals)
		return result	


class partner(models.Model):
	_name="sales.partner"
	_rec_name="company"

	company=fields.Char(string="Company")
	company_name=fields.Char(string="Company")
	company_address=fields.Char(string="Company address")
	company_state=fields.Char(string="Company State")
	company_country=fields.Char(string="Company country")
