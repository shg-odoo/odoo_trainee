from odoo import http
from odoo.http import request


class PartnerForm(http.Controller):
    @http.route(['/customer/form'], type='http' , auth='public',website=True)
    def partner_form(self,**post):
        print("keiri")
        return request.render("test-module.tmp_customer_form",{})

    @http.route(['/customer/form/submit'],type='http' , auth='public',website=True)
    def customer_form_submit(self,**post):
        partner = request.env['res.partner'].sudo().create({
            'name':post.get('name'),
            'email':post.get('email'),
            'phone':post.get('phone')
        })
        vals={
            'partner':partner
        }
        print("vals...........",vals)

        return request.render("test-module.tmp_customer_form_success",vals)