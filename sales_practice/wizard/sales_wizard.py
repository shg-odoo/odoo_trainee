from odoo import fields, models, api


class Wizards(models.TransientModel):
    _name = "sales.wizard"
    _description = "Wizard: Quick Registration of Sales"


    next_activity = fields.Many2one('sales.activity', string="Activity")


    def add_activity(self):
        ids = self._context.get("active_ids")
        return self.env['sales'].browse(ids).write({'next_activity':self.next_activity})


