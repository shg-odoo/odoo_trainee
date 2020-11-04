# -*- coding: utf-8 -*-
import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression

class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id

        SalePortal = request.env['sale.portal.proposal']
        if 'proposal_count' in counters:
            values['proposal_count'] = SalePortal.search_count([
                ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
                ('state', 'in', ['sent','confirmed', 'done'])
            ]) if SalePortal.check_access_rights('read', raise_exception=False) else 0
        return values

    @http.route(['/my/proposals', '/my/proposals/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_proposal(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        SalePortal = request.env['sale.portal.proposal']

        domain = [
            ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
            ('state', 'in', ['confirmed', 'sent'])
        ]

        searchbar_sortings = {
            'date': {'label': _('Order Date'), 'order': 'date_order desc'},
            'name': {'label': _('Reference'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'state'},
        }
        # default sortby order
        if not sortby:
            sortby = 'date'
        sort_order = searchbar_sortings[sortby]['order']

        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # count for pager
        order_count = SalePortal.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/proposals",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=order_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager
        orders = SalePortal.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_proposal_history'] = orders.ids[:100]

        values.update({
            'date': date_begin,
            'orders': orders.sudo(),
            'page_name': 'proposal',
            'pager': pager,
            'default_url': '/my/proposals',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("sale_portal_proposal.portal_my_proposal", values)


