# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import binascii

from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.payment.controllers.portal import PaymentProcessing
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression

#
# class SamplePortal(CustomerPortal):
#     @http.route('/proposal', auth='public')
#     def handler(self,**kwargs):
#         print("kooi")
#         return "kooi"





class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id
        ProductProposal = request.env['product.proposal']

        if 'order_count' in counters:
            values['order_count'] = ProductProposal.search_count([
                ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
                ('state', 'in', ['sale', 'done'])
            ]) if ProductProposal.check_access_rights('read', raise_exception=False) else 0

        return values

    @http.route(['/my/proposals', '/my/proposals/page/<int:page>'], type='http', auth="user", website=True)
    def product_proposal_portal_my_orders(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        ProductProposal = request.env['product.proposal']

        domain = [
            ('message_partner_ids', 'child_of', [partner.commercial_partner_id.id]),
            ('state', 'in', ['sale', 'done'])
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
        order_count = ProductProposal.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/proposals",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=order_count,
            page=page,
            step=self._items_per_page
        )
        # content according to pager
        orders = ProductProposal.search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_orders_history'] = orders.ids[:100]

        values.update({
            'date': date_begin,
            'orders': orders.sudo(),
            'page_name': 'order',
            'pager': pager,
            'default_url': '/my/proposals',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("product_proposal.product_proposal_portal_my_orders", values)

    @http.route(['/my/proposals/<int:order_id>'], type='http', auth="public", website=True)
    def proposal_portal_order_page(self, order_id, report_type=None, access_token=None, message=False, download=False,
                                   **kw):
        try:
            proposal_order_sudo = self._document_check_access('product.proposal', order_id, access_token=access_token)
            print("proposal_order_sudo.........",proposal_order_sudo)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=proposal_order_sudo, report_type=report_type,
                                     report_ref='product_proposal.report_proposal_order',
                                     download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if proposal_order_sudo:
            # store the date as a string in the session to allow serialization
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % proposal_order_sudo.id)
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % proposal_order_sudo.id] = now
                body = _('Proposal viewed by customer %s', proposal_order_sudo.partner_id.name)
                _message_post_helper(
                    "product.proposal",
                    proposal_order_sudo.id,
                    body,
                    token=proposal_order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=proposal_order_sudo.user_id.sudo().partner_id.ids,
                )

        values = {
            'proposal_order': proposal_order_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': proposal_order_sudo.partner_id.id,
            'report_type': 'html',
            'action': proposal_order_sudo._get_portal_return_action(),
        }
        print("valuess : proposal_order....................",values['proposal_order'])
        print("valuess : token....................",values['token'])
        if proposal_order_sudo.company_id:
            values['res_company'] = proposal_order_sudo.company_id

        if proposal_order_sudo.state in ('draft', 'sent', 'cancel'):
            history = request.session.get('my_quotations_history', [])
        else:
            history = request.session.get('my_orders_history', [])
        values.update(get_records_pager(history, proposal_order_sudo))

        return request.render('product_proposal.product_proposal_portal_template', values)

    @http.route(['/my/proposals/<int:order_id>/accept'], type='json', auth="public", website=True)
    def portal_quote_accept(self, order_id, access_token=None, name=None, signature=None):
        # get from query string if not on json param
        access_token = access_token or request.httprequest.args.get('access_token')
        try:
            proposal_order_sudo = self._document_check_access('product.proposal', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order.')}

        try:
            proposal_order_sudo.write({
                'signed_by': name,
                'signed_on': fields.Datetime.now(),
            })
            request.env.cr.commit()
        except (TypeError, binascii.Error) as e:
            return {'error': _('Invalid signature data.')}

        if proposal_order_sudo.action_confirm():
            proposal_order_sudo.action_send_mail()

        pdf = request.env.ref('product_proposal.report_proposal_order').sudo()._render_qweb_pdf([proposal_order_sudo.id])[0]

        _message_post_helper(
            'product.proposal', proposal_order_sudo.id, _('Order signed by %s') % (name,),
            attachments=[('%s.pdf' % proposal_order_sudo.name, pdf)],
            **({'token': access_token} if access_token else {}))

        query_string = '&message=sign_ok'
        if proposal_order_sudo.has_to_be_paid(True):
            query_string += '#allow_payment=yes'
        return {
            'force_refresh': True,
            'redirect_url': proposal_order_sudo.get_portal_url(query_string=query_string),
        }

    @http.route(['/my/proposals/<int:order_id>/decline'], type='http', auth="public", methods=['POST'], website=True)
    def decline(self, order_id, access_token=None, **post):
        try:
            proposal_order_sudo = self._document_check_access('product.proposal', order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        message = post.get('decline_message')

        query_string = False
        if message:
            proposal_order_sudo.action_cancel()
            _message_post_helper('product.proposal', order_id, message, **{'token': access_token} if access_token else {})
        else:
            query_string = "&message=cant_reject"

        return request.redirect(proposal_order_sudo.get_portal_url(query_string=query_string))