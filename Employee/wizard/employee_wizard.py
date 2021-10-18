from odoo import fields, models, api


class Wizards(models.TransientModel):
    _name = "employee.wizard"
    _description = "Wizard:Registration of Department"

    department_id = fields.Many2one('employee.department', string="Department")


    def add_department(self):
        ids = self._context.get("active_ids")
        return self.env['employee'].browse(ids).write({'department_id':self.department_id})