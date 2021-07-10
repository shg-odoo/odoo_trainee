from odoo import models, fields, api, _
from datetime import datetime

class CarRental(models.Model):
    _name = "car.rental"
    _rec_name = "partner_id"

    partner_id = fields.Many2one('res.partner', String="Customer",required=True)
    car_id = fields.Many2one('car.car', string="Your Car",required=True)
    from_date = fields.Datetime(string="Booking From",required=True)
    to_date = fields.Datetime(string="Booking To",required=True)
    rental_lines = fields.One2many('car.rental.lines', 'carrental_id')
    name_seq = fields.Char(string="Booking Referance", copy=False, required=True, index=True,
                           default=lambda self: _('New'))
    _sql_constraints = [
        ('date_check2', "CHECK ((from_date <= to_date))", "The start date must be greater that the end date.")]
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('car.rental') or _('New')
        result = super(CarRental, self).create(vals)
        return result

    @api.onchange('car_id', 'from_date', 'to_date')
    def _onchange_car_id(self):
        for rec in self:
            hours = 0
            lines = [(5, 0, 0)]
            if rec.from_date and rec.to_date:
                delta = datetime.strptime(str(rec.to_date), '%Y-%m-%d %H:%M:%S') - datetime.strptime(
                    str(rec.from_date), '%Y-%m-%d %H:%M:%S')
                hours = float(delta.total_seconds()) / 3600

            for line in self.car_id:
                val = {
                    'seat': line.number_of_seats,
                    'amount_per': line.amount_per_hour,
                    'total_hour': hours,
                    'sub_total': line.amount_per_hour * hours,
                    'currency_id': self.currency_id
                }
                lines.append((0, 0, val))
            rec.rental_lines = lines


class Carcar(models.Model):
    _name = "car.car"
    _rec_name = "car_name"

    car_name = fields.Char(string="Car Name", required=True)
    number_of_seats = fields.Integer(string="Number Of Seats")
    amount_per_hour = fields.Float(String="Rate Per Hour", required=True)
    image = fields.Binary(string="Image",required=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)


class CarRentalLines(models.Model):
    _name = "car.rental.lines"

    total_hour = fields.Float(string="Total Booking Hour")
    amount_per = fields.Float(string="Rate Per Hour")
    sub_total = fields.Float(string="Sub Total")
    carrental_id = fields.Many2one('car.rental', string="Car Rental ID")
    seat = fields.Integer(string="Number Of Seats")
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
