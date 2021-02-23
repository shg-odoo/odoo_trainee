from odoo import models, fields, api

class BMICalculator(models.Model):
    _name="bmi.calculator"
    _inherit="school.student"

    bmi=fields.Float(string="BMI",store=True)
    
    @api.onchange("weight","height")
    def _calculateBMI(self):
        for i in self:
            temp1=(i.height*0.3048)**2
            print(temp1)
            i.bmi=i.weight*temp1