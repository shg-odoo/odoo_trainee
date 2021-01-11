from odoo import http
from odoo.http import request

class Proposal(http.Controller):
    @http.route(['/my/proposals/<int:proposal_id>/'], type='http', auth="public", website=True)
    def proposal(self, proposal_id, *args, **kwargs):
        print("ID..........", args, kwargs, self, proposal_id)
        proposal = request.env['proposal.proposal'].sudo().search([('id','=',proposal_id)])
        return http.request.render('proposal.proposal_details_page_template', {'proposals': proposal})

    @http.route(['/proposal/accept/'], type='http', auth="public", website=True)
    def accept_qty_price(self, *args, **kwargs):
        return http.request.render('proposal.proposal_accept_page_template', {})

    @http.route(['/proposal/reject/'], type='http', auth="public", website=True)
    def reject_proposal(self, *args, **kwargs):
        return http.request.render('proposal.proposal_reject_page_template', {})

