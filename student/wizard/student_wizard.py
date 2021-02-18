from odoo import fields,models,api

class Wizard(models.TransientModel):
    _name = 'student.wizard'
    _description = "Wizard for adding college using action"

    college_id = fields.Many2one('student.college', string='College')

    def add_college(self):
        ids = self._context.get('active_ids')
        self.env['student'].browse(ids).write({'college_id':self.college_id})

    def get_data(self):
        college_data = self.env['student.college'].search([('college_city','=','PAtan')])
        print("college data :" , college_data)
        for rec in college_data:
            print("college name",rec.college_name)
            print("college city",rec.college_city)
