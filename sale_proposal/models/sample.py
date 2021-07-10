from odoo import models, fields, api, exceptions, _


class Proposal(models.Model):
    _name = 'proposals.proposals'
    _description = "Sales Proposal"
    _inherit = ['mail.thread', 'portal.mixin', 'mail.activity.mixin']

    def action_proposal_mail_send(self):
        self.state = "sent"
        template_id = self.env.ref('proposal_week_2.email_template_proposal_mail').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    def action_cancel_proposal(self):
        self.state = "cancel"

    def action_confirmed_proposal(self):
        self.state = "confirmed"
        sale_order_line_ids = []
        sale_order_tuple_line_ids = ()
        for rec in self:
            for line in rec.proposal_line_ids:
                sale_order_list_line_ids = [0, 0]
                sale_order_list_line_ids.append(({'product_id': line.product_id.id, 'name': line.description,
                                                  'product_uom_qty': line.qty_accepted,
                                                  'price_unit': line.price_accepted}))
                sale_order_tuple_line_ids = tuple(sale_order_list_line_ids)
                sale_order_line_ids.append(sale_order_tuple_line_ids)
        self.env['sale.order'].create(
            {'partner_id': self.customer_id.id, 'order_line': sale_order_line_ids, 'state': 'sale'})

    @api.model
    def create(self, vals):
        if vals.get('proposal_name', _('New')) == _('New'):
            seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.now())
            vals['proposal_name'] = self.env['ir.sequence'].next_by_code('proposals.proposals',
                                                                         sequence_date=seq_date) or _('New')
        result = super(Proposal, self).create(vals)
        return result

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

    def preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    def _get_share_url(self, redirect=False, signup_partner=False, pid=None):
        self.ensure_one()
        return super(Proposal, self)._get_share_url(redirect, signup_partner, pid)

    def _compute_access_url(self):
        super(Proposal, self)._compute_access_url()
        for proposal in self:
            proposal.access_url = '/my/proposals/%s' % (proposal.id)

    def _get_portal_return_action(self):
        """ Return the action used to display orders when returning from customer portal. """
        self.ensure_one()
        return self.env.ref('proposal_week_2.action_proposal')

    def _get_report_base_filename(self):
        self.ensure_one()
        return '%s' % (self.proposal_name)

    proposal_name = fields.Char(default=lambda self: _('New'), readonly=True)
    sales_man_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    customer_id = fields.Many2one("res.partner", required=True)
    price_list_id = fields.Many2one("product.pricelist", required=True)
    proposal_line_ids = fields.One2many("proposals.line", 'proposal_id')
    state = fields.Selection([('draft', 'Draft'),
                              ('sent', 'Sent'),
                              ('confirmed', 'Confirmed'),
                              ('cancel', 'Cancel')], default="draft")
    proposed_total_price = fields.Float(compute='_compute_proposed_total', default=0.0, store=True, readonly=True)
    accepted_total_price = fields.Float(compute='_compute_accepted_total', default=0.0, store=True, readonly=True)
    proposal_date = fields.Datetime(default=fields.Datetime.now)
    fiscal_position_id = fields.Many2one(
        'account.fiscal.position', string='Fiscal Position')
    partner_shipping_id = fields.Many2one(
        'res.partner')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)
    proposal_status = fields.Selection([('accept', 'Accepted'),
                                        ('reject', 'Rejected'),
                                        ('no_response', 'No Response')], default="no_response")


class ProposalLine(models.Model):
    _name = 'proposals.line'

    @api.onchange('product_id')
    def product_id_change(self):
        if not self.product_id:
            return
        valid_values = self.product_id.product_tmpl_id.valid_product_template_attribute_line_ids.product_template_value_ids
        # remove the is_custom values that don't belong to this template
        for pacv in self.product_custom_attribute_value_ids:
            if pacv.custom_product_template_attribute_value_id not in valid_values:
                self.product_custom_attribute_value_ids -= pacv

        # remove the no_variant attributes that don't belong to this template
        for ptav in self.product_no_variant_attribute_value_ids:
            if ptav._origin not in valid_values:
                self.product_no_variant_attribute_value_ids -= ptav

        vals = {}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['qty_proposed'] = self.qty_proposed or 1.0

        product = self.product_id.with_context(
            partner=self.proposal_id.customer_id,
            quantity=vals.get('qty_proposed') or self.qty_proposed,
            date=self.proposal_id.proposal_date,
            pricelist=self.proposal_id.price_list_id.id,
            uom=self.product_uom.id
        )

        vals.update(description=self.get_proposal_line_multiline_description_sale(product))

        if self.proposal_id.price_list_id and self.proposal_id.customer_id:
            vals['price_proposed'] = self.env['account.tax']._fix_tax_included_price_company(
                self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)
        self.update(vals)

        title = False
        message = False
        result = {}
        warning = {}
        if product.sale_line_warn != 'no-message':
            title = _("Warning for %s") % product.name
            message = product.sale_line_warn_msg
            warning['title'] = title
            warning['message'] = message
            result = {'warning': warning}
            if product.sale_line_warn == 'block':
                self.product_id = False

        return result

    def get_proposal_line_multiline_description_sale(self, product):
        return product.get_product_multiline_description_sale() + self._get_proposal_line_multiline_description_variants()

    def _get_proposal_line_multiline_description_variants(self):
        if not self.product_custom_attribute_value_ids and not self.product_no_variant_attribute_value_ids:
            return ""

        description = "\n"

        custom_ptavs = self.product_custom_attribute_value_ids.custom_product_template_attribute_value_id
        no_variant_ptavs = self.product_no_variant_attribute_value_ids._origin

        # display the no_variant attributes, except those that are also
        # displayed by a custom (avoid duplicate description)
        for ptav in (no_variant_ptavs - custom_ptavs):
            description += "\n" + ptav.with_context(lang=self.proposal_id.customer_id.lang).display_name

        # display the is_custom values
        for pacv in self.product_custom_attribute_value_ids:
            description += "\n" + pacv.with_context(lang=self.proposal_id.customer_id.lang).display_name

        return description

    @api.onchange('product_uom', 'qty_proposed')
    def product_uom_change(self):
        if self.proposal_id.price_list_id and self.proposal_id.customer_id:
            product = self.product_id.with_context(
                lang=self.proposal_id.customer_id.lang,
                partner=self.proposal_id.customer_id,
                quantity=self.qty_proposed,
                date=self.proposal_id.proposal_date,
                pricelist=self.proposal_id.price_list_id.id,
                uom=self.product_uom.id,
                fiscal_position=self.env.context.get('fiscal_position')
            )
            self.price_proposed = self.env['account.tax']._fix_tax_included_price_company(
                self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)

    def _get_display_price(self, product):
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

        if self.proposal_id.price_list_id.discount_policy == 'with_discount':
            return product.with_context(pricelist=self.proposal_id.price_list_id.id).price
        product_context = dict(self.env.context, partner_id=self.proposal_id.customer_id.id,
                               date=self.proposal_id.proposal_date, uom=self.product_uom.id)

        final_price, rule_id = self.proposal_id.price_list_id.with_context(product_context).get_product_price_rule(
            product or self.product_id, self.qty_proposed or 1.0, self.proposal_id.customer_id)
        base_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id,
                                                                                           self.qty_proposed,
                                                                                           self.product_uom,
                                                                                           self.proposal_id.price_list_id.id)
        if currency != self.proposal_id.price_list_id.currency_id:
            base_price = currency._convert(
                base_price, self.proposal_id.price_list_id.currency_id,
                self.proposal_id.company_id or self.env.company, self.proposal_id.proposal_date or fields.Date.today())
        # negative discounts (= surcharge) are included in the display price
        return max(base_price, final_price)

    def _get_real_price_currency(self, product, rule_id, qty, uom, price_list_id):
        PricelistItem = self.env['product.pricelist.item']
        field_name = 'lst_price'
        currency_id = None
        product_currency = product.currency_id
        if rule_id:
            pricelist_item = PricelistItem.browse(rule_id)
            if pricelist_item.pricelist_id.discount_policy == 'without_discount':
                while pricelist_item.base == 'pricelist' and pricelist_item.base_pricelist_id and pricelist_item.base_pricelist_id.discount_policy == 'without_discount':
                    price, rule_id = pricelist_item.base_pricelist_id.with_context(uom=uom.id).get_product_price_rule(
                        product, qty, self.order_id.partner_id)
                    pricelist_item = PricelistItem.browse(rule_id)

            if pricelist_item.base == 'standard_price':
                field_name = 'standard_price'
                product_currency = product.cost_currency_id
            elif pricelist_item.base == 'pricelist' and pricelist_item.base_pricelist_id:
                field_name = 'price'
                product = product.with_context(pricelist=pricelist_item.base_pricelist_id.id)
                product_currency = pricelist_item.base_pricelist_id.currency_id
            currency_id = pricelist_item.pricelist_id.currency_id

        if not currency_id:
            currency_id = product_currency
            cur_factor = 1.0
        else:
            if currency_id.id == product_currency.id:
                cur_factor = 1.0
            else:
                cur_factor = currency_id._get_conversion_rate(product_currency, currency_id,
                                                              self.company_id or self.env.company,
                                                              self.order_id.date_order or fields.Date.today())

        product_uom = self.env.context.get('uom') or product.uom_id.id
        if uom and uom.id != product_uom:
            # the unit price is in a different uom
            uom_factor = uom._compute_price(1.0, product.uom_id)
        else:
            uom_factor = 1.0

        return product[field_name] * uom_factor * cur_factor, currency_id

    def _get_protected_fields(self):
        return [
            'product_id', 'description', 'price_proposed', 'product_uom', 'qty_proposed',
            'tax_id', 'analytic_tag_ids'
        ]

    @api.onchange('price_proposed', 'qty_proposed')
    def accepted_price_qty_change(self):
        self.qty_accepted = self.qty_proposed
        self.price_accepted = self.price_proposed

    product_id = fields.Many2one("product.product")
    description = fields.Text()
    qty_proposed = fields.Integer(default=1)
    price_proposed = fields.Float("Price Proposes(per unit)", digits='Product Price')
    qty_accepted = fields.Integer(default=1)
    price_accepted = fields.Float("Price Accepted(per unit)")
    proposal_id = fields.Many2one("proposals.proposals")
    proposed_sub_total = fields.Float(default=0.0, readonly=True)
    accepted_sub_total = fields.Float(default=0.0, readonly=True)
    product_custom_attribute_value_ids = fields.One2many('product.attribute.custom.value', 'sale_order_line_id',
                                                         string="Custom Values", copy=True)
    product_no_variant_attribute_value_ids = fields.Many2many('product.template.attribute.value', string="Extra Values",
                                                              ondelete='restrict')
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure',
                                  domain="[('category_id', '=', product_uom_category_id)]")
    company_id = fields.Many2one(related='proposal_id.company_id', string='Company', store=True, readonly=True,
                                 index=True)
    tax_id = fields.Many2many('account.tax', string='Taxes')
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    analytic_line_ids = fields.One2many('account.analytic.line', 'so_line', string="Analytic lines")


# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import binascii
from datetime import date

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression


class CustomerPortal(CustomerPortal):

    @http.route(['/my/proposals/<int:proposal_id>'], type='http', auth="public", website=True)
    def portal_proposal_page(self, proposal_id, report_type=None, access_token=None, message=False, download=False,
                             **kw):
        try:
            proposal_sudo = self._document_check_access('proposals.proposals', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=proposal_sudo, report_type=report_type,
                                     report_ref='proposal_week_2.action_report_proposal', download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if proposal_sudo:
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_proposal%s' % proposal_sudo.id)
            if isinstance(session_obj_date, date):
                session_obj_date = session_obj_date.isoformat()
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_proposal%s' % proposal_sudo.id] = now
                body = _('Proposal viewed by customer %s') % proposal_sudo.customer_id.name
                _message_post_helper(
                    "proposals.proposals",
                    proposal_sudo.id,
                    body,
                    token=proposal_sudo.access_token,
                    message_type="notification",
                    subtype="mail.mt_note",
                    partner_ids=proposal_sudo.sales_man_id.sudo().partner_id.ids,
                )

        values = {
            'proposals_proposals': proposal_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': proposal_sudo.customer_id.id,
            'report_type': 'html',
            'action': proposal_sudo._get_portal_return_action(),
        }
        if proposal_sudo.company_id:
            values['res_company'] = proposal_sudo.company_id

        history = request.session.get('my_proposals_history', [])

        values.update(get_records_pager(history, proposal_sudo))
        return request.render('proposal_week_2.proposal_portal_template', values)

    @http.route(['/my/proposals/<int:proposal_id>/accept'], type='http', auth="public", website=True, methods=['POST'])
    def portal_proposal_accept(self, proposal_id, access_token=None, name=None, **post):
        # get from query string if not on json param
        try:
            proposal_sudo = self._document_check_access('proposals.proposals', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        proposal_sudo.write({
            'proposal_status': 'accept',
        })
        request.env.cr.commit()

        message = post.get('accepting_message')

        _message_post_helper(
            'proposals.proposals', proposal_sudo.id, _('Proposal is Accepted.'),
            **({'token': access_token} if access_token else {}))

        query_string = False
        if message:
            _message_post_helper('proposals.proposals', proposal_id, message,
                                 **{'token': access_token} if access_token else {})
        else:
            query_string = "&message=cant_accept"

        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))

    @http.route(['/my/proposals/<int:proposal_id>/decline'], type='http', auth="public", methods=['POST'], website=True)
    def decline(self, proposal_id, access_token=None, **post):
        try:
            proposal_sudo = self._document_check_access('proposals.proposals', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        proposal_sudo.write({
            'proposal_status': 'reject',
        })
        request.env.cr.commit()

        message = post.get('decline_message')

        query_string = False
        if message:
            _message_post_helper('proposals.proposals', proposal_id, message,
                                 **{'token': access_token} if access_token else {})
        else:
            query_string = "&message=cant_reject"

        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))
