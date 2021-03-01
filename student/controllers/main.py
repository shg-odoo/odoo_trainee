from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/student',type="http", website=True, auth='public')
    def student(self, **kw):
        # return "hello Odoo"
        students = request.env['student'].sudo().search([])
        print(students)
        return request.render("student.students", {'students': students})



    @http.route('/student/hobbies',type="http", website=True, auth='public')
    def studentHobbies(self, **kw):
        # return "hello Odoo"
        hobbies = request.env['student.hobby'].sudo().search([])
        print(hobbies)
        return request.render("student.students_hobbies", {'hobbies': hobbies})

    @http.route('/student/detail/<model("student"):student>',type='http',auth="public",website=True)
    def student_details(self,student,**kw):
        student_detail = request.env['student'].browse(student.id)
        values = {
            'students':student_detail,
        }
        return request.render("student.student_detail",values)


    @http.route('/create_student',type="http",website=True,auth='public')
    def create_stu(self,**kw):
        student_detail =request.env['student'].browse()
        values = {
            'students':student_detail
        }
        return request.render("student.new_student",values)



    @http.route('/students/delete/<model("student"):std>', type='http', auth="public", website=True)
    def delete_student(self, std, **kw):
        
        std.unlink()
        return http.local_redirect("/student")


    @http.route('/submit',type="http",website=True,auth='public')
    def submit_data(self,**kw):
        request.env['student'].create(kw)
        return http.local_redirect("/student")
        
 