# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import main
from odoo.addons.portal.controllers.portal import CustomerPortal


class WebsiteProposal(http.Controller):

    @http.route(['/proposal/<int:pro_id>'], type='http', auth="public", website=True, sitemap=True)
    def proposal(self, pro_id, access_token=None, **kwargs):
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        url = request.env['ir.config_parameter'].sudo().get_param(
            'web.base.url') + '/proposal/%s/access_token=%s' % (pro_id, proposals.access_token)
        return request.redirect(url)

    @http.route(['/proposal/<int:pro_id>/<string:token>'], type='http', auth="public", website=True, sitemap=True)
    def proposal_token(self, pro_id, token, **kwargs):
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        return http.request.render('portal_proposal.proposal_page_template', {
            'proposals': proposals})

    @http.route(['/proposal/accept'], type='json', auth="public", website=True, sitemap=True)
    def proposal_accept(self, qty_list, price_list, pro_id, token, **kwargs):
        proposal = CustomerPortal._document_check_access(
            self, 'portal.proposal', pro_id, access_token=token)
        proposal.accept_qty_price(qty_list, price_list, pro_id, token)

    @http.route(['/proposal/reject'], type='json', auth='public', website=True, sitemap=True)
    def proposal_reject(self, pro_id, token, **kwargs):
        proposal = CustomerPortal._document_check_access(
            self, 'portal.proposal', pro_id, access_token=token)
        proposal.refuse(pro_id)
