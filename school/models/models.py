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
    students_lines = fields.One2many('school.student.lines','student_id', string="Students Lines")
    company_id = fields.Many2one('res.company', required=True, default=lambda self : self.env.user.company_id)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('done','Done'),
        ('cancel','Cancelled'),
        ], string='Status', readonly=True, default='draft')


    def wiz_test_action(self):
        return self.env['school.student']._for_xml_id("school.student.wiz_test_action")
        # return {
        #         'type': 'ir.actions.act_window',
        #         'res_model': 'student.wiz',
        #         'view_mode': 'form',
        #         'target': 'new'
        # }

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'


class CourseLines(models.Model):
    _name = 'school.student.lines'
    _description = "Student Table Lines"

    product_id = fields.Many2one('product.product', string="Courses")
    product_qty = fields.Integer(string="Course Code")
    student_id =fields.Many2one('school.student', string="Student ID")


# @api.onchange('company_id')
# def set_student_gender(self):
#     for rec in self:
#         if rec.company_id:
#                 rec.gender = rec.company_id.gender