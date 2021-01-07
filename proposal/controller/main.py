from odoo import http
from odoo.http import request

class Proposal(http.Controller):
    @http.route('/my/proposals/<int:proposal_id>', type='http', auth='public', website=True)
    def sale_details(self , **kwargs):
        proposal_details = request.env['proposal.proposal'].sudo().search([])
        return  request.render('proposal.proposal_details_page', {'my_details': proposal_details})