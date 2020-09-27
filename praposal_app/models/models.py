# -*- coding: utf-8 -*
from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.addons import decimal_precision as dp


class Proposal(models.Model):
    _name = 'proposal.order'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Proposal'

    name = fields.Char(string="Proposal No", required=True, copy=False, store=True, readonly=True, index=True, default = lambda self: _('New'))
    proposal_line = fields.One2many('proposal.order.line', "proposal_id", string="Proposal Lines")
    date_order = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True, default = fields.Datetime.now)
    total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always')   
    note =fields.Text('Note')
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('sent', 'Sent'),('proposal_accepted','Proposal Accepted'),('confirm', 'Confirmed'), ('cancel', 'Cancel')], default="draft")
    confirm_date = fields.Datetime(string='Confirm Date')
    types_name = fields.Char('Types Name', compute='_compute_types_name')
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1)
    user_id = fields.Many2one('res.users', string="Users")
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get('proposal.order'))
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist', readonly=True,)
    currency_id = fields.Many2one("res.currency", related='company_id.currency_id', string="Currency", readonly=True, )
    amount_untaxed = fields.Monetary(string='Proposed Total', store=True, readonly=True, compute='_amount_all', track_visibility='onchange', track_sequence=5)
    accepted_total = fields.Monetary(string='Accepted Total', readonly=True, store=True,compute='_amount_all', track_visibility='onchange', track_sequence=5)
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('proposal.order') or _('New')
        return super(Proposal, self).create(vals)

    @api.depends('proposal_line.price_subtotal','proposal_line.accepted_subtotal')
    def _amount_all(self):
        for order in self:
            amount_untaxed  = 0.0
            accepted_total = 0.0
            for line in order.proposal_line:
                amount_untaxed += line.price_subtotal
                accepted_total += line.accepted_subtotal
            order.update({
                'amount_untaxed': amount_untaxed,
                'accepted_total': accepted_total,
                'total': amount_untaxed + accepted_total
                })


    @api.multi
    def action_confirm(self):
        return self.write(
            {'state': 'confirm',
            'confirm_date': fields.Datetime.now(),
            }) 

    @api.multi
    def action_cencle(self):
        return self.write({'state': 'cancel'})


    def preview_proposal_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    def _compute_access_url(self):
        super(Proposal, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/proposal/%s' % (order.id)


    @api.multi
    @api.depends('state')
    def _compute_types_name(self):
        for record in self:
            record.types_name = _('Proposal') if record.state in ('draft', 'sent', 'cancel') else _('Proposal Order')



    @api.multi 
    def action_proposal_send(self):
        template_id = self.env.ref('praposal_app.proposal_email_template').id
        print("#"*20,template_id)
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        return self.write({'state': 'sent'})   


class Proposallines(models.Model):
    _name = 'proposal.order.line'
    _description = 'Proposal Lines'

    proposal_id = fields.Many2one('proposal.order','Proposal Id')
    product = fields.Many2one('product.product','Products')
    name = fields.Text("Description")
    qty_propos = fields.Integer("Proposed Quantity",default=1)
    price_propos = fields.Float("Price Proposed",)
    qty_acept = fields.Integer("Qty Accepted",)
    price_acept = fields.Float("Price Accepted",)
    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    accepted_subtotal = fields.Float(compute='_compute_amount', string='Accepted SubTotal', readonly=True, store=True)
  
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")

    @api.depends('qty_propos','price_propos','price_acept')
    def _compute_amount(self):
        price_sub = 0.0
        accpt_price =0.0
        for line in self:
            price_sub =line.qty_propos * line.price_propos
            accpt_price = line.qty_acept * line.price_acept
            print("@@@"*20,accpt_price)
            line.update({
                    'price_subtotal': price_sub,
                    'accepted_subtotal': accpt_price,
            })

    @api.onchange('product')
    def _onchange_price(self):
        price_obj = self.env['product.product'].browse(self.product.id)
        self.price_propos = price_obj.list_price
        self.price_acept = price_obj.list_price
        self.name = price_obj.description

    @api.onchange('qty_propos')
    def _onchange_qty(self):
        self.qty_acept = self.qty_propos