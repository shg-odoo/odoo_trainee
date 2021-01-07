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

    @http.route('/student/delete', website=True, auth='user', type="http", csrf=False)
    def delete_student_details(self,**post):
        current_name = post.get('id')
        print(current_name)
        print("\n\n\n\n")
        request.env['school.student'].search([('id', '=', current_name)]).unlink()
        return http.local_redirect("/school/student")


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
        id_no = kw.get('id')
        request.env['school.student'].search([('id', '=', id_no)])
        return http.local_redirect("/school/student")



    # @http.route('/student/update', type="http", auth="public", website=True)
    # def create_student(self, **kw):
    #     id_no = kw.get('id')
    #     request.env['school.student'].search([('id', '=', id_no)]).write({
    #         'name':id_no,
    #         })
    #     return http.request.render('school.create_student',{})


    # @http.route('/student/edit', website=True, auth='user', type="http", csrf=False)
    # def edit_student_details(self,**kw):
    #     ca = post.get('id')
    #     print(ca)
    #     request.env['school.student'].search([('id', '=', ca)])
    #     return http.local_redirect("/add_student")
        
    # @http.route('/update_details', website=True, auth='user')
    # def edit_details(self,**kw):
    #     request.env['school.student'].sudo()
    #     

