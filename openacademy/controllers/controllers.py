# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Openacademy(http.Controller):
    @http.route('/openacademy/', auth='public', website=True, sitemap=False)
    def index(self, **kw):

        return "Hello, world"
    @http.route('/openacademy/sessions/', auth='public', website=True, sitemap=False)
    def list(self, **kw):
        return http.request.render('openacademy.session_page', {})

    @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('openacademy.object', {
            'object': obj
        })