from odoo import fields, models, api


class Wizards(models.TransientModel):
    _name = "student.wizard"
    _description = "Wizard: Quick Registration of College"


    college_id = fields.Many2one('student.college', string="College")
    hobbies_id = fields.Many2one('student.hobby', string="Hobbies")


    def add_college(self):
        ids = self._context.get("active_ids")
        return self.env['student'].browse(ids).write({'college_id':self.college_id})

    def add_hobbies(self):
        ids = self._context.get("active_ids")
        return self.env['student'].browse(ids).write({'hobbies_id':self.hobbies_id})