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


    @http.route(['/my/proposal_orders/<int:proposal_order_id>'], type='http', auth="public", website=True)
    def proposal_portal_order_page(self, proposal_order_id, report_type=None, access_token=None, message=False, download=False,
                                   **kw):
        try:
            proposal_order_sudo = self._document_check_access('product.proposal', proposal_order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        # if report_type in ('html', 'pdf', 'text'):
        #     return self._show_report(model=order_sudo, report_type=report_type,
        #                              report_ref='sale.action_report_saleorder',
        #                              download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if proposal_order_sudo:
            # store the date as a string in the session to allow serialization
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % proposal_order_sudo.id)
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % proposal_order_sudo.id] = now
                body = _('Proposal viewed by customer %s', proposal_order_sudo.parner_id.name)
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
        if proposal_order_sudo.company_id:
            values['res_company'] = proposal_order_sudo.company_id

        if proposal_order_sudo.state in ('draft', 'sent', 'cancel'):
            history = request.session.get('my_quotations_history', [])
        else:
            history = request.session.get('my_orders_history', [])
        values.update(get_records_pager(history, proposal_order_sudo))

        return request.render('product_proposal.product_proposal_portal_template', values)

