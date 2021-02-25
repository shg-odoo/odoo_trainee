from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/student',type="http", website=True)
    def student(self, **kw):
        # return "hello Odoo"
        students = request.env['student'].sudo().search([])
        print(students)
        return request.render("odoo_trainee.students", {'students': students})



    @http.route('/student/hobbies',type="http", website=True)
    def studentHobbies(self, **kw):
        # return "hello Odoo"
        hobbies = request.env['student.hobby'].sudo().search([])
        print(hobbies)
        return request.render("odoo_trainee.students_hobbies", {'hobbies': hobbies})

    
    @http.route('/students/show/<model("student"):student>',type="http",auth="public", website=True)
    def studentData(self,student, **kw):
        student_data = request.env['student'].sudo().browse([student.id])
        print(student_data)
        return request.render("odoo_trainee.student_details", {'student': student_data})


    @http.route('/students/delete/<model("student"):student>', type='http', auth="public", website=True)
    def delete_student(self, student, **kw):
        print('\n\n\n\n\n')
        print(student)
        student.unlink()
        print('\n\n\n\n\n\n\n\n')
        return http.local_redirect("/student")


    @http.route('/create_students', type='http', auth="public", website=True)
    def create_student(self, **kw):
        return request.render("odoo_trainee.create_students")


    @http.route("/submit_data", type='http', auth="public", website=True)
    def submit_form(self,**kwargs):
        request.env['student'].create(kwargs)
        return http.local_redirect("/student")

