from odoo import models, fields, api, exceptions


class Proposals(models.Model):
    _name = 'proposals.proposals'
    _description = "Sales Proposal"
    _inherit = ['mail.thread']

    def action_sent_proposal(self):
    	self.state = "sent"
    	self.env['mail.templates'].browse(proposal_email_template).send_mail()

    proposal_name = fields.Char()
    sales_man_id = fields.Many2one("res.users",string="Salesman")
    customer_id = fields.Many2one("res.partner")
    price_list = fields.Many2one("product.pricelist")
    proposal_line_ids = fields.One2many("proposals.line", 'proposal_id')
    state = fields.Selection([('draft','Draft'),
    	('sent','Sent'),
    	('confirmed','Confirmed'),
    	('cancel','Cancel')],default="draft")

class ProposaLisList(models.Model):
	_name = 'proposals.line'

	product_id = fields.Many2one("product.product")
	description = fields.Text()
	qty_proposed = fields.Integer()
	price_proposed = fields.Float()
	qty_accepted = fields.Integer()
	price_accepted = fields.Float()
	proposal_id = fields.Many2one("proposals.proposals")