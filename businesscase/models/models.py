# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,timedelta

class businesscase(models.Model):
    _name = 'businesscase.businesscase'
    _description = 'businesscase.businesscase'
    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    def _default_validity_date(self):
        return self.datetime
        

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
