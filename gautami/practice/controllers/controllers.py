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
    @http.route('/show_colleges/', auth='public', type="http", website=True)
    def show_colleges(self, **kw):
        college = request.env['college.details'].sudo().search([])
        return http.request.render('practice.show_colleges', {
            'college': college,
        })

    @http.route('/add_college/', auth='public', type="http", website=True)
    def add_college(self, **kw):
        return http.request.render('practice.create')
    
    @http.route('/save_data/', auth='public', type="http", website=True)
    def save_data(self, **kw):
        print("save data",kw)
        request.env['college.details'].create(kw)
        college = request.env['college.details'].sudo().search([])
        return http.request.render('practice.show_colleges', {
            'college': college,
        })
    
    @http.route('/delete/<model("college.details"):cid>/', auth='public', type="http", website=True)
    def delete(self,cid, **kw):
        cid.unlink()
        college = request.env['college.details'].sudo().search([])
        return http.request.render('practice.show_colleges', {
            'college': college,
        })
    
    @http.route('/update/<model("college.details"):cid>/', auth='public', type="http", website=True)
    def update(self,cid, **kw):
        college1 = request.env['college.details'].search([('id','=',cid.id)])
        return http.request.render('practice.update_college', {
            'college': college1,
        })

    @http.route('/update_data/', auth='public', type="http", website=True)
    def update_data(self, **kw):
        print(kw)
        college1 = request.env['college.details'].search([])
        return http.request.render('practice.show_colleges', {
            'college': college1,
        })
    
