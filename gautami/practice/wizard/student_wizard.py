from odoo import models, fields, api

class Student(models.TransientModel):
    _name = 'student.wizard'

    college_id = fields.Many2one('college.details')

    def add_college(self):
        ids = self._context.get('active_ids')
        self.env['student.details'].browse(ids).write({'college_id': self.college_id})
