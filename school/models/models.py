# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'school.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student Table"

    name = fields.Char(string="Name", required=True)
    description = fields.Text()
    age = fields.Integer(string="Age")
    gender = fields.Selection([
    	('male', 'Male'),
    	('female', 'Female'),
    	('other', 'Other'),
    	],string='Gender', default='male')
    image  = fields.Binary(string="Image")