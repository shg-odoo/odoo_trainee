from odoo import fields, models, api


class Wizards(models.TransientModel):
    _name = "employee.wizard"


    company_id = fields.Many2one("employee.company", string="Company")
    # hobbies_id = fields.Many2many("employee.hobbies", string="Hobbies")


    def add_employee_company(self):
        ids = self._context.get("active_ids")
        return self.env['employee'].browse(ids).write({'company_id':self.company_id})

    # def add_employee_hobbies(self):
    #     ids = self._context.get("active_ids")
    #     return self.env['employee'].browse(ids).write({'hobbies_id':self.hobbies_ids})