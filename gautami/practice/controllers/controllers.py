from odoo import http
from odoo.http import request

class Basic(http.Controller):
    @http.route('/practice/', auth='public')
    def index(self, **kw):
        return "Hello, this is Gautami"

class Basic2(http.Controller):

    @http.route('/teacher/', auth='public')
    def index(self, **kw):
        return http.request.render('practice.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

class Colleges(http.Controller):
    @http.route('/colleges/', auth='public')
    def index(self, **kw):
        college = request.env['college.details'].sudo().search([])
        return http.request.render('practice.college', {
            'college': college,
        })
