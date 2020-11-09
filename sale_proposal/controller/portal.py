from odoo import api, fields, models, SUPERUSER_ID, _
from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.addons.portal.controllers.mail import _message_post_helper

import ast


class CustomerProposalPortal(CustomerPortal):
    @http.route(['/my/proposal/<int:proposal_id>'], type='http', auth="public", website=True)
    def portal_proposal_page(self, proposal_id, report_type=None, access_token=None, message=False, download=False, **kw):
        try:
            proposal_sudo = self._document_check_access(
                'proposal.order', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=proposal_sudo, report_type=report_type, report_ref='sale_proposal.action_report_proposal_order', download=download)

        # use sudo to allow accessing/viewing orders for public user
        # only if he knows the private token
        # Log only once a day
        if proposal_sudo:
            # store the date as a string in the session to allow serialization
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get(
                'view_quote_%s' % proposal_sudo.id)
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % proposal_sudo.id] = now
                body = _('Proposal viewed by customer %s',
                         proposal_sudo.partner_id.name)
                _message_post_helper(
                    "proposal.order",
                    proposal_sudo.id,
                    body,
                    token=proposal_sudo.access_token,
                    message_type="notification",
                    subtype_xmlid="mail.mt_note",
                    partner_ids=proposal_sudo.user_id.sudo().partner_id.ids,
                )

        values = {
            'proposal_order': proposal_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': proposal_sudo.partner_id.id,
            'report_type': 'html',
            'action': proposal_sudo._get_portal_return_action(),
        }
        if proposal_sudo.company_id:
            values['res_company'] = proposal_sudo.company_id

        return request.render('sale_proposal.sale_proposal_portal_template', values)

    @http.route(['/my/proposal/<int:proposal_id>/accept'], type='http', auth="public", website=True)
    def portal_proposal_accept(self, proposal_id=None, access_token=None, name=None, signature=None, customer_accetped_vals=None):
        access_token = access_token or request.httprequest.args.get(
            'access_token')
        try:
            proposal_sudo = self._document_check_access(
                'proposal.order', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return {'error': _('Invalid order.')}
        body = _('Proposal Accepted by customer %s',
                 proposal_sudo.partner_id.name)
        _message_post_helper(
            "proposal.order",
            proposal_sudo.id,
            body,
            token=proposal_sudo.access_token,
            message_type="notification",
            subtype_xmlid="mail.mt_note",
            partner_ids=proposal_sudo.user_id.sudo().partner_id.ids,
        )
        # if customer update values then we are updating to backend
        if customer_accetped_vals:
            customer_accetped_vals = list(
                ast.literal_eval(customer_accetped_vals))
            for line in customer_accetped_vals:
                proposal_line = request.env['proposal.order.line'].browse(
                    int(line['line_id']))
                proposal_line.sudo().write({
                    'qty_accepted': float(line['qty_accepted']),
                    'price_accepted': float(line['price_accepted'])
                })
        proposal_sudo.write({
            'has_cutomer_accepted_proposal': True
        })
        query_string = False
        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))

    @http.route(['/my/proposal/<int:proposal_id>/refuse'], type='http', auth="public", website=True)
    def portal_proposal_refuse(self, proposal_id=None, access_token=None, name=None, signature=None):
        try:
            proposal_sudo = self._document_check_access(
                'proposal.order', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')
        body = _('Proposal Rejected by customer %s',
                 proposal_sudo.partner_id.name)
        _message_post_helper(
            "proposal.order",
            proposal_sudo.id,
            body,
            token=proposal_sudo.access_token,
            message_type="notification",
            subtype_xmlid="mail.mt_note",
            partner_ids=proposal_sudo.user_id.sudo().partner_id.ids,
        )
        # Updating state of proposal to cancel
        proposal_sudo.write({
            'state': 'cancel',
            'has_cutomer_rejected_proposal': True
        })
        query_string = False
        return request.redirect(proposal_sudo.get_portal_url(query_string=query_string))
