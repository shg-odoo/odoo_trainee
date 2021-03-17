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

    @http.route('/createmanufacturer', type="http", auth="public", website=True)
    def createmanufacturer(self, **kwargs):
        return request.render('cloth_manufacturer_demo.create_manufacturer')

    @http.route('/delete/<model("manufacturer"):std>', type="http", website=True)
    def delete(self, std, **kwargs):
        std.unlink()
        return request.redirect('/manufacturer')
