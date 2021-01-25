# -*- coding: utf-8 -*-
from odoo import api, fields, models, http
import uuid


class PortalProposal(models.Model):
    _name = 'portal.proposal'
    _description = 'Portal Proposal'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    user_id = fields.Many2one('res.users', string='Salesman')
    partner_id = fields.Many2one('res.partner', string='Customer')
    total_proposed_amt = fields.Float(
        string='Total Proposed Amount', compute='_get_total_proposed_accepted_amt')
    total_accepted_amt = fields.Float(
        string='Total Accepted Amount', compute='_get_total_proposed_accepted_amt')
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent'), (
        'confirmed', 'Confirmed'), ('cancel', 'Cancel')], default='draft', string='State')
    line_ids = fields.One2many(
        'portal.proposal.line', 'proposal_id', string='Proposal Lines')
    name = fields.Char(string='Number', copy=False)
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')
    link = fields.Char(string='Link')
    access_token = fields.Char(
        string='Access Token', default=lambda self: str(uuid.uuid4()))

    def _get_total_proposed_accepted_amt(self):
        for proposal in self:
            proposal.total_proposed_amt = sum(
                proposal.line_ids.mapped('proposed_price'))
            proposal.total_accepted_amt = sum(
                proposal.line_ids.mapped('accepted_price'))

    @api.model
    def create(self, vals):
        if not vals.get('name') or vals['name'] == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'portal.proposal') or _('New')
        return super(PortalProposal, self).create(vals)

    def action_send(self):
        access_token = self._portal_ensure_token()
        self.access_token = access_token
        web_base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        
        url = (web_base_url + '/proposal/%s') % (self.id)
        self.link = url

        template = self.env['mail.template'].search(
            [('model', '=', 'portal.proposal')])
        if template:
            email_values = {'email_to': self.partner_id.email,
                            'email_from': self.env.user.email or '', 'subject': 'Proposal Sent'}
            template.send_mail(self.id, email_values=email_values)

        self.state = 'sent'

    def refuse(self, proposal_id):
        rec = self.search([('id', '=', proposal_id)])
        rec.state = 'cancel'

    def accept_qty_price(self, qty_lst, price_lst, proposal_id, token):
        print("Called....")
        rec = self.search(
            [('id', '=', proposal_id)])
        message = ''
        for line in rec.line_ids:
            for qty_line in qty_lst:
                for price_line in price_lst:
                    if qty_line['prod'] == price_line['prod'] == str(line.product_id.id):
                        line.accepted_qty = qty_line['qty']
                        line.accepted_price = price_line['price']
                        message += ('Accepted qty is %s and accepted price is %s for product %s. \n') % (
                            line.accepted_qty, line.accepted_price, line.product_id.name)
        rec.sudo().message_post(body=message, email_from=rec.partner_id.email)

    def action_confirm(self):
        vals = {'partner_id': self.partner_id.id,
                'date_order': fields.Datetime.now(),
                'pricelist_id': self.pricelist_id.id
                }
        order = self.env['sale.order'].create(vals)

        for line in self.line_ids:
            vals = {'order_id': order.id,
                    'product_id': line.product_id.id,
                    'name': line.label,
                    'product_uom_qty': line.accepted_qty,
                    'price_unit': line.accepted_price,
                    'name': self.name
                    }
            self.env['sale.order.line'].create(vals)

        order.action_confirm()
        self.state = 'confirmed'
