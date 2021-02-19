from odoo import models, fields, api,_
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

class Sales(models.Model):
    _name = 'sales'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Sales Details"

    number_seq = fields.Char(string="Number", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    customer = fields.Char(string="Customer")
    invoice_date = fields.Date(string="Invoice Date")
    due_date = fields.Char(string="Due Date(Remaining days)")
    next_activity = fields.Many2one("sales.activity",string="Next Activity")
    taxt_included = fields.Integer(string="Tax Included")
    total = fields.Integer(string="Total")
    payment = fields.Selection([ ('paid', 'Paid'),('not_paid', 'Not Paid'),],'Payment')
    state = fields.Selection([
            ('draft','Draft'),
            ('confirm','Confirm'),
            ('done','Done'),
            ('cancel','Cancelled'),
    ], string='Status', readonly=True, default='draft')
    address = fields.Char("Address")
    sales_person = fields.Many2one("sales.salesmen",string="Sales Person")
    review = fields.Char("Customer Review")

    

    @api.onchange('invoice_date')
    def _get_due_date(self):
        if self.invoice_date:
            for rec in self:
                date_format = '%Y-%m-%d'
                joining_date = rec.invoice_date
                current_date = (datetime.today()).strftime(date_format)

                d1 = datetime.strptime(str(joining_date), date_format).date()
                d2 = datetime.strptime(str(current_date), date_format).date()
                r = relativedelta(d2,d1)
                rec.due_date = (r.years*365)+(r.months*30)+(r.days)





    @api.model
    def create(self,vals):
        if vals.get('number_seq',_('New')) == _('New'):
                vals['number_seq'] = self.env['ir.sequence'].next_by_code('sales.sequence') or _('New')
        result = super(Sales, self).create(vals)
        return result

     
    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Confirmed Your Sales Data Entry',
                    'type': 'rainbow_man',
                }
            }


    def action_done(self):
        for rec in self:
            rec.state = 'done'


                


class Activity(models.Model):
    _name = 'sales.activity'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "activity"

    activity_id = fields.One2many("sales","next_activity",string="Activity Id")
    activity = fields.Char("Activity")


class SalesMen(models.Model):
    _name = "sales.salesmen"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "sales_person"


    sales_person = fields.Char("Sales Person")
    contactNo = fields.Char("Contact")
    email = fields.Char("Email")
    salesman_id = fields.One2many("sales","next_activity",string="Sales Person Id")
