from odoo import models, fields, api, exceptions
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

class SaleOrder(models.Model):
    _name = "sale.order"
    _description = "Sales Order"
    
    number = fields.Char("String Number")
    creationDate = fields.Datetime(string="Creation Date")