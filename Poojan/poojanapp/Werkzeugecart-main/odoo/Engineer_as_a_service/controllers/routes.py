from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/mypath', type="http")
    def mypath(self, **kwargs):
        students = request.env['user.list'].search([])
        return request.render('Engineer_as_a_service.my_template', {'students': students})

    @http.route('/create_student', type="http")
    def create_student(self, **kwargs):
        return request.render('Engineer_as_a_service.create_student')

    @http.route('/submit_form', type="http", method="POST")
    def submit_form(self, **kwargs):
        request.env['user.list'].create(kwargs)
        return http.local_redirect('/mypath')

    @http.route('/delete/<model("user.list"):std>', type="http")
    def delete(self, std=None, **kwargs):
        print(std)
        # import pdb; pdb.set_trace()
        std.unlink()
        return http.local_redirect('/mypath')