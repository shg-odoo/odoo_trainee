from odoo import models, fields, api

class IWcalculator(models.Model):
    _name="iw.calculator"
    _inherit="student"

    iw=fields.Float(string="Ideal Weight",compute="_calculateIW",store=True)

    @api.depends("height","gender")
    def _calculateIW(self):
        for i in self:
            if i.gender == "male":
                i.iw = 56.2 + 1.41*(12*(((i.height)/30.48)-5))
            elif i.gender == "female":
                i.iw = 53.2 + 1.36*(12*(((i.height)/30.48)-5))