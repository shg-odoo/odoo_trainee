from odoo import http
from odoo.http import request
 
class student(http.Controller): 
 
    @http.route('/student', auth='public', website=True) 
    def student_detail(self): 
        return "<h1>Hello World!</h1>" 
