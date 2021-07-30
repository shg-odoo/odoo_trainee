from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/student_details', type="http", website=True)
    def student_details(self, **kwargs):
        students = request.env['student'].search([])
        return request.render('trainee_demo.my_template', {'students': students})

    @http.route('/create_student', type="http", website=True)
    def create_student(self, **kwargs):
        return request.render('trainee_demo.create_student')

    @http.route('/submit_form', type="http", website=True)
    def submit_form(self, **kwargs):
        request.env['student'].create(kwargs)
        return request.redirect('/student_details')

    @http.route('/delete/<model("student"):std>', type="http", website=True)
    def delete(self, std, **kwargs):
        std.unlink()
        return request.redirect('/student_details')