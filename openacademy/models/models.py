from odoo import models, fields, api, exceptions, _
from odoo.exceptions import ValidationError
from datetime import timedelta


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible",
                                     index=True)
    session_ids = fields.One2many('openacademy.session',
                                  'course_id',
                                  string="Sessions"
                                  )

    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count([('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    _sql_constraints = [('name_description_check',
                         'CHECK(name != description)',
                         "The title of the course should not be the description"
                         ),
                        (
                            'name_unique',
                            'UNIQUE(name)',
                            "The course title must be unique"
                        ),
                        ]


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()
    instructor_id = fields.Many2one('res.partner',
                                    string="Instructor",
                                    domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
                if r.taken_seats >= 100:
                    raise exceptions.ValidationError(_("Taken seats Should Less or equal to Available seats."))

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {'warning': {'title': "Incorrect 'seats' value",
                                'message': "The number of available seats may not be negative", }, }
            if self.seats < len(self.attendee_ids):
                return {'warning': {'title': "Too many attendees",
                                    'message': "Increase seats or remove excess attendees", }, }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be an attendee"))

# class Session(models.Model):
#   _name = 'openacademy.session'
#   _description = "OpenAcademy Sessions"

#   name = fields.Char(required=True)
#   # instructor_name = fields.Many2many('openacademy.instrustor', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")
#   basic_knowledge = fields.Char()
#   category = fields.Selection([('programming_lang','Programming Language'), ('designing','Designing')])
#   start_date = fields.Date(required = True)
#   #end_date = fields.Date(constrains="Check_Date_Diff")

#   @api.constrains('end_date','start_date')
#   def Check_Date_Diff(self):
#       if self.end_date <= self.start_date:
#           raise ValidationError(_('The planned end date of the course cannot be prior to the planned start date.'))

#   # def name_get(self):
#   #   result = []
#   #   for record in self:
#   #       name = record.name + ' ' + str(id)
#   #       result.append((record.id, name))
#   #   return result

#   # def name_get(self):
#   #     result = []
#   #     for record in self:
#   #         name = record.name
#   #         result.append(name)
#   #     return result


class Instructor(models.Model):
    _name = 'openacademy.instructor'
    _description = "OpenAcademy Instructor"

    instructor_name = fields.Char(required=True)
    # instructor_id = fields.Integer(required=True)
    instructor_field = fields.Char()
    instructor_course = fields.Char()

# def name_get(self):
#     result = []
#     for record in self:
#         name = record.instructor_name + ' ' + str(record.instructor_id)
#         result.append((record.id, name))
#     return result


class Students(models.Model):
    _name = 'openacademy.student'
    _description = "OpenAcademy Students"

    student_name = fields.Char(required=True)
    student_email = fields.Char()
    student_course = fields.Char()
    student_instructor = fields.Char()

# student_course = fields.Many2many('openacademy.session', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")
# student_instructor = fields.Many2many('openacademy.instructor', string='Enrolled Course', help="Optional tags you may want to assign for custom reporting", widget="many2many_tags")
