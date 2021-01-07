from odoo import api, fields, models, _




class Proposal(models.Model):
	_name = "proposal.proposal"
	_inherit = ['mail.thread','portal.mixin','mail.activity.mixin']
	_description = "Manage Proposal" 
	_rec_name = "customer_id"

	seq = fields.Char(string="Number", readonly="True")
	proposal_date = fields.Date(string="Proposal Date", default=fields.Datetime.now, required=True)
	customer_id = fields.Many2one("res.partner", string="Customer", required=True)
	salesman_id = fields.Many2one("res.users",string="Sales Person", default =lambda self: self.env.user, required=True)
	proposal_line_ids = fields.One2many("proposal.line", "proposal_id")
	state = fields.Selection([('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')],default="draft", string="Status")
	proposed_total_price = fields.Float(compute = '_compute_proposed_total', default = 0.0, store=True, readonly=True, string="Proposed Total")
	accepted_total_price = fields.Float(compute = '_compute_accepted_total', default = 0.0, store=True, readonly=True, string="Accepted Total")
  	# proposal_status = fields.Selection([('accept','Accepted'),
   #      								('reject','Rejected'),
   #      								('no_response','No Response')],default="no_response")

	@api.model
	def create(self, values):
	        if values.get('seq', _('New')) == _('New'):
	            values['seq'] = self.env['ir.sequence'].next_by_code('proposal.proposal') or _('New')
	        crt = super(Proposal, self).create(values)
	        return crt

	@api.depends('proposal_line_ids')
	def _compute_proposed_total(self):
		proposed_total = []
		if self.proposal_line_ids:
			for line in self.proposal_line_ids:
				line.proposed_sub_total = line.qty_proposed * line.price_proposed
				proposed_total.append(line.proposed_sub_total)
			self.proposed_total_price = sum(proposed_total)

	@api.depends('proposal_line_ids')
	def _compute_accepted_total(self):
		total = []
		if self.proposal_line_ids:
			for line in self.proposal_line_ids:
				line.accepted_sub_total = line.qty_accepted * line.price_accepted
				total.append(line.accepted_sub_total)    
			self.accepted_total_price = sum(total)

	def action_proposal_mail_send(self):
		self.state = "sent"

	def action_confirmed_proposal(self):
		# self.write({'state': 'confirmed'})
		self.state = "confirmed"

	def action_cancel_proposal(self):
		self.state = "cancel"

	def preview_proposal(self):
		self.ensure_one()
		return {
            'type': 'ir.actions.act_url',
            # 'target': 'self',
            # 'url': f'/my/proposal/{self.id}'
        }

class ProposalLine(models.Model):
	_name = "proposal.line"
	_description = "Proposal Line" 
	_rec_name = "product_id"

	proposal_id = fields.Many2one("proposal.proposal", string="Proposal Id")
	product_id = fields.Many2one("product.product", string="Product", required=True)
	description = fields.Text()
	qty_proposed = fields.Integer(string="Proposed Quantity", required=True, default=1)
	price_proposed = fields.Char(string=" Price Proposed(per unit)")
	qty_accepted = fields.Integer(default=1)
	price_accepted = fields.Float(string="Accepted Price(per unit)")
	proposed_sub_total = fields.Float(default = 0.0, readonly=True)
	accepted_sub_total = fields.Float(default = 0.0, readonly=True)

	@api.onchange('price_proposed', 'qty_proposed')
	def accepted_price_qty_change(self):
		self.qty_accepted = self.qty_proposed
		self.price_accepted = self.price_proposed 

	@api.onchange('product_id')
	def DEscription_change(self):
		self.description = self.product_id.name