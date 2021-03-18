# -*- coding: utf-8 -*-
# from odoo import http


# class SaleTestApp(http.Controller):
#     @http.route('/sale_test_app/sale_test_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_test_app/sale_test_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_test_app.listing', {
#             'root': '/sale_test_app/sale_test_app',
#             'objects': http.request.env['sale_test_app.sale_test_app'].search([]),
#         })

#     @http.route('/sale_test_app/sale_test_app/objects/<model("sale_test_app.sale_test_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_test_app.object', {
#             'object': obj
#         })
