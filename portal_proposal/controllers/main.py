# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.website.controllers import main


class WebsiteProposal(http.Controller):

    @http.route(['/proposal/<int:pro_id>/<string:token>'], type='http', auth="public", website=True, sitemap=True)
    def proposal(self, token, pro_id, **kwargs):
        proposals = request.env['portal.proposal'].sudo().search(
            [('id', '=', pro_id)])
        # return http.request.render('portal_proposal.proposal_page_template', {'proposals': proposals, 'token': token})
        response = http.request.render('portal_proposal.proposal_page_template', {
                                       'proposals': proposals, 'token': token})
        print("Headers...", response.headers)
        response.headers['User-Agent'] = 'Chrome/51.0.2704.103' #'Chrome/56.0.2924.76'
        print("Updated headers...", response.headers)
        return response
