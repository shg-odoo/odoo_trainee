# -*- coding: utf-8 -*-
# from odoo import http


# class DoctorInherit(http.Controller):
#     @http.route('/doctor_inherit/doctor_inherit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/doctor_inherit/doctor_inherit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('doctor_inherit.listing', {
#             'root': '/doctor_inherit/doctor_inherit',
#             'objects': http.request.env['doctor_inherit.doctor_inherit'].search([]),
#         })

#     @http.route('/doctor_inherit/doctor_inherit/objects/<model("doctor_inherit.doctor_inherit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('doctor_inherit.object', {
#             'object': obj
#         })
