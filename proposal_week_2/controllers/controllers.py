# -*- coding: utf-8 -*-
# from odoo import http


# class ProposalWeek2(http.Controller):
#     @http.route('/proposal_week_2/proposal_week_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proposal_week_2/proposal_week_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proposal_week_2.listing', {
#             'root': '/proposal_week_2/proposal_week_2',
#             'objects': http.request.env['proposal_week_2.proposal_week_2'].search([]),
#         })

#     @http.route('/proposal_week_2/proposal_week_2/objects/<model("proposal_week_2.proposal_week_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proposal_week_2.object', {
#             'object': obj
#         })
