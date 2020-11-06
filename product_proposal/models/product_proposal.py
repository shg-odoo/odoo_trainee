from odoo import models, fields, api, _


class ProductProposal(models.Model):
    _name = "product.proposal"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = "partner_id"

    user_id = fields.Many2one('res.users', string="Salesman", default=lambda self: self.env.user)
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    proposal_line_ids = fields.One2many('proposal.lines', 'proposal_id')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('accept', 'Accept'),
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

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('product.proposal') or _('New')
        result = super(ProductProposal, self).create(vals)
        return result

    def action_send_mail(self):
        print("action email ...............")
        template = self.env.ref('product_proposal.email_template_product_proposal')
        print("......................template", template)
        # # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)
        return self.write({'state': 'sent'})


    def _amount_total(self):
        pass

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_send(self):
        self.write({'state': 'sent'})

    def action_cancel(self):
        self.write({'state': 'cancel'})


class ProposalLines(models.Model):
    _name = "proposal.lines"

    proposal_id = fields.Many2one('product.proposal')
    product_id = fields.Many2one('product.product', string='Product')
    label = fields.Text(string='Product Label', required=True)
    qty_proposed = fields.Integer(string="Proposed Quantity", default="1")
    qty_accepted = fields.Integer(string="Accepted Quantity")
    price_proposed = fields.Float(string="Proposed Price")
    price_accepted = fields.Float(string="Accepted Price")
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    sub_total_proposed = fields.Monetary(string='SubTotal Proposed', store=True, readonly=True)
    sub_total_accepted = fields.Monetary(string='SubTotal Accepted', store=True, readonly=True)

    @api.onchange('product_id', 'qty_proposed', 'price_proposed')
    def _onchange_product_id(self):
        print("..............................prod name", self.product_id.name)
        self.label = self.product_id.name
        print("........................propsd price")
        self.price_proposed = self.product_id.lst_price
        print("............................subtotl proporsed", self.qty_proposed * self.price_proposed)
        self.sub_total_proposed = self.qty_proposed * self.price_proposed
