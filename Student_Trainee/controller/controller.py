from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/students',type="http", website=True)
    def student(self, **kwargs):
        students = request.env['school.student'].sudo().search([])
        print(students)
        return request.render("Student_Trainee.students", {'students': students})
    
    @http.route('/students/detail/<model("school.student"):student>', type='http', auth="public", website=True)
    def student_details(self, student, **kw):
        student_details = request.env['school.student'].search([('id', '=', student)])
        print('\n\n\n\n\n')
        print(student_details)
        print('\n\n\n\n\n')
        return student_details

    @http.route('/students/delete/<model("school.student"):student>', type='http', auth="public", website=True)
    def delete_student(self, student, **kw):
        print('\n\n\n\n\n')
        student.unlink()
        print('\n\n\n\n\n\n\n\n')
        return http.local_redirect("/students")