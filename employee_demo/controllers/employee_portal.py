from odoo import http
from odoo.http import request


class EmployeePort(http.Controller):

    @http.route('/employee', type="http", website=True)
    def employee(self, **kwargs):
        employee_det = request.env['employee'].search([])
        return request.render('employee_demo.employee_details', {'employee_det': employee_det})

    @http.route('/submit_form', type="http", auth="public", website=True)
    def submit_form(self, **kwargs):
        request.env['employee'].create(kwargs)
        return request.redirect('/employee')

    @http.route('/delete/<model("employee"):std>', type="http", website=True)
    def delete(self, std, **kwargs):
        std.unlink()
        return request.redirect('/employee')

    @http.route('/create_employee', type="http", website=True)
    def create_employee(self, **kwargs):
        return request.render('employee_demo.create_employee')
