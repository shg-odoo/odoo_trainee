from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/students',type="http", website=True)
    def student(self, **kwargs):
        students = request.env['school.student'].sudo().search([])
        print(students)
        return request.render("Student_Trainee.students", {'students': students})



    # @http.route('/student/hobbies',type="http", website=True)
    # def studentHobbies(self, kw):
    #     # return "hello Odoo"
    #     hobbies = request.env['student.hobby'].sudo().search([])
    #     print(hobbies)
    #     return request.render("odoo_trainee.students_hobbies", {'hobbies': hobbies})