# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'academy.teachers'

    name = fields.Char()
    biography = fields.Html()
    
    course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")

class Course(models.Model):
    _inherit = 'product.template'
    teacher_id = fields.Many2one('academy.teachers', string="Teacher")
