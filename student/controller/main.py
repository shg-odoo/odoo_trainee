from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/mypath',type="http",website=True)
    def mypath(self,**kwargs):
        students = request.env['student'].search([])
        return request.render('student.my_template', {'students': students})

    @http.route('/create_student',*type="http",website=True)
    def create_student(self,*kwargs):
        return request.render('student.create_student')

    @http.route('/submit_form', type="http",website=True)
    def submit_form(self,**kwargs):
        request.env['student'].create(kwargs)
        return request.redirect('/mypath')

    @http.route('/delete/<model("student"):std>', type="http", website=True)
    def delete(self, std, **kwargs):
        std.unlink()
        return request.redirect('/mypath')