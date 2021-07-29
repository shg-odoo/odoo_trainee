# -*- coding: utf-8 -*-

from odoo import models, fields, api


class  Inherited_Student(models.Model):

	_inherit = "student"

	status =  fields.Selection([('learning','Learning'),('graduate','Graduate'),],'status',default='learning')

	