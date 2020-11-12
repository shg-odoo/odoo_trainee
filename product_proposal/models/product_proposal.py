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
        ('confirm', 'Confirm'),
        ('cancel', 'Cancelled')], default='draft')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    name_seq = fields.Char(string="Proposal Sequence", copy=False, required=True, index=True,
                           default=lambda self: _('New'))
    date_proposal = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True,
                                    states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False,
                                    default=fields.Datetime.now)
    proposed_total = fields.Monetary(string='Proposed Total', store=True, compute='_compute_proposed_total')
    accepted_total = fields.Monetary(string='Accepted Total', store=True)
    total_amt = fields.Monetary(string='Total', store=True, readonly=True)
    # pricelist_id = fields.Many2one(
    #     'product.pricelist', string='Pricelist', check_company=True,  # Unrequired company
    #     required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
    #     help="If you change the pricelist, only newly added lines will be affected.")
    # currency_id = fields.Many2one(related='pricelist_id.currency_id',store=True)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)

    # add pricelist,tax

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('product.proposal') or _('New')
        result = super(ProductProposal, self).create(vals)
        return result

    def action_send_mail(self):
        template_id = self.env.ref('product_proposal.email_template_product_proposal').id
        print("template/....................", template_id)
        template = self.env['mail.template'].browse(template_id)
        print("template....................", template)
        template.send_mail(self.id, force_send=True)

        return self.write({'state': 'sent'})




    @api.depends('proposal_line_ids.sub_total_proposed')
    def _compute_proposed_total(self):
        self.proposed_total = 0.0
        if self.proposal_line_ids:
            for line in self.proposal_line_ids:
                print("in line.subtotal.........................",line.sub_total_proposed)
                self.proposed_total += line.sub_total_proposed
        self.total_amt = self.proposed_total
        print("jjjjjjjjjjjjjjjjjjjjjj totsl proposd",self.total_amt)


    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_send(self):
        self.write({'state': 'sent'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def smt_btn_preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    #
    def _get_share_url(self, redirect=False, signup_partner=False, pid=None):
        self.ensure_one()
        return super(ProductProposal, self)._get_share_url(redirect, signup_partner, pid)

    def _compute_access_url(self):
        super(ProductProposal, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/proposals/%s' % (order.id)

    def _get_portal_return_action(self):
        """ Return the action used to display orders when returning from customer portal. """
        self.ensure_one()
        return self.env.ref('product_proposal.action_product_proposal')




#
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
    sub_total_proposed = fields.Monetary(string='SubTotal Proposed', store=True)
    sub_total_accepted = fields.Monetary(string='SubTotal Accepted', store=True)

    #

    @api.onchange('product_id', 'qty_proposed', 'price_proposed')
    def _onchange_product_id(self):
        print("..............................prod name", self.product_id.name)
        self.label = self.product_id.name
        print("........................propsd price")
        self.price_proposed = self.product_id.lst_price
        print("............................subtotl proposed", self.qty_proposed * self.price_proposed)
        self.sub_total_proposed = self.qty_proposed * self.price_proposed
