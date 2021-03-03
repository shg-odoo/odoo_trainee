from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/student',type="http", website=True)
    def student(self, **kw):
        students = request.env['student'].sudo().search([])
        print(students)
        return request.render("Student_Management.students", {'students': students})

    
    @http.route('/create_student', type='http', auth="public", website=True)
    def create_student(self, **kw):
        return request.render("Student_Management.create_student")

    
    @http.route("/submit_data", type='http', auth="public", website=True)
    def submit_form(self,**kwargs):
        request.env['student'].create(kwargs)
        return http.local_redirect("/student")


    @http.route('/student/delete/<model("student"):student>', type='http', auth="public", website=True)
    def delete_student(self, student, **kw):
        student.unlink()
        return http.local_redirect("/student")

    # @http.route('/student/details/<model("student"):student>', type='http', auth="public", website=True)
    # def student_detail(self, student, **kw):
    #     student_details = request.env['student'].search([])
    #     return request.render("Student_Management.student_details", {'students': student_details})





    

    


    

    

    

