# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proposal_week_2(models.Model):
#     _name = 'proposal_week_2.proposal_week_2'
#     _description = 'proposal_week_2.proposal_week_2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
