from odoo import http
from odoo.http import request
from datetime import datetime


class CarRentalWeb(http.Controller):
    @http.route('/CarRental', type='http', auth="public", website=True)
    def render_car_rental_web_page(self, **kwargs):
        list = []
        car_web = http.request.env['car.car'].sudo().search([])
        for cars in car_web:
            car_details = {
                'car_id': cars.id,
                'name': cars.car_name,
                'car_image': cars.image,
                'car_rent': cars.amount_per_hour,
                'car_seats': cars.number_of_seats
            }
            list.append(car_details)
        return http.request.render('car_rental.car_rental_page_template', {
            'car_details': list,
        })

    @http.route(['/CarRental/<int:car_id>/booking'], type='http', auth="public", website=True)
    def car_rentnow_web_page(self, car_id, **kwargs):
        list = []
        car_web = http.request.env['car.car'].sudo().search([('id', '=', car_id)])
        for cars in car_web:
            car_details = {
                'car_id': cars.id,
                'name': cars.car_name,
                'car_image': cars.image,
                'car_rent': cars.amount_per_hour,
                'car_seats': cars.number_of_seats
            }
            list.append(car_details)
        return http.request.render('car_rental.car_rentnow_template', {
            'car_details': list,
        })

    @http.route(['/Carrental/booking_sumitted'], type='http', auth="public", methods=['POST'], website=True)
    def car_rentnow_booking_submitted(self, **post):
        car_obj = http.request.env['car.rental']
        car_match = car_obj.sudo().browse(post['car'])
        car_check = request.env['res.partner'].sudo().create({'name': post['partner_name']})
        delta = datetime.strptime(post['to'], '%Y-%m-%d') - datetime.strptime(
            post['from'], '%Y-%m-%d')
        hours = float(delta.total_seconds()) / 3600
        lines = [(5, 0, 0)]
        val = {
            'seat': post['seats'],
            'amount_per': post['rate'],
            'total_hour': hours,
            'sub_total': hours * int(float(post['rate']))
        }
        lines.append((0, 0, val))
        request.env['car.rental'].sudo().create({'car_id': post['car_id'],
                                                 'partner_id': car_check.id,
                                                 'from_date': post['from'],
                                                 'to_date': post['to'],
                                                 'rental_lines': lines})
        return http.request.render('car_rental.booking_done')
