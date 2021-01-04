# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.website.tools import get_video_embed_code

class Course(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Table"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    age = fields.Integer(string="Age")
    date_from = fields.Datetime(string="From")
    date_to = fields.Datetime(string="To")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ],string='Gender', default='male')
    image  = fields.Binary(string="Image")
    active = fields.Boolean('Active',default=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self : self.env.user.company_id)
   


#     video_url = fields.Char('Video URL',
#                             help='URL of a video for showcasing your student.')
#     embed_code = fields.Char(compute="compute_embed_code")


# @api.depends('video_url')
# def compute_embed_code(self):
#     for rec in self:
#         rec.embed_code = get_video_embed_code(rec.video_url)

# @api.onchange('company_id')
# def set_student_gender(self):
#     for rec in self:
#         if rec.company_id:
#                 rec.gender = rec.company_id.gender