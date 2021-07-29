from odoo import http
from odoo.http import request

class StudentDetails(http.Controller):

    @http.route('/employee', type="http" , website=True)
    def student(self,**kwargs):
        pass