from odoo import http

class CarRentalWeb(http.Controller):
    @http.route('/CarRental',type='http',auth="public", website=True)
    def render_car_rental_web_page(self,**kwargs):
        list=[]
        car_web= http.request.env['car.car'].sudo().search([])
        for cars in car_web:
            car_details={
                'name': cars.car_name,
                'car_image':cars.image,
                'car_rent':cars.amount_per_hour,
                'car_seats':cars.number_of_seats
            }
            list.append(car_details)
            print(list,'pppppppppppppppp')

        return http.request.render('car_rental.car_rental_page_template',{
            'car_details':list,
        })