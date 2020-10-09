# -*- coding: utf-8 -*-
from odoo import http


class Openacademy(http.Controller):
    @http.route('/openacademy/openacademy/', auth='public')
    def index(self, **kw):
        return "Hello, world"

