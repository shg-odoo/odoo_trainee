from odoo import api, models, fields

class AddCollegeWizard(models.TransientModel):
    _name = "add.college.wizard"
    _description = "Registration of College to Mutiple Student Records"

    college_ids = fields.Many2one('college', string='College')

    def add_college(self):
        ids = self._context.get('active_ids')
        self.env['student'].browse(ids).write({'college_ids':self.college_ids})