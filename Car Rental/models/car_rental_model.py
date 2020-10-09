from odoo import models,fields,api,_
class CarRental(models.Model):
    _name="car.rental"
    _rec_name = "partner_id"

    partner_id=fields.Many2one('res.partner', String="Customer")
    car_id=fields.Many2one('car.car',string="Your Car")
    from_date=fields.Datetime(string="Booking From",required=True)
    to_date=fields.Datetime(string="Booking To",required=True)
    name_seq=fields.Char(string="Booking Referance",copy=False,required=True,index=True,default=lambda self:_('New'))
    @api.model
    def create(self, vals):
        if vals.get('name_seq',_('New'))==_('New'):
            vals['name_seq']= self.env['ir.sequence'].next_by_code('car.rental') or _('New')

        result= super(CarRental,self).create(vals)
        print(result)
        return result


class Carcar(models.Model):
    _name="car.car"
    _rec_name="car_name"

    car_name=fields.Char(string="Car Name")
    number_of_seats=fields.Integer(string="Number Of Seats")
    amount_per_hour=fields.Float(String="Rate Per Hour")
    image=fields.Binary(string="Image",required=True)



