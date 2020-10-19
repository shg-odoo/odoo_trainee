from odoo import models, fields, api, _


class SaleProposal(models.Model):
    _name = "sale.proposal"
    _rec_name = "partner_id"

    user_id = fields.Many2one('res.users', string="Salesman",default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string="Customer")
    proposal_line_ids=fields.One2many('proposal.lines','proposal')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], default='draft')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    name_seq = fields.Char(string="Proposal Sequence", copy=False, required=True, index=True,
                           default=lambda self: _('New'))

class ProposalLines(models.Model):
    _name = "proposal.lines"

    Product_id = fields.Many2one('product.product', string='Product')
    label = fields.Text(string='Description', required=True)
    qty_proposed=fields.Integer(string="Quantity Proposed")
    qty_accepted=fields.Integer(string="Quantity Accepted")
    price_proposed=fields.Float(string="Price Proposed")
    price_accepted=fields.Float(string="Price Accepted")
    amt_total_proposed=fields.Float(string="Amount total proposed")
    amt_total_accepted=fields.Float(string="Amount total accepted")
    proposal=fields.Many2one('sale.proposal')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)



