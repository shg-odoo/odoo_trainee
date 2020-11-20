from odoo import models, fields, api, _


class ResPartner(models.Models):
    _inherit=['res.partner']

    name = fields.Char(string='Name')
    email = fields.Integer(string='Email')
    phone= fields.Integer(string='Phone')


