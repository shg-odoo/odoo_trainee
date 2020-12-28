# -*- coding: utf-8 -*-
# python3 odoo-bin --addons addons/,/home/mub/Munaf --xmlrpc-port=9999 -d self_proposal -u odoo_trainee

from odoo import models, fields, api, _

class Proposal(models.Model):
    """docstring for Praposal"""
    _name = 'sale.proposal'
    _inherit = ['mail.thread','portal.mixin','mail.activity.mixin']
    _description = "Sales Proposal by salesman to the customer"
    _rec_name = 'proposal_name'

    proposal_name = fields.Char(default=lambda self: _('New'), readonly = True)
    salesman_id = fields.Many2one('res.users', string='Salesman', default=lambda self: self.env.user)
    customer_id = fields.Many2one('res.partner', string='Customer')
    price_list_id = fields.Many2one("product.pricelist", required=True)
    proposal_line_ids = fields.One2many("proposal.line", 'proposal_id')
    state = fields.Selection([('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')], default='draft')
    proposal_date = fields.Datetime('Proposal Date',readonly=True, default=lambda self: fields.Datetime.now())
    proposed_total_price = fields.Float(compute = '_compute_proposed_total', default = 0.0, store=True, readonly=True)
    accepted_total_price = fields.Float(compute = '_compute_accepted_total', default = 0.0, store=True, readonly=True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    proposal_status = fields.Selection([('accept','Accepted'),
        ('reject','Rejected'),
        ('no_response','No Response')],default="no_response")
    fiscal_position_id = fields.Many2one(
        'account.fiscal.position', string='Fiscal Position')
    note = fields.Text(string='Description')

    untaxed_amount = fields.Float('Amount Untaxed', readonly=True, store=True, compute='calculate_total_amount')
    taxes = fields.Float('Taxes', readonly=True, store=True, compute='calculate_total_amount')
    total = fields.Float('Total', readonly=True, store=True, compute='calculate_total_amount')

    @api.model
    def get_record_counter(self):
        data = {stat:self.env['sale.proposal'].sudo().search_count([('state','=', stat)]) for stat in ['draft','sent','confirmed','cancel']}
        return data

    def _get_portal_return_action(self):
        """ Return the action used to display orders when returning from customer portal. """
        self.ensure_one()
        return self.env.ref('odoo_trainee.menu_root')

    @api.model
    def create(self, vals):
        if vals.get('proposal_name', _('New')) == _('New'):
            seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.now())
            vals['proposal_name'] = self.env['ir.sequence'].next_by_code('sale.proposal', sequence_date=seq_date) or _('New')
        result = super(Proposal, self).create(vals)
        return result

    def preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            # 'target': 'self',
            'url': f'/my/proposals/{self.id}'
        }

    def action_proposal_mail_send(self):
        self.state = "sent"
        template_id = self.env.ref('odoo_trainee.email_template_proposal_mail').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    def action_confirmed_proposal(self):
        self.state = "confirmed"
        sale_order_line_ids = []
        sale_order_tuple_line_ids = ()
        for rec in self:
            for line in rec.proposal_line_ids:
                sale_order_list_line_ids = [0,0]
                sale_order_list_line_ids.append(({'product_id':line.product_id.id,'name':line.description,'product_uom_qty':line.qty_accepted,'price_unit':line.price_accepted}))
                sale_order_tuple_line_ids = tuple(sale_order_list_line_ids)
                sale_order_line_ids.append(sale_order_tuple_line_ids)
        self.env['sale.order'].create({'partner_id':self.customer_id.id,'order_line':sale_order_line_ids,'state':'sale'})
        template_id = self.env.ref('odoo_trainee.email_template_proposal_mail').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    def action_cancel_proposal(self):
        self.state = "cancel"

    @api.depends('proposal_line_ids')
    def calculate_total_amount(self):
        if self.proposal_line_ids:
            untaxed = 0
            total_taxes = 0
            for record in self.proposal_line_ids:
                untaxed += record.price_proposed
                if record.tax_id:
                    for tax in record.tax_id:
                        amo = record.price_proposed * tax.amount / 100
                        total_taxes += amo
            self.untaxed_amount = untaxed
            self.taxes = total_taxes
            self.total = self.untaxed_amount + self.taxes
            self.accepted_total_price = self.untaxed_amount + self.taxes
            # self.proposed_total_price = self.accepted_total_price

class Proposalline(models.Model):
    _name = 'proposal.line'
    _description = 'product lines for sale proposal'

    proposal_id = fields.Many2one("sale.proposal")
    product_id = fields.Many2one('product.product', string='Product', ondelete='cascade', help="Select a product for Proposal.")
    description = fields.Text()
    qty_proposed = fields.Integer(string='Quantity', default=1)
    unit_price = fields.Float(string='Price Proposed')
    price_proposed = fields.Float("Total Price", digits='Product Price')
    qty_accepted = fields.Integer(default=1)
    price_accepted = fields.Float("Price Accepted(per unit)")
    tax_id = fields.Many2many('account.tax', string='Taxes')

    @api.onchange('qty_proposed')
    def change_price_on_qty(self):
        if self.qty_proposed:
            self.price_proposed = self.product_id.lst_price * self.qty_proposed

    @api.onchange('product_id')
    def onchange_products(self):
        if self.product_id:
            self.unit_price = self.product_id.lst_price
            self.description = self.product_id.description or self.product_id.description_sale
            self.price_proposed = self.product_id.lst_price