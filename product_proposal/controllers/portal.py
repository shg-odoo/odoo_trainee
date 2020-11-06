import http

from AptUrl.Helpers import _

from community.addons.portal.controllers.mail import _message_post_helper
from community.addons.portal.controllers.portal import get_records_pager, CustomerPortal
from community.odoo import fields
from community.odoo.exceptions import AccessError, MissingError
from community.odoo.http import request
from community.odoo.osv import expression


class CustomerPortal(CustomerPortal):


    @http.route(['/my/proposal_orders/<int:proposal_order_id>'], type='http', auth="public", website=True)
    def proposal_portal_order_page(self, proposal_order_id, report_type=None, access_token=None, message=False, download=False,
                                   **kw):
        try:
            order_sudo = self._document_check_access('product.proposal', proposal_order_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        # if report_type in ('html', 'pdf', 'text'):
        #     return self._show_report(model=order_sudo, report_type=report_type,
        #                              report_ref='sale.action_report_saleorder',
        #                              download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if order_sudo:
            # store the date as a string in the session to allow serialization
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % order_sudo.id)
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % order_sudo.id] = now
                body = _('Proposal viewed by customer %s', order_sudo.parner_id.name)
                _message_post_helper(
                    "product.proposal",
                    order_sudo.id,
                    body,
                    token=order_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=order_sudo.user_id.sudo().partner_id.ids,
                )

        values = {
            'proposal_order': order_sudo,
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

        if order_sudo.state in ('draft', 'sent', 'cancel'):
            history = request.session.get('my_quotations_history', [])
        else:
            history = request.session.get('my_orders_history', [])
        values.update(get_records_pager(history, order_sudo))

        return request.render('product.proposal.product_proposal_portal_template', values)
