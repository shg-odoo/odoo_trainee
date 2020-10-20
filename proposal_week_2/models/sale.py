from odoo import models, fields, api, exceptions


class Sale(models.Model):
    _inherit = ['sale.order']