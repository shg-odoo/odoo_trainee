from odoo import api, fields, models, _


class PortalProposalLines(models.Model):
    _name = 'portal.proposal.line'
    _description = 'Portal Proposal Lines'

    product_id = fields.Many2one('product.product',string='Product')
    label = fields.Char(string='Description')
    proposed_qty = fields.Integer(string='Qty Proposed')
    accepted_qty = fields.Integer(string='Qty Accepted',compute="_get_default_proposed")
    proposed_price = fields.Float(string='Price Proposed',compute='_get_proposed_price')
    accepted_price = fields.Float(string='Price Accepted',compute="_get_default_proposed") 
    proposal_id = fields.Many2one('portal.proposal',string='Proposal')

    def _get_proposed_price(self):
    	for line in self:
    		price = 0
    		for item in line.proposal_id.pricelist_id.item_ids:
    			if item.product_tmpl_id == line.product_id.product_tmpl_id:
    				price = item.fixed_price
    		line.proposed_price = (line.product_id.standard_price + price) * line.proposed_qty

    def _get_default_proposed(self):
    	for line in self:
    		line.accepted_qty = line.proposed_qty
    		line.accepted_price = line.proposed_price