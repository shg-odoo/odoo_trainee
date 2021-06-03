from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/home', type='http', website=True)
    def home(self, **kwargs):
        """
        @return: request to render template id: my_template
        """
        stu = request.env['student'].search([])
        print('+'*20)
        print('stu:', stu)  # stu: student(1, 2, 3, 4, 5, 6, 7, 8, 9)
        return request.render('school.my_template', {'stu': stu})

    @http.route('/create_student', type='http', website=True)
    def create_student(self, **kwargs):
        """
        @return: request to render template id: create_student
        """
        return request.render('school.create_student')

    @http.route('/submit_form', type='http', website=True)
    def submit_form(self, **kwargs):
        request.env['student'].create(kwargs)
        return request.redirect('/home')

    @http.route('/delete_student/<model("student"):std>', type='http', website=True)
    def delete_student(self, std, **kwargs):
        std.unlink()
        return request.redirect('/home')



# to use this controller we need to install website module or we can put
#  it inside depends as ['website']
