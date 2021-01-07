from odoo import api, fields, models, _
from werkzeug.urls import url_join


class PortalProposal(models.Model):
	_name = 'portal.proposal'
	_description = 'Portal Proposal'
	_inherit = ['mail.thread', 'mail.activity.mixin']

	user_id = fields.Many2one('res.users',string='Salesman')
	partner_id = fields.Many2one('res.partner',string='Customer')
	total_proposed_amt = fields.Float(string='Total Proposed Amount',compute='_get_total_amt')
	total_accepted_amt = fields.Float(string='Total Accepted Amount',compute='_get_total_amt')
	state = fields.Selection([('draft','Draft'),('sent','Sent'),('confirmed','Confirmed'),('cancel','Cancel')],default='draft',string='State')
	line_ids = fields.One2many('portal.proposal.line','proposal_id',string='Proposal Lines')
	name = fields.Char(string='Number', copy=False)
	pricelist_id = fields.Many2one('product.pricelist',string='Pricelist')

	def _get_total_amt(self):
		for proposal in self:
			count = count1 = 0
			for line in proposal.line_ids:
				count += line.proposed_price
				count1 += line.accepted_price
			proposal.total_proposed_amt = count
			proposal.total_accepted_amt = count1

	@api.model
	def create(self, vals):
		if not vals.get('name') or vals['name'] == _('New'):
			vals['name'] = self.env['ir.sequence'].next_by_code('portal.proposal') or _('New')
		return super(PortalProposal, self).create(vals)


	def send(self):
		web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
		# action = self.env.ref('portal_proposal.proposal_action')
		# menu = self.env.ref('portal_proposal.proposal_menu')
		# record_url = "/web#id=%s&action=%s&model=portal.proposal&view_type=form&menu_id=%s" % (self.id, action.id, menu.id)
		# url = url_join(web_base_url,record_url)
		url = web_base_url + '/proposal/' + str(self.id)
		url = '<a href="%s">here</a>'%(url)
		vals = {'recipient_ids':[self.partner_id.id],
				'subject':'Proposal Sent',
				'body_html':'The link to the proposal %s is %s.'%(self.name,url)
		}
		self.env['mail.mail'].create(vals)
		self.state = 'sent'

	def accept(self):
		pass

	def refuse(self):
		self.state = 'cancel'

	def accept_qty_price(self):
		print("CALLED")
		return {}

	def confirm(self):
		vals = {'partner_id':self.partner_id.id,
				'date_order':fields.Datetime.now(),
				'pricelist_id':self.pricelist_id.id
				}
		order = self.env['sale.order'].create(vals)
		
		for line in self.line_ids:
			vals = {'order_id':order.id,
					'product_id':line.product_id.id,
					'name':line.label,
					'product_uom_qty':line.accepted_qty,
					'price_unit':line.accepted_price,
					'name':self.name 
					}
			self.env['sale.order.line'].create(vals)
		
		order.action_confirm()
		self.state = 'confirmed'