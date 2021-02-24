from odoo import models, fields, api,_



class customers(models.Model):
    _name = 'sales.customers'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customers Details"
    _rec_name = "customer_name"


    customer_id = fields.One2many("sales","customer",string="Customers Id")
    customer_name = fields.Char(string="Customer Name")
    image = fields.Binary(string='Image')
    company_address = fields.Char(string="Company Address", track_visibility="always")
    phone_no = fields.Char(string="Phone No")
    email = fields.Char(string="Email")
    person_contact = fields.Char("Contact Of Person")
    person_name = fields.Char("Name Of Contact")
    person_position = fields.Char("Position")
    person_email = fields.Char("Person Email")
    person_image = fields.Binary(string='Person Image')
