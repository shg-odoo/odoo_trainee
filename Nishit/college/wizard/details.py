from odoo import fields,models,api

class detail(models.TransientModel):
    _name="student.wizard"

    #clg_id=fields.Many2one("colleges")
    hobb_id=fields.Many2many("student.hobbies",string="Hobbies")
    complain=fields.Char(string ="Complain Box")
    
    def add_complain(self):
        ids = self._context.get('active_ids')
        self.env['college.student'].browse(ids).write({'hobb_id': self.hobb_id})
    