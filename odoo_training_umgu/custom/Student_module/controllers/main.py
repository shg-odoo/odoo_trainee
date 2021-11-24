from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/home', type="http", website=True)
    def home(self, **kwargs):
        students = request.env['student.details'].sudo().search([])
        return request.render('Student_module.home_page', {'students': students})

    @http.route('/create_student', type="http", website=True)
    def create_student(self, **kwargs):
        return request.render('Student_module.create_student')

    @http.route('/submit_form', type="http", website=True)
    def submit_form(self, **kwargs):
        request.env['student.details'].create(kwargs)
        return request.redirect('/home')

    @http.route('/delete/<model("student.details"):std>', type="http", website=True)
    def delete(self, std, **kwargs):
        std.unlink()
        return request.redirect('/home')