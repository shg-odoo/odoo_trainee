from odoo import models, fields, api, exceptions, _
from datetime import timedelta


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Session"


    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be an attendee"))

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if not rec.seats:
                rec.taken_seats = 0.0
            else:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats

    @api.onchange('seats', 'attendee_ids')
    def _onchange_verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                    
                },
            }

    @api.depends('start_date', 'duration')
    def _compute_get_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.duration):
                rec.end_date = rec.start_date
                continue
            duration = timedelta(days=rec.duration, seconds=-1)
            rec.end_date = rec.start_date + duration

    def _set_end_date(self):
        for rec in self:
            if not (rec.start_date and rec.end_date):
                continue
            rec.duration = (rec.end_date - rec.start_date).days + 1

    @api.depends('attendee_ids')
    def _compute_get_attendees_count(self):
        for rec in self:
            rec.attendees_count = len(rec.attendee_ids)

    name = fields.Char(string="Title", required=True)
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Float(digits=(6,2), help="Duration in Days")
    seats = fields.Integer("Number of Seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|',('instructor', '=', True),('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_compute_taken_seats')
    active = fields.Boolean(default=True)
    end_date = fields.Date(string="End Date", store=True,
        compute='_compute_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(
        string="Attendees count", compute='_compute_get_attendees_count', store=True)
    color = fields.Integer()

