from odoo import fields,models,api

class Wizard(models.TransientModel):
    _name = 'student.wizard'
    _description = "Wizard for adding college using action"

    college_id = fields.Many2one('student.college', string='College')

    def add_college(self):
        ids = self._context.get('active_id')
        self.env['student'].browse(ids).write({'college_id':self.college_id})
