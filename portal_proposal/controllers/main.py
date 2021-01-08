from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website.controllers import main


class WebsiteProposal(http.Controller):
	
	@http.route(['/proposal/<int:pro_id>/'], type='http', auth="public", website=True, sitemap=True)
	def proposal(self, pro_id, *args, **kwargs):
		print("ID..........", args, kwargs, self, pro_id)
		proposals = request.env['portal.proposal'].sudo().search([('id','=',pro_id)])
		return http.request.render('portal_proposal.proposal_page_template', {'proposals': proposals})

	@http.route(['/proposal/accept/'], type='http', auth="public", website=True, sitemap=True)
	def save_accept_qty_price(self, *args, **kwargs):
		print("ACCEPT....", args, kwargs, self, request.env.context, request.httprequest.args)
		return http.request.render('portal_proposal.accept_page_template', {})

	# @http.route('/proposal/', auth='public', website=True)
	# def get_vals(self, **kw):
	# 	query_string = request.httprequest.query_string
	# 	print("STRING...", query_string)
