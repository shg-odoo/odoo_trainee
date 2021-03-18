# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class doctor_inherit(models.Model):
#     _name = 'doctor_inherit.doctor_inherit'
#     _description = 'doctor_inherit.doctor_inherit'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
