# -*- coding: utf-8 -*-
from datetime import date
from odoo import fields, http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression

class CustomerProposal(CustomerPortal):
    
    @http.route(['/my/proposal/<int:proposal_id>'], type='http', auth="user", website=True,csrf=True)
    def portal_order_page(self,proposal_id, report_type=None, access_token=True, message=False, download=False, **kw):
        """ This route for send the proposal order 
        :param proposal_id : Has record id of current model"""
        try:
            order_sudo = self._document_check_access('proposal.order', proposal_id, access_token=access_token)
            print('\n\n',order_sudo,'\n\n')
        except (AccessError, MissingError):
            return request.redirect('/my')

        if report_type in ('html', 'pdf', 'text'):
            return self._show_report(model=order_sudo, report_type=report_type, report_ref='sale.action_report_saleorder', download=download)

        if order_sudo:
            now = fields.Date.today().isoformat()
            session_obj_date = request.session.get('view_quote_%s' % order_sudo.id)
            if isinstance(session_obj_date, date):
                session_obj_date = session_obj_date.isoformat()
            if session_obj_date != now and request.env.user.share and access_token:
                request.session['view_quote_%s' % order_sudo.id] = now
                body = _('Proposal viewed by customer')
                _message_post_helper(res_model='proposal.order', res_id=order_sudo.id, message=body, token=order_sudo.access_token, message_type='notification', subtype="mail.mt_note", partner_ids=order_sudo.user_id.sudo().partner_id.ids)

        values = {
            'proposal_order': order_sudo,
            'message': message,
            'token': access_token,
            'return_url': '/shop/payment/validate',
            'bootstrap_formatting': True,
            'partner_id': order_sudo.partner_id.id,
            'report_type': 'html',
        }
        if order_sudo.company_id:
            values['res_company'] = order_sudo.company_id

        return request.render('praposal_app.proposal_order_portal_template', values)                            
        

    @http.route('/proposal/accepted/', type='json',access_token=True, auth='user',website=True,csrf=True)
    def proposal_order(self,data,access_token=None):
        """ This route for accept proposal order 
        :param data (list of dict): Has record id and each line ids of one2many field and Accepted Qty and Accepted Price
        """
        #Fatch record id
        record_id = [rec_ids['rec_id'] for rec_ids in data]
        try:
            proposalorder_sudo = self._document_check_access('proposal.order',int(record_id[0]), access_token=access_token)
            print('\n\n\n',proposalorder_sudo)
        except (AccessError, MissingError):
            return request.redirect('/my')
                
        #Update State and Proposal Order Line
        if proposalorder_sudo :
            vals = {'state': 'proposal_accepted','proposal_line':[(1,int(records['line_id']) ,{'qty_acept':int(records['qty_acept']) ,'price_acept':float(records['price_acept']) })for records in data]}
            proposalorder_sudo.write(vals)
        return True

    
    @http.route('/proposal/rejected/', type='json',access_token=True, auth='user',website=True,csrf=True)
    def proposal_order_rejected(self,record_id):
        """ This route for Reject proposal order 
        :param record_id: Has record id of current model"""
        # Update state
        proposalorder = request.env['proposal.order'].sudo().search([('id','=',record_id)]).write({'state': 'proposal_rejected'})
        return True


