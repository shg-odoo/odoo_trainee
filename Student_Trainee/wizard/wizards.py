from odoo import models, fields


class SchoolWizard(models.TransientModel):
    _name = "school.wizard"
    _description = "Quick Registration Of School"

    school_id = fields.Many2one("student.school", string="School")

    def add_school(self):
        ids = self._context.get("active_ids")
        return (
            self.env["school.student"].browse(ids).write({"school_id": self.school_id})
        )
