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
        return http.request.render('school.student_thanks',{})


    @http.route('/student/delete/<model("school.student"):student>', type='http', auth="public", website=True)
    def delete_student(self, student, **kw):
        print('\n\n\n\n\n')
        student.unlink()
        print('\n\n\n\n\n\n\n\n')
        return http.local_redirect("/school/student")
   

    # @http.route('/student/delete', website=True, auth='user', type="http", csrf=False)
    # def delete_student_details(self,**post):
    #     current_name = post.get('id')
    #     print(current_name)
    #     print("\n\n\n\n")
    #     request.env['school.student'].search([('id', '=', current_name)]).unlink()
    #     return http.local_redirect("/school/student")


    @http.route('/student/update', type="http", auth="public", website=True)
    def update_student_details(self,**post):
        data = post.get('id')
        print(data)
        ha = request.env['school.student'].search([('id', '=', data)])
        return request.render('school.update_student',
            {"student_data":ha
            })
    
   
    @http.route('/edit/student', website=True, auth='user')
    def edit_student(self,**kw):
        id_no = kw.pop('id')
        student = request.env['school.student'].browse(id_no)
        student.write(kw)
        return http.local_redirect("/school/student")

    # @http.route('/edit/student/<model("school.student"):student>', type='http', auth="public", website=True)
    # def delete_student(self, student, **kw):
    #     print('\n\n\n\n\n')
    #     student.write(kw)
    #     print('\n\n\n\n\n\n\n\n')
    #     return http.local_redirect("/school/student")
   


   