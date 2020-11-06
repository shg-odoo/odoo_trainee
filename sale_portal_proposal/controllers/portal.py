# -*- coding: utf-8 -*-
import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression
from functools import partial
from odoo.tools import formatLang

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

    def _get_portal_proposal_details(self, order_sudo, order_line=False):
        currency = order_sudo.currency_id
        format_price = partial(formatLang, request.env, digits=currency.decimal_places)
        results = {
            'order_amount_total': format_price(order_sudo.amount_total_accepted),
            'order_amount_untaxed': format_price(order_sudo.amount_untaxed_accepted),
            'order_amount_tax': format_price(order_sudo.amount_tax_accepted),
        }
        return results

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

    @http.route(['/my/proposals/<int:proposal_id>'], type='http', auth="public", website=True)
    def portal_proposal_page(self, proposal_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            order_sudo = self._document_check_access('sale.portal.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type,
                                     report_ref='sale.action_report_saleorder', download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if order_sudo:
            # store the date as a string in the session to allow serialization
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_proposal_%s' % order_sudo.id)
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_proposal_%s' % order_sudo.id] = now
                body = _('Proposal viewed by customer %s', order_sudo.partner_id.name)
                _message_post_helper(
                    "sale.portal.proposal",
                    order_sudo.id,
                    body,
                    token=order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=order_sudo.user_id.sudo().partner_id.ids,
                )

        values = {
            'sale_proposal': order_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': order_sudo.partner_id.id,
            'report_type': 'html',
            'action': order_sudo._get_portal_return_action(),
        }
        if order_sudo.company_id:
            values['res_company'] = order_sudo.company_id

        history = request.session.get('my_proposal_history', [])
        values.update(get_records_pager(history, order_sudo))

        return request.render('sale_portal_proposal.sale_portal_proposal_template', values)

    @http.route(['/my/proposals/<int:proposal_id>/update_proposals_line_dict'], type='json', auth="public", website=True)
    def update_proposals_line_dict(self, line_id, remove=False, proposal_id=None, access_token=None,price=False,**kwargs):
        try:
            order_sudo = self._document_check_access('sale.portal.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if order_sudo.state not in ('draft', 'sent'):
            return False
        order_line = request.env['sale.portal.proposal.line'].sudo().browse(int(line_id))
        if order_line.proposal_id != order_sudo:
            return False
        if price:
            order_line.write({'price_unit_accepted': price})
        else:
            number = -1 if remove else 1
            quantity = order_line.product_uom_qty_accepted + number

            order_line.write({'product_uom_qty_accepted': quantity})
        results = self._get_portal_proposal_details(order_sudo, order_line)

        return results

    @http.route(['/my/proposals/<int:proposal_id>/accept_proposal'], type='json', auth="public",website=True)
    def accept_proposal(self,proposal_id=None, access_token=None,accept=False,reject=False,**kwargs):
        try:
            order_sudo = self._document_check_access('sale.portal.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if order_sudo.state not in ('draft', 'sent'):
            return False
        proposal_status = 'approved' if accept else 'rejected'
        order_sudo.write({'proposal_status': proposal_status})
        _message_post_helper(
            'sale.portal.proposal', order_sudo.id, _('Proposal Accepted'),
            **({'token': access_token} if access_token else {}))

        query_string = '&message=accepted_ok'
        return request.redirect(order_sudo.get_portal_url(query_string=query_string))

