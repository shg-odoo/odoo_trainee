# -*- coding: utf-8 -*-
from odoo import http


class Businesscase(http.Controller):
    @http.route('/businesscase/businesscase/', auth='public')
    def index(self, **kw):
#        return "helloo world"

#     @http.route('/businesscase/businesscase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('businesscase.listing', {
#             'root': '/businesscase/businesscase',
#             'objects': http.request.env['businesscase.businesscase'].search([]),
#         })

#     @http.route('/businesscase/businesscase/objects/<model("businesscase.businesscase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('businesscase.object', {
#             'object': obj
#         })
