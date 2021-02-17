from odoo import models, fields, api,_
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class Sales(models.Model):
    _name = 'sales'
    _description = "Sales Details"

    number_seq = fields.Char(string="Number", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    customer = fields.Char(string="Customer")
    invoice_date = fields.Date(string="Invoice Date")
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    due_date = fields.Char(string="Due Date",readonly=True)
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

    
    # @api.onchange('invoice_date','current_date')
    # def _get_due_date(self):
    #    start_date = datetime.strptime(str(self.invoice_date), '%Y-%m-%d')
    #    end_date = datetime.strptime(str(self.current_date), '%Y-%m-%d')
            # rec.due_date = ((end_date - start_date).days)




    @api.model
    def create(self,vals):
        if vals.get('number_seq',_('New')) == _('New'):
                vals['number_seq'] = self.env['ir.sequence'].next_by_code('sales.sequence') or _('New')
        result = super(Sales, self).create(vals)
        return result

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'


    def action_done(self):
        for rec in self:
            rec.state = 'done'


                


class Activity(models.Model):
    _name = 'sales.activity'
    _rec_name = "activity"

    activity_id = fields.One2many("sales","next_activity",string="Activity Id")
    activity = fields.Char("Activity")
