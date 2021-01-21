# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PortalProposalLines(models.Model):
    _name = 'portal.proposal.line'
    _description = 'Portal Proposal Lines'

    product_id = fields.Many2one('product.product', string='Product')
    label = fields.Char(string='Description')
    proposed_qty = fields.Integer(string='Qty Proposed', default=1)
    accepted_qty = fields.Integer(string='Qty Accepted')
    proposed_price = fields.Float(
        string='Price Proposed')
    accepted_price = fields.Float(string='Price Accepted')
    proposal_id = fields.Many2one('portal.proposal', string='Proposal')

    @api.onchange('product_id')
    def onchange_product(self):
        if self.product_id and self.proposal_id.pricelist_id:
            if self.proposal_id.pricelist_id.discount_policy == 'with_discount':
                self.proposed_price = self.product_id.with_context(
                    pricelist=self.proposal_id.pricelist_id.id).price
            product_context = dict(
                self.env.context, partner_id=self.proposal_id.partner_id.id, date=fields.Date.today())
            final_price, rule_id = self.proposal_id.pricelist_id.with_context(
                product_context).get_product_price_rule(self.product_id, 1.0, self.proposal_id.partner_id)
            self.proposed_price = final_price

    @api.onchange('proposed_qty', 'proposed_price')
    def onchange_proposed_qty(self):
        self.accepted_qty = self.proposed_qty if self.proposed_qty else 1
        self.accepted_price = self.proposed_price if self.proposed_price else 0
