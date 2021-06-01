from odoo import models, fields, api


class School(models.TransientModel):

    # Used for temporary or for certain period of time store records
    #  in database and than remove it

    _name = "school.wizard"
    _description = "Wizard for school"

    # mention fields that we want to show in wizard view
    school_id = fields.Many2one('student.school', string="School Name")

    def add_school(self):
        """
        This methods gets called when we click Add school button on model `student`
        in action button, because we have bind this action for perticular this `student`
        model.
        """
        ids = self.env.context.get('active_ids')
        print('='*15)
        print('self.env.context:', self.env.context)  # context is an dictionary containing below key,val
        # {'lang': 'en_US', 'tz': 'Europe/Brussels', 'uid': 1, 'allowed_company_ids': [1],
        #  'active_id': 3, 'active_ids': [3, 5], 'active_model': 'student',
        #  'active_domain': []}
        print('ids: ', ids)  # this will give all the selected ids which we can say active_ids
        #  ids:  [3, 5]
        self.env['student'].browse(ids).write({'school_id': self.school_id})  # write is ORM method
