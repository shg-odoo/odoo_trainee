from odoo import fields,models,api


class Wizards(models.TransientModel):
    _name           = "student.wizard"
    _description    = "Add your college"

    college_id      = fields.Many2one('student.college',string="College")


    def add_college(self):
        ids   = self._context.get("active_ids")
        return self.env['student'].browse(ids).write({'college_id':self.college_id})
