from odoo import http
from odoo.http import request
from datetime import datetime

class MyController(http.Controller):

    @http.route('/students',type="http", website=True)
    def student(self, **kw):
        students = request.env['school.student'].sudo().search([])
        print('\n\n\n\n\n')
        print("Students Mapped Function: ",students.mapped('email'))
        print("\n")
        # stud_sorted=students.sorted(lambda o:o.age)
        # stud_sorted_list=[]
        # for i in stud_sorted:
        #     stud_sorted_dict={}
        #     stud_sorted_dict["name"]=i.name
        #     bdate=datetime.strftime(i.birthDate,"%d/%m/%Y")
        #     stud_sorted_dict["birthDate"]=bdate
        #     stud_sorted_dict["age"]=i.age
        #     stud_sorted_list.append(stud_sorted_dict)
        # print("Student Sorted Function: ",stud_sorted_list)
        # print("\n")
        stud_filt=students.filtered(lambda o:o.city=="Mehsana")
        stud_filt_list=[]
        for i in stud_filt:
            stud_filt_dict={}
            stud_filt_dict["name"]=i.name
            stud_filt_dict["city"]=i.city
            stud_filt_list.append(stud_filt_dict)
        print("Student Filtered Function: ",stud_filt_list)
        print('\n\n\n\n\n')
        return request.render("Student_Trainee.students", {'students': students})

    @http.route('/students/create', type='http', auth="public", website=True)
    def create_student(self,**kw):
        return request.render("Student_Trainee.create_student")
    
    @http.route("/submit_student_data", type='http', auth="public", website=True)
    def submit_form(self,**kwargs):
        request.env['school.student'].create(kwargs)
        return http.local_redirect("/students")

    @http.route('/students/detail/<model("school.student"):student>', type='http', auth="public", website=True)
    def student_details(self, student, **kw):
        student_details = request.env['school.student'].browse(student.id)
        print('\n\n\n\n\n')
        print(student.id)
        print('\n\n\n\n\n')
        return request.render("Student_Trainee.student_detail", {'students': student_details})

    @http.route('/students/delete/<model("school.student"):student>', type='http', auth="public", website=True)
    def delete_student(self, student, **kw):
        print('\n\n\n\n\n')
        print(student)
        student.unlink()
        print('\n\n\n\n\n\n\n\n')
        return http.local_redirect("/students")