from odoo import models, fields, api,_
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

class Sales(models.Model):
    _name = 'sales'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Sales Details"

    number_seq = fields.Char(string="Number", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    customer = fields.Many2one("sales.customers", string="Customer")
    invoice_date = fields.Date(string="Invoice Date", track_visibility="always")
    due_date = fields.Char(string="Due Date(Remaining days)")
    next_activity = fields.Many2one("sales.activity",string="Next Activity")
    taxt_included = fields.Integer(string="Tax Included")
    total = fields.Integer(string="Total")
    payment = fields.Selection([ ('paid', 'Paid'),('not_paid', 'Not Paid'),],'Payment', track_visibility="always")
    state = fields.Selection([
            ('draft','Draft'),
            ('confirm','Confirm'),
            ('done','Done'),
            ('cancel','Cancelled'),
    ],string='Status', readonly=True, default='draft')
    address = fields.Char("Address")
    sales_person = fields.Many2one("sales.salesmen", string="Sales Person")
    review = fields.Char("Customer Review")
    active = fields.Boolean('Active',default=True)

    

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
            


    def action_done(self):
        for rec in self:
            rec.state = 'done'
            return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Done Your Sales Data Entry',
                    'type': 'rainbow_man',
                }
            }

    
    def test_recordset(self):
        for rec in self:
            print("Odoo ORM: Record set Operations")
            salesman = self.env['sales.salesmen'].search([])
            print("Mapped salesman..",salesman.mapped('sales_person'))
            print("Sorted salesman..",salesman.sorted(lambda o: o.write_date,reverse=True))
            print("Filtered salesman..",salesman.filtered(lambda o:  o.email))

    
    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s %s' % (field.number_seq, field.customer)))
        return res 


    def open_sales_salesperson(self):
            return {
                'name': _('SalesMen'),
                'domain': [('salesman_id','=',self.id)],
                'view_type': 'form',
                'res_model': 'sales.salesmen',
                'view_id': False,
                'view_mode': 'tree,form',
                'type': 'ir.actions.act_window',
            }



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
    salesman_id = fields.One2many("sales","sales_person",string="Sales Person Id")
    current_date = fields.Date(string="Current Date",default=lambda s: fields.Date.context_today(s))
    image = fields.Binary(string='Image')


class Products(models.Model):
    _name = "sales.products"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = "sales_person"


    product_seq = fields.Char(string="Product Sequence", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    product_name = fields.Char(string="Product Name")
    color = fields.Integer("Color")
    price = fields.Char("Price")
    image = fields.Binary(string='Image')


    @api.model
    def create(self,vals):
        if vals.get('product_seq',_('New')) == _('New'):
                vals['product_seq'] = self.env['ir.sequence'].next_by_code('sales.products.sequence') or _('New')
        result = super(Products, self).create(vals)
        return result

    
