# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import main
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.mail import _message_post_helper
import uuid


class WebsiteProposal(http.Controller):

    @http.route(['/proposal/<int:pro_id>'], type='http', auth="public", website=True, sitemap=True)
    def proposal(self, pro_id, access_token=None, **kwargs):
        proposal = CustomerPortal._document_check_access(
            self, 'portal.proposal', pro_id, access_token=access_token)
        # message = "Accepted Proposal"
        # _message_post_helper('portal.proposal', pro_id, message, **{'token': access_token} if access_token else {})
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        response = http.request.render('portal_proposal.proposal_page_template', {
                                       'proposals': proposals})
        print("RES...", response)
        print(">>>", access_token)

        # url = request.redirect(proposal.get_portal_url(query_string=False))
        # url = '/proposal/%s/?access_token=%s' % (pro_id,str(uuid.uuid4()))
        url = request.env['ir.config_parameter'].sudo().get_param(
            'web.base.url') + '/proposal/form/%s/access_token=%s' % (pro_id, proposals.access_token)
        url = request.redirect(url)
        print("URL...", url)
        # request.redirect(proposal.get_portal_url(query_string=False))
        return url

    @http.route(['/proposal/form/<int:pro_id>/<string:token>'], type='http', auth="public", website=True, sitemap=True)
    def proposal_token(self, pro_id, token, **kwargs):
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        return http.request.render('portal_proposal.proposal_page_template', {
            'proposals': proposals})
