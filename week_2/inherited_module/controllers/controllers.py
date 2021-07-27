# -*- coding: utf-8 -*-
# from odoo import http


# class InheritedModule(http.Controller):
#     @http.route('/inherited_module/inherited_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherited_module/inherited_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherited_module.listing', {
#             'root': '/inherited_module/inherited_module',
#             'objects': http.request.env['inherited_module.inherited_module'].search([]),
#         })

#     @http.route('/inherited_module/inherited_module/objects/<model("inherited_module.inherited_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherited_module.object', {
#             'object': obj
#         })
