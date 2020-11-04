from odoo import api, models, fields, _
from odoo.tools.misc import formatLang, get_lang

from werkzeug.urls import url_encode


class SaleProposal(models.Model):
    _name = "proposal.order"
    _inherit = ['portal.mixin', 'mail.thread',
                'mail.activity.mixin', 'utm.mixin']
    _discription = "Portal proposal"

    name = fields.Char(string='Portal Reference', required=True, copy=False, readonly=True, states={
                       'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    pricelist_id = fields.Many2one(
        'product.pricelist', string='Pricelist', check_company=True,  # Unrequired company
        required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, only newly added lines will be affected.")

    date_order = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
    currency_id = fields.Many2one(related='pricelist_id.currency_id', depends=["pricelist_id"], store=True)
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('confirmed', 'Confirmed'), 
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    proposal_line_ids = fields.One2many('proposal.order.line', 'proposal_id', string='Proposal Lines', states={'cancel': [('readonly', True)], 'confirmed': [('readonly', True)]}, copy=True, auto_join=True)
    amount_total_proposed = fields.Monetary(string='Amount Total Proposed', store=True, readonly=True, compute='_amount_total_proposed', tracking=4)
    amount_total_accepted = fields.Monetary(string='Amount Total Accepted', store=True, readonly=True, compute='_amount_total_accepted', tracking=4)

    def _compute_access_url(self):
        super(SaleProposal, self)._compute_access_url()
        for proposal in self:
            proposal.access_url = '/my/proposal/%s' % (proposal.id)

    @api.depends('proposal_line_ids.proposed_price_subtotal')
    def _amount_total_proposed(self):
        for proposal in self:
            amount_total = 0
            for line in proposal.proposal_line_ids:
                amount_total += line.proposed_price_subtotal
            proposal.update({
                'amount_total_proposed' : amount_total
            })

    @api.depends('proposal_line_ids.accepted_price_subtotal')
    def _amount_total_accepted(self):
        for proposal in self:
            amount_total = 0
            for line in proposal.proposal_line_ids:
                amount_total += line.accepted_price_subtotal   
            proposal.update({
                'amount_total_accepted' : amount_total
            })
    
    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('proposal.order', sequence_date=seq_date) or _('New')

        result = super(SaleProposal, self).create(vals)
        return result

    def send_mail_customer(self):
        self.ensure_one()
        template_id = self.env['ir.model.data'].xmlid_to_res_id('sale_proposal.email_template_sale_proposal', raise_if_not_found=False)
        template = self.env['mail.template'].browse(template_id)
        ctx = {
            'default_model' : 'proposal.order',
            'default_res_id' : self.ids[0],
            'default_use_template' : bool(template_id),
            'default_template_id' : template_id,
            'default_composition_mode' : 'comment',
            'mark_so_as_sent' : True,
            'custom_layout' : 'mail.mail_notification_paynow',
            'force_email' : True,
            'model_description' : 'Proposal Order'
        }
        return {
            'type' : 'ir.actions.act_window',
            'view_mode' : 'form',
            'res_model' : 'mail.compose.message',
            'views' : [(False, 'form')],
            'view_id' : False,
            'target' : 'new',
            'context' : ctx,
        }

    def _get_share_url(self, redirect=False, signup_partner=False, pid=None):
        """Override for proposal order.

        If the proposal is in a state where an action is required from the partner,
        return the URL with a login token. Otherwise, return the URL with a
        generic access token (no login).
        """
        self.ensure_one()
        if self.state not in ['confirmed', 'cancel']:
            auth_param = url_encode(self.partner_id.signup_get_auth_param()[self.partner_id.id])
            return self.get_portal_url(query_string='&%s' % auth_param)
        return super(SaleProposal, self)._get_share_url(redirect, signup_partner, pid)

    def _get_portal_return_action(self):
        """ Return the action used to display proposal when returning from customer portal. """
        self.ensure_one()
        return self.env.ref('sale_proposal.action_proposal_order')

class SaleProposalLine(models.Model):
    _name = "proposal.order.line"

    product_id = fields.Many2one(
        'product.product', string='Product', domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        change_default=True, ondelete='restrict', check_company=True)  # Unrequired company
    product_template_id = fields.Many2one(
        'product.template', string='Product Template',
        related="product_id.product_tmpl_id", domain=[('sale_ok', '=', True)])
    name = fields.Text(string='Description', required=True)
    proposal_id = fields.Many2one('proposal.order', string="Proposal Reference", required=True, ondelete='cascade', index=True, copy=False)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    qty_proposed = fields.Float(string='Qty Proposed')
    qty_accepted = fields.Float(string='Qty Accepted')
    price_proposed = fields.Float('Price Proposed', required=True, digits='Product Price', default=0.0)
    price_accepted = fields.Float('Price Accepted', required=True, digits='Product Price', default=0.0)
    proposed_price_subtotal = fields.Monetary(compute='_compute_proposed_amount', string='Subtotal', readonly=True, store=True)
    accepted_price_subtotal = fields.Monetary(compute='_compute_accepted_amount', string='Subtotal', readonly=True, store=True)
    currency_id = fields.Many2one(related='proposal_id.currency_id', depends=['proposal_id.currency_id'], store=True, string='Currency', readonly=True)
    company_id = fields.Many2one(related='proposal_id.company_id', string='Company', store=True, readonly=True, index=True)
    product_updatable = fields.Boolean(compute='_compute_product_updatable', string='Can Edit Product', readonly=True, default=True)
    state = fields.Selection(
        related='proposal_id.state', string='Proposal Status', readonly=True, copy=False, store=True, default='draft')
    product_no_variant_attribute_value_ids = fields.Many2many('product.template.attribute.value', string="Extra Values", ondelete='restrict')

    @api.depends('product_id', 'proposal_id.state', 'qty_proposed')
    def _compute_product_updatable(self):
        for line in self:
            if line.state ==  'cancel' or (line.state == 'confirmed' and line.qty_proposed > 0):
                line.product_updatable = False
            else:
                line.product_updatable = True

    @api.depends('qty_proposed','price_proposed')
    def _compute_proposed_amount(self):
        for line in self:
            price_subtotal = line.qty_proposed * line.price_proposed
            line.update({
                'proposed_price_subtotal' : price_subtotal
            })
    
    @api.depends('qty_accepted','price_accepted')
    def _compute_accepted_amount(self):
        for line in self:
            price_subtotal = line.qty_accepted * line.price_accepted
            line.update({
                'accepted_price_subtotal' : price_subtotal
            })
            
    @api.onchange("product_id","qty_proposed")
    def product_id_change(self):
        if not self.product_id:
            return
        if self.qty_proposed:
            self.qty_accepted = self.qty_proposed
        vals ={}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['qty_proposed'] = self.qty_proposed or 1.0
            vals['name'] = self.product_id.name_get()[0][1]
        
        product = self.product_id.with_context(
            lang=get_lang(self.env, self.proposal_id.partner_id.lang).code,
            partner=self.proposal_id.partner_id,
            quantity=vals.get('qty_proposed') or self.qty_proposed,
            date=self.proposal_id.date_order,
            pricelist=self.proposal_id.pricelist_id.id,
            uom=self.product_uom.id
        )

        if self.proposal_id.pricelist_id and self.proposal_id.partner_id:
            price = self._get_display_price(product)
            vals['price_proposed'] = price
            vals['price_accepted'] = price
        self.update(vals)
    
    @api.onchange("price_proposed")
    def change_price_proposed(self):
        if self.price_proposed:
            self.price_accepted = self.price_proposed

    def _get_display_price(self, product):
        # TO DO: move me in master/saas-16 on sale.order
        # awa: don't know if it's still the case since we need the "product_no_variant_attribute_value_ids" field now
        # to be able to compute the full price

        # it is possible that a no_variant attribute is still in a variant if
        # the type of the attribute has been changed after creation.
        no_variant_attributes_price_extra = [
            ptav.price_extra for ptav in self.product_no_variant_attribute_value_ids.filtered(
                lambda ptav:
                    ptav.price_extra and
                    ptav not in product.product_template_attribute_value_ids
            )
        ]
        if no_variant_attributes_price_extra:
            product = product.with_context(
                no_variant_attributes_price_extra=tuple(no_variant_attributes_price_extra)
            )

        if self.proposal_id.pricelist_id.discount_policy == 'with_discount':
            return product.with_context(pricelist=self.proposal_id.pricelist_id.id).price
        product_context = dict(self.env.context, partner_id=self.proposal_id.partner_id.id, date=self.proposal_id.date_order, uom=self.product_uom.id)

        final_price, rule_id = self.proposal_id.pricelist_id.with_context(product_context).get_product_price_rule(product or self.product_id, self.qty_proposed or 1.0, self.proposal_id.partner_id)
        base_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id, self.product_uom_qty, self.product_uom, self.order_id.pricelist_id.id)
        if currency != self.proposal_id.pricelist_id.currency_id:
            base_price = currency._convert(
                base_price, self.proposal_id.pricelist_id.currency_id,
                self.proposal_id.company_id or self.env.company, self.proposal_id.date_order or fields.Date.today())
        # negative discounts (= surcharge) are included in the display price
        return max(base_price, final_price)