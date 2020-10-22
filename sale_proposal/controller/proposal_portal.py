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
        print(history, proposal_sudo, 'dooooooooooooooneeeeeeeeeeee')

        return request.render('sale_proposal.sale_proposal_portal_template', values)

    # @http.route(['/my/proposals/<int:proposal_id>/accept'], type='http', auth="public", website=True, methods=['POST'])
    # def proposal_order(self, data, access_token=None):
    #     """ This route for accept proposal order
    #     :param data (list of dict): Has record id and each line ids of one2many field and Accepted Qty and Accepted Price
    #     """
    #     # Fatch record id
    #     record_id = [rec_ids['rec_id'] for rec_ids in data]
    #     try:
    #         proposalorder_sudo = self._document_check_access('sale.proposal', int(record_id[0]),
    #                                                          access_token=access_token)
    #         print('\n\n\n', proposalorder_sudo)
    #     except (AccessError, MissingError):
    #         return request.redirect('/my')
    #
    #     # Update State and Proposal Order Line
    #     if proposalorder_sudo:
    #         vals = {'proposal_status': 'accept', 'proposal_line_ids': [(1, int(records['line_id']),
    #                                                                  {'qty_accepted': int(records['qty_accepted']),
    #                                                                   'price_accepted': float(records['price_accepted'])}) for
    #                                                                 records in data]}
    #         proposalorder_sudo.write(vals)
    #     return True
    # def portal_proposal_accept(self, proposal_id, access_token=None, name=None, **post):
    #     # get from query string if not on json param
    #     try:
    #         proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)
    #     except (AccessError, MissingError):
    #         return request.redirect('/my')
    #
    #     proposal_sudo.write({
    #         'proposal_status': 'accept',
    #     })
    #     request.env.cr.commit()
    #     # print('alhamdulillah',post.get('inputid'))
    #     s=request.httprequest.form.getlist('qty_accept')
    #     print(s)
    #     # message = post.get('accepting_message')
    #     #
    #     # _message_post_helper(
    #     #     'proposals.proposals', proposal_sudo.id, _('Proposal is Accepted.'),
    #     #     **({'token': access_token} if access_token else {}))
    #     #
    #     # query_string = False
    #     # if message:
    #     #     _message_post_helper('proposals.proposals', proposal_id, message,
    #     #                          **{'token': access_token} if access_token else {})
    #     # else:
    #     #     query_string = "&message=cant_accept"
    #
    #     return request.redirect(proposal_sudo.get_portal_url())
    #
    # @http.route(['/my/proposals/<int:proposal_id>/decline'], type='http', auth="public", methods=['POST'], website=True)
    # def decline(self, proposal_id, access_token=None, **post):
    #     try:
    #         proposal_sudo = self._document_check_access('sale.proposal', proposal_id, access_token=access_token)
    #     except (AccessError, MissingError):
    #         return request.redirect('/my')
    #
    #     proposal_sudo.write({
    #         'proposal_status': 'reject',
    #     })
    #     request.env.cr.commit()
    #
    #     # message = post.get('decline_message')
    #     #
    #     # query_string = False
    #     # if message:
    #     #     _message_post_helper('proposals.proposals', proposal_id, message,
    #     #                          **{'token': access_token} if access_token else {})
    #     # else:
    #     #     query_string = "&message=cant_reject"
    #
    #     return request.redirect(proposal_sudo.get_portal_url())

    @http.route('/proposal/accepted/', type='json', access_token=True, auth='user', website=True, csrf=True)
    def proposal_order(self, data, access_token=None):
        """ This route for accept proposal order
        :param data (list of dict): Has record id and each line ids of one2many field and Accepted Qty and Accepted Price
        """
        print('oooooooooookkkkkk')
        # Fatch record id
        # record_id = [rec_ids['rec_id'] for rec_ids in data]
        # try:
        #     proposalorder_sudo = self._document_check_access('sale.proposal', int(record_id[0]),
        #                                                      access_token=access_token)
        #     print('\n\n\n', proposalorder_sudo)
        # except (AccessError, MissingError):
        #     return request.redirect('/my')

        # Update State and Proposal Order Line
        # if proposalorder_sudo:
        #     vals = {'proposal_status': 'accept', 'proposal_line': [(1, int(records['line_id']),
        #                                                              {'qty_acept': int(records['qty_acept']),
        #                                                               'price_acept': float(records['price_acept'])}) for
        #                                                             records in data]}
        #     proposalorder_sudo.write(vals)
        # return True

    @http.route('/proposals/rejected/', type='json', access_token=True, auth='user', website=True, csrf=True)
    def proposal_order_rejected(self, record_id):
        """ This route for Reject proposal order
        :param record_id: Has record id of current model"""
        # Update state
        # proposalorder = request.env['sale.proposal'].sudo().search([('id', '=', record_id)]).write(
        #     {'state': 'proposal_rejected'})
        return True