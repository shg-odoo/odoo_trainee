# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import main
from odoo.addons.portal.controllers.portal import CustomerPortal


class WebsiteProposal(http.Controller):

    @http.route(['/proposal/<int:pro_id>'], type='http', auth="public", website=True, sitemap=True)
    def proposal(self, pro_id, access_token=None, **kwargs):
        proposal = CustomerPortal._document_check_access(
            self, 'portal.proposal', pro_id, access_token=access_token)
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])        
        print(">>>", access_token)
        if not access_token:
        	access_token = request.httprequest.args.get('access_token')
        print(">>>>>>>>", access_token)

        url = request.env['ir.config_parameter'].sudo().get_param(
            'web.base.url') + '/proposal/%s/access_token=%s' % (pro_id, proposals.access_token)
        url = request.redirect(url)
        print("URL...", url)
        return url

    @http.route(['/proposal/<int:pro_id>/<string:token>'], type='http', auth="public", website=True, sitemap=True)
    def proposal_token(self, pro_id, token, **kwargs):
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        print("Session...",request.session)
        return http.request.render('portal_proposal.proposal_page_template', {
            'proposals': proposals})

    @http.route(['/proposal/<int:pro_id>/accept', '/proposal/<int:pro_id>/accept/<string:token>'], type='json', auth="public", website=True, sitemap=True)
    def proposal_accept(self, pro_id, token, **kwargs):
    	print("JSON Controller...")
