from datetime import date
from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal,get_records_pager


class CustomerPortal(CustomerPortal):

    @http.route(['/my/proposals/<int:proposal_id>'], type='http', auth="public", website=True)
    def portal_proposal_page(self, proposal_id, report_type=None, access_token=None, message=False, download=False,
                             **kw):
        try:
            proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=proposal_sudo, report_type=report_type,
                                     report_ref='sale_proposal.sale_proposal_report',
                                     download=download)
        if proposal_sudo:
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % proposal_sudo.id)
            if isinstance(session_obj_date, date):
                session_obj_date = session_obj_date.isoformat()
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % proposal_sudo.id] = now
                body = _('Quotation viewed by customer %s') % proposal_sudo.partner_id.name
                _message_post_helper(
                    "sale.order",
                    proposal_sudo.id,
                    body,
                    token=proposal_sudo.access_token,
                    message_type="notification",
                    subtype="mail.mt_note",
                    partner_ids=proposal_sudo.user_id.sudo().partner_id.ids,
                )

        values = {
            'sale_proposal': proposal_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': proposal_sudo.partner_id.id,
            'report_type': 'html',
        }
        if proposal_sudo.company_id:
            values['res_company'] = proposal_sudo.company_id

        history = request.session.get('my_proposals_history', [])
        values.update(get_records_pager(history, proposal_sudo))

        return request.render('sale_proposal.sale_proposal_portal_template', values)

    @http.route('/proposal/accepted/', type='json', auth='user', website=True, csrf=True)
    def proposal_accepted(self, data):
        for rec in data:
            proposal_sudo = request.env['sale.proposal'].sudo().search([('id', '=', int(rec['proposal_id']))])
            if proposal_sudo:
                vals = {'proposal_status': 'accept','proposal_line_ids': [(1, int(records['line_id']),
                                               {'qty_accepted': int(records['qty_accepted']),
                                                'price_accepted': float(records['price_accepted']),
                                                'amt_total_accepted': records['amount_total_accpt']}) for
                                              records in data]}
                proposal_sudo.write(vals)
            return True

    @http.route('/proposal/rejected/', type='json', auth='user', website=True, csrf=True)
    def proposal_rejected(self, proposal_id):
        proposal_sudo = request.env['sale.proposal'].sudo().search([('id', '=', proposal_id)])
        vals={'proposal_status': 'reject'}
        proposal_sudo.write(vals)