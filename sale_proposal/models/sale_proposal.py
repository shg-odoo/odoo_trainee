from odoo import models, fields, api, _


class SaleProposal(models.Model):
    _name = "sale.proposal"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = "partner_id"

    user_id = fields.Many2one('res.users', string="Salesman", default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string="Customer",required=True)
    proposal_line_ids = fields.One2many('proposal.lines', 'proposal_id')
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
    date_proposal = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True,
                                    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False,
                                    default=fields.Datetime.now)
    proposed_total = fields.Monetary(string='Proposed Total', store=True, readonly=True, compute='_amount_total')
    accepted_total = fields.Monetary(string='Accepted Total', store=True, readonly=True, compute='_amount_total')
    total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_total')
    proposal_status = fields.Selection([('accept', 'Accepted'),
                                        ('reject', 'Rejected'),
                                        ('pending', 'Pending')], default="pending")

    def action_send_mail(self):
        template_id = self.env.ref('sale_proposal.mail_proposal_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        return self.write({'state': 'sent'})

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('sale.proposal') or _('New')
        result = super(SaleProposal, self).create(vals)
        return result

    @api.depends('proposal_line_ids.amt_total_proposed', 'proposal_line_ids.amt_total_accepted')
    def _amount_total(self):
        for order in self:
            proposed_total = 0.0
            accepted_total = 0.0
            for line in order.proposal_line_ids:
                proposed_total += line.amt_total_proposed
                accepted_total += line.amt_total_accepted
                print(proposed_total)
                print(accepted_total, 'accpt')

            order.update({
                'proposed_total': proposed_total,
                'accepted_total': accepted_total,
                'total': proposed_total + accepted_total
            })

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_send(self):
        self.write({'state': 'sent'})

    def action_cancell(self):
        self.write({'state': 'cancel'})

    def preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    def _get_share_url(self, redirect=False, signup_partner=False, pid=None):
        self.ensure_one()
        return super(SaleProposal, self)._get_share_url(redirect, signup_partner, pid)

    def _compute_access_url(self):
        super(SaleProposal, self)._compute_access_url()
        for proposal in self:
            proposal.access_url = '/my/proposals/%s' % (proposal.id)

    def _get_report_base_filename(self):
        self.ensure_one()
        return '%s' % (self.name_seq)


class ProposalLines(models.Model):
    _name = "proposal.lines"

    product_id = fields.Many2one('product.product', string='Product')
    label = fields.Text(string='Description', required=True)
    qty_proposed = fields.Integer(string="Quantity Proposed", default="1")
    qty_accepted = fields.Integer(string="Quantity Accepted")
    price_proposed = fields.Float(string="Price Proposed")
    price_accepted = fields.Float(string="Price Accepted")
    amt_total_proposed = fields.Float(string="Amount total proposed")
    amt_total_accepted = fields.Float(string="Amount total accepted")
    proposal_id = fields.Many2one('sale.proposal')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        self.price_proposed = self.product_id.lst_price
        self.label = self.product_id.name

    @api.onchange('qty_proposed', 'price_proposed')
    def _onchange_proposal(self):
        self.amt_total_proposed = self.qty_proposed * self.price_proposed

    @api.onchange('qty_accepted', 'price_accepted')
    def _onchange_proposal_accepted(self):
        self.amt_total_accepted = self.qty_accepted * self.price_accepted
