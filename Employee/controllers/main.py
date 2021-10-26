from odoo import http
from odoo.http import request

class Employee(http.Controller):

    @http.route('/index/',type="http",website =True)
    def employee(self,**kw):
        # return "hello Odoo"
        Employee = http.request.env['employee']
        print(Employee)
        return request.render('Employee.index',{'employees':Employee.search([]) 
            })

    @http.route('/delete/<model("employee"):employee>', type='http', auth="public", website=True)
    def delete_employee(self,employee,**kw):
        employee.unlink()
        return http.local_redirect('/index')

    @http.route('/create_employee/',type='http',website=True)
    def create_employee(self,**kw):
        return request.render('Employee.create_employee')

    @http.route("/add_employee", type='http', auth="public", website=True)
    def submit_form(self,**kwargs):
        request.env['employee'].create(kwargs)
        return http.local_redirect("/index")