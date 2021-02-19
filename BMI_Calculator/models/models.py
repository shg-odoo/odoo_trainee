from odoo import models, fields, api

class BMICalculator(models.Model):
    _name="bmi.calculator"
    _inherit="school.student"

    bmi=fields.Float(string="BMI",compute="_calculateBMI",store=True)

    @api.depends("weight","height")
    def _calculateBMI(self):
        for i in self:
            i.bmi=i.weight//(i.height*0.3048)**2