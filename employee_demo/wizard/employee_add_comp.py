from odoo import models, fields, api


class Employee(models.TransientModel):
    _name = 'employee.wizard'
    
    company_id = fields.Many2one('employee.company')

    def add_company(self):
        active_ids = self._context.get('active_ids')
        self.env['employee'].browse(active_ids).write({'company_id':self.company_id})