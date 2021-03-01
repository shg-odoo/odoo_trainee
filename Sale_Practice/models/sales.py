from odoo import models, fields, api, exceptions
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta

class SaleOrder(models.Model):
    _name = "sale.order"
    _description = "Sales Order"
    
    number = fields.Char(string = "Number")
    creationDate = fields.Date(string="Creation Date")
    customer = fields.Char(string = "Customer")
    salesPerson = fields.Char(string = "Sales Person")
    nextActivity = fields.Char(string = "Next Activity")
    total = fields.Char(string="Total")
    