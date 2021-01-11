from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website.controllers import main


class WebsiteProposal(http.Controller):
	
	@http.route(['/proposal/<int:pro_id>/'], type='http', auth="public", website=True, sitemap=True)
	def proposal(self, pro_id, **kwargs):
		print("ID..........")
		proposals = request.env['portal.proposal'].sudo().search([('id','=',pro_id)])
		return http.request.render('portal_proposal.proposal_page_template', {'proposals': proposals})

	@http.route(['/proposal/accept'], type='json', auth="user", website=True, sitemap=True)
	def save_accept_qty_price(self, **kwargs):
		print("ACCEPT....")
		# return http.request.render('portal_proposal.accept_page_template', {})
		return {'html': request.env.ref('portal_proposal.accept_page_template',raise_if_not_found=True)}
		# return request.env.ref('portal_proposal.accept_page_template').sudo()
		# return {'html': request.env['ir.qweb']._render('portal_proposal.accept_page_template', {})}