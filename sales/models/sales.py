#./odoo-bin --addons=addons,../enterprise,../odoo_trainee -d sale -u sales --db-filter=sale
from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class sales(models.Model):
	_name = "sales"
	_inherit=['mail.thread','mail.activity.mixin']
	_description="Sales Model"
	

  
	# _description = "Sales Model"
	number=fields.Char(string="Number",required=True,readonly=True,copy=False,default=lambda self:_('New'))
	order_date=fields.Date(string="create_date")
	partnet_id =fields.Many2one("sales.partner",string="Customer",store=True)
	sales_person = fields.Char(string="Sales Person")
	next_act=fields.Char(string="Next Activity")
	total = fields.Integer(string="Total")
	status=fields.Char(string="status")
	product=fields.Char(string="Product")
	des=fields.Char(string="Description")


	@api.model

   
	def create(self,vals):
		if vals.get('number',_('New'))==_('New'):
			vals['number']=self.env['ir.sequence'].next_by_code('sales') or _('New')
		result= super(sales,self).create(vals)
		return result	




class partner(models.Model):
	_name="sales.partner"
	_rec_name="sales_id"

	sales_id=fields.Char(string="Customer",store=True)
	company_add=fields.Char(string="Company Address")
	phone=fields.Char(string="Phpne no.")
	email=fields.Char(string="E-mail")



	


	
# class test(models.Model):
# 	_inherit = "sales"
# 	review = fields.Char(string="Review")