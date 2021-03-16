from odoo import http
from odoo.http import request


class ManufacturerPortal(http.Controller):

    @http.route('/manufacturer', type="http", auth="public", website=True)
    def manufacturer(self, **kwargs):
        manufacturer_det = request.env['manufacturer'].search([])
        return request.render('cloth_manufacturer_demo.manufacturer_details', {'manufacturer_det': manufacturer_det})

    @http.route('/submit_form', type="http", auth="public", website=True)
    def submit_form(self, **kwargs):
        request.env['manufacturer'].create(kwargs)
        return request.redirect('/manufacturer')

