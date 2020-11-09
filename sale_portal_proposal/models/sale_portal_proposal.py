# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from functools import partial
from itertools import groupby

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
from odoo.tools.misc import formatLang, get_lang
from werkzeug.urls import url_encode

class SalePortalProposal(models.Model):
    _name = 'sale.portal.proposal'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Sale Portal Proposal'

    @api.depends('line_ids.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.line_ids:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax,
            })

    @api.depends('line_ids.price_total_accepted')
    def _amount_all_accepted(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.line_ids:
                amount_untaxed += line.price_subtotal_accepted
                amount_tax += line.price_tax_accepted
            order.update({
                'amount_untaxed_accepted': amount_untaxed,
                'amount_tax_accepted': amount_tax,
                'amount_total_accepted': amount_untaxed + amount_tax,
            })

    def _amount_by_group(self):
        for order in self:
            currency = order.currency_id or order.company_id.currency_id
            fmt = partial(formatLang, self.with_context(lang=order.partner_id.lang).env, currency_obj=currency)
            res = {}
            for line in order.line_ids:
                price_reduce = line.price_unit
                taxes = line.tax_id.compute_all(price_reduce, quantity=line.product_uom_qty, product=line.product_id,
                                                partner=order.partner_id)['taxes']
                for tax in line.tax_id:
                    group = tax.tax_group_id
                    res.setdefault(group, {'amount': 0.0, 'base': 0.0})
                    for t in taxes:
                        if t['id'] == tax.id or t['id'] in tax.children_tax_ids.ids:
                            res[group]['amount'] += t['amount']
                            res[group]['base'] += t['base']
            res = sorted(res.items(), key=lambda l: l[0].sequence)
            order.amount_by_group = [(
                l[0].name, l[1]['amount'], l[1]['base'],
                fmt(l[1]['amount']), fmt(l[1]['base']),
                len(res),
            ) for l in res]

    def _amount_by_group_accepted(self):
        for order in self:
            currency = order.currency_id or order.company_id.currency_id
            fmt = partial(formatLang, self.with_context(lang=order.partner_id.lang).env, currency_obj=currency)
            res = {}
            for line in order.line_ids:
                price_reduce = line.price_unit_accepted
                taxes = line.tax_id.compute_all(price_reduce, quantity=line.product_uom_qty_accepted, product=line.product_id,
                                                partner=order.partner_id)['taxes']
                for tax in line.tax_id:
                    group = tax.tax_group_id
                    res.setdefault(group, {'amount': 0.0, 'base': 0.0})
                    for t in taxes:
                        if t['id'] == tax.id or t['id'] in tax.children_tax_ids.ids:
                            res[group]['amount'] += t['amount']
                            res[group]['base'] += t['base']
            res = sorted(res.items(), key=lambda l: l[0].sequence)
            order.amount_by_group_accepted = [(
                l[0].name, l[1]['amount'], l[1]['base'],
                fmt(l[1]['amount']), fmt(l[1]['base']),
                len(res),
            ) for l in res]

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    date_order = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now, help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.")
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", )
    pricelist_id = fields.Many2one(
        'product.pricelist', string='Pricelist', check_company=True,
        required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, only newly added lines will be affected.")
    currency_id = fields.Many2one(related='pricelist_id.currency_id', depends=["pricelist_id"], store=True)
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    line_ids = fields.One2many(
        'sale.portal.proposal.line',
        'proposal_id',
        string='Lines',
        required=False,states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)
    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all',
                                     tracking=5)
    amount_tax = fields.Monetary(string='Taxes', store=True, readonly=True, compute='_amount_all')
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', tracking=4)
    amount_by_group = fields.Binary(string="Tax amount by group", compute='_amount_by_group', help="type: [(name, amount, base, formated amount, formated base)]")
    #for accepted values
    amount_untaxed_accepted = fields.Monetary(string='Accepted Untaxed Amount', store=True, readonly=True, compute='_amount_all_accepted',
                                     tracking=5)
    amount_tax_accepted = fields.Monetary(string='Accepted Taxes', store=True, readonly=True, compute='_amount_all_accepted')
    amount_total_accepted = fields.Monetary(string='Accepted Total', store=True, readonly=True, compute='_amount_all_accepted', tracking=4)
    amount_by_group_accepted = fields.Binary(string="Accepted Tax amount by group", compute='_amount_by_group_accepted',
                                    help="type: [(name, amount, base, formated amount, formated base)]")

    proposal_status = fields.Selection(
        string='Proposal Status',
        selection=[('not_reviewed', 'Not Reviewed'),
                   ('approved', 'Approved'),
                   ('rejected', 'Rejected'),
                   ],
        required=False,default='not_reviewed')
    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order',
        required=False)

    @api.model
    def create(self, vals):
        if 'company_id' in vals:
            self = self.with_company(vals['company_id'])
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if 'date_order' in vals:
                seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.portal.proposal', sequence_date=seq_date) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        if any(f not in vals for f in ['pricelist_id']):
            partner = self.env['res.partner'].browse(vals.get('partner_id'))
            vals['pricelist_id'] = vals.setdefault('pricelist_id', partner.property_product_pricelist.id)
        result = super(SalePortalProposal, self).create(vals)
        return result
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        """
        Update the following fields when the partner is changed:
        - Pricelist
        """

        self = self.with_company(self.company_id)
        partner_user = self.partner_id.user_id or self.partner_id.commercial_partner_id.user_id
        values = {
            'pricelist_id': self.partner_id.property_product_pricelist and self.partner_id.property_product_pricelist.id or False,
        }
        user_id = partner_user.id
        if not self.env.context.get('not_self_saleperson'):
            user_id = user_id or self.env.uid
        if user_id and self.user_id.id != user_id:
            values['user_id'] = user_id

        self.update(values)

    def action_send_mail(self):
        if self.filtered(lambda so: so.state != 'draft'):
            raise UserError(_('Only draft orders can be marked as sent directly.'))
        for order in self:
            order.message_subscribe(partner_ids=order.partner_id.ids)
        mail_template = self.env.ref('sale_portal_proposal.email_template_sale_portal_proposal')
        mail_template.send_mail(self.id, force_send=True)
        self.write({'state': 'sent'})

    def action_confirm(self):
        sale_obj = self.env['sale.order']
        sale_lines = []
        # for line in self.line_ids:
        #     line.

        self.write({'state': 'confirmed'})

    def _get_share_url(self, redirect=False, signup_partner=False, pid=None):
        self.ensure_one()
        if self.state not in ['confirmed', 'cancel']:
            auth_param = url_encode(self.partner_id.signup_get_auth_param()[self.partner_id.id])
            return self.get_portal_url(query_string='&%s' % auth_param)
        return super(SalePortalProposal, self)._get_share_url(redirect, signup_partner, pid)

    def _compute_access_url(self):
        super(SalePortalProposal, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/proposals/%s' % (order.id)

    def _get_portal_return_action(self):
        """ Return the action used to display orders when returning from customer portal. """
        self.ensure_one()
        return self.env.ref('sale_portal_proposal.sale_portal_proposal_action')

    def preview_sale_portal_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    def _get_report_base_filename(self):
        self.ensure_one()
        return '%s %s' % ('Proposal', self.name)

class SalePortalProposalLine(models.Model):
    _name = 'sale.portal.proposal.line'
    _description = 'Sale Portal Proposal Line'

    @api.depends('state')
    def _compute_product_uom_readonly(self):
        for line in self:
            line.product_uom_readonly = line.state in ['sale', 'done', 'cancel']

    @api.depends('product_uom_qty', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit
            taxes = line.tax_id.compute_all(price, line.proposal_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.proposal_id.partner_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])

    @api.depends('product_uom_qty_accepted', 'price_unit_accepted', 'tax_id')
    def _compute_amount_accepted(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit_accepted
            taxes = line.tax_id.compute_all(price, line.proposal_id.currency_id, line.product_uom_qty_accepted,
                                            product=line.product_id, partner=line.proposal_id.partner_id)
            line.update({
                'price_tax_accepted': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total_accepted': taxes['total_included'],
                'price_subtotal_accepted': taxes['total_excluded'],
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])

    name = fields.Text(string='Description', required=True)
    product_id = fields.Many2one(
        'product.product', string='Product',
        domain="[('sale_ok', '=', True), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        change_default=True, ondelete='restrict', check_company=True)
    proposal_id = fields.Many2one('sale.portal.proposal', string='Proposal Reference', required=True,
                                  ondelete='cascade', index=True,
                                  copy=False)
    salesman_id = fields.Many2one(related='proposal_id.user_id', store=True, string='Salesperson', readonly=True)
    currency_id = fields.Many2one(related='proposal_id.currency_id', depends=['proposal_id.currency_id'], store=True,
                                  string='Currency', readonly=True)
    company_id = fields.Many2one(related='proposal_id.company_id', string='Company', store=True, readonly=True, index=True)
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)
    product_uom_qty_accepted = fields.Float(string='Quantity Accepted', digits='Product Unit of Measure', required=True, default=1.0)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure',
                                  domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    product_uom_readonly = fields.Boolean(compute='_compute_product_uom_readonly')
    state = fields.Selection(
        related='proposal_id.state', string='Order Status', readonly=True, copy=False, store=True, default='draft')
    tax_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])
    price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)
    price_unit_accepted = fields.Float('Price Accepted', required=True, digits='Product Price', default=0.0)
    price_tax = fields.Float(compute='_compute_amount', string='Total Tax', readonly=True, store=True)
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)
    price_tax_accepted = fields.Float(compute='_compute_amount_accepted', string='Total Tax Accepted', readonly=True, store=True)
    price_subtotal_accepted = fields.Monetary(compute='_compute_amount_accepted', string='Subtotal Accepted', readonly=True, store=True)
    price_total_accepted = fields.Monetary(compute='_compute_amount_accepted', string='Total Accepted', readonly=True, store=True)

    @api.onchange('product_id')
    def product_id_change(self):
        if not self.product_id:
            return
        valid_values = self.product_id.product_tmpl_id.valid_product_template_attribute_line_ids.product_template_value_ids


        vals = {}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['product_uom_qty'] = self.product_uom_qty or 1.0

        product = self.product_id.with_context(
            lang=get_lang(self.env, self.proposal_id.partner_id.lang).code,
            partner=self.proposal_id.partner_id,
            quantity=vals.get('product_uom_qty') or self.product_uom_qty,
            date=self.proposal_id.date_order,
            pricelist=self.proposal_id.pricelist_id.id,
            uom=self.product_uom.id
        )
        vals['name'] = product.name
        if self.proposal_id.pricelist_id and self.proposal_id.partner_id:
            vals['price_unit'] = self.env['account.tax']._fix_tax_included_price_company(
                self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)
        self.update(vals)

        title = False
        message = False
        result = {}
        warning = {}
        if product.sale_line_warn != 'no-message':
            title = _("Warning for %s", product.name)
            message = product.sale_line_warn_msg
            warning['title'] = title
            warning['message'] = message
            result = {'warning': warning}
            if product.sale_line_warn == 'block':
                self.product_id = False

        return result

    def _get_display_price(self, product):
        # TO DO: move me in master/saas-16 on sale.order
        # awa: don't know if it's still the case since we need the "product_no_variant_attribute_value_ids" field now
        # to be able to compute the full price

        # it is possible that a no_variant attribute is still in a variant if
        # the type of the attribute has been changed after creation.

        if self.proposal_id.pricelist_id.discount_policy == 'with_discount':
            return product.with_context(pricelist=self.proposal_id.pricelist_id.id).price
        product_context = dict(self.env.context, partner_id=self.proposal_id.partner_id.id, date=self.proposal_id.date_order,
                               uom=self.product_uom.id)

        final_price, rule_id = self.proposal_id.pricelist_id.with_context(product_context).get_product_price_rule(
            product or self.product_id, self.product_uom_qty or 1.0, self.proposal_id.partner_id)
        base_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id,
                                                                                           self.product_uom_qty,
                                                                                           self.product_uom,
                                                                                           self.proposal_id.pricelist_id.id)
        if currency != self.proposal_id.pricelist_id.currency_id:
            base_price = currency._convert(
                base_price, self.proposal_id.pricelist_id.currency_id,
                self.proposal_id.company_id or self.env.company, self.proposal_id.date_order or fields.Date.today())
        # negative discounts (= surcharge) are included in the display price
        return max(base_price, final_price)









