from odoo import http
from odoo.http import request

class Main(http.Controller):

    @http.route('/mypath',type="http",website=True)
    def mypath(self,**kwargs):
        students=request.env["college.student"].search([])
        return request.render("college.student_id",{"students":students})

    @http.route("/create",type="http",website=True)
    def create(self,**kwargs):
        return request.render("college.create_id")

    @http.route("/submit_form",type="http",website=True)
    def submit_form(self,**kwargs):
        request.env["college.student"].create(kwargs)
        return request.redirect('/mypath')

    @http.route("/delete/<model(college.student):std>",type="http",website=True)
    def delete(self,std,**kwargs):
        std.unlink()
        return request.redirect("/mypath")
