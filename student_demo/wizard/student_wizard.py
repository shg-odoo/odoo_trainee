from odoo import models, fields, api,_

class Wizards(models.TransientModel):
    _name = "student.wizard"
    _description = "Wizard: ADD  College"


    college_id = fields.Many2one('student.college', string="College")


    def add_college(self):
        ids = self._context.get("active_ids")
        return self.env['student'].browse(ids).write({'college_id':self.college_id})