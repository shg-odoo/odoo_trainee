from odoo import http
from odoo.http import request

class Student(http.Controller):

    @http.route('/school/student/', website=True, auth='user')
    def school_student(self,**kw):
        #return "Hello World"
        students = request.env['school.student'].sudo().search([])
        return request.render("school.students_id", {
                'students': students
            })

    @http.route('/add_student', website=True, auth='user')
    def student_webform(self,**kw):
        return http.request.render('school.create_student',{})

    @http.route('/create/webstudent', website=True, auth='user')
    def create_webstudent(self,**kw):
        request.env['school.student'].sudo().create(kw)
        return request.render("school.student_thanks",{})
    
        
