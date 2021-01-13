from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website.controllers import main


class WebsiteProposal(http.Controller):
	
	@http.route(['/proposal/<int:pro_id>/'], type='http', auth="public", website=True, sitemap=True)
	def proposal(self, pro_id, **kwargs):
		proposals = request.env['portal.proposal'].sudo().search([('id','=',pro_id)])
		return http.request.render('portal_proposal.proposal_page_template', {'proposals': proposals})

	@http.route(['/proposal/accept'], type='http', auth="public", website=True, sitemap=True)
	def save_accept_qty_price(self, **kwargs):
		return http.request.render('portal_proposal.accept_page_template', {'accepted': True})
		