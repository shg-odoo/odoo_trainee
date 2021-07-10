from odoo import models


class CarRentalXlsx(models.AbstractModel):
    _name = 'report.car_rental.report_rental_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 11, })
        format3 = workbook.add_format({'num_format': 'dd/mm/yy hh:mm'})
        format2.set_align('center')
        format3.set_align('center')
        sheet = workbook.add_worksheet('Car Rental')
        sheet.merge_range(2, 2, 2, 3, 'Customer', format1)
        sheet.merge_range('E3:G3', lines.partner_id.name, format2)
        sheet.write(3, 2, 'Car', format1)
        sheet.write(3, 4, lines.car_id.car_name, format2)
        sheet.merge_range('C5:D5', 'Booking From', format1)
        sheet.merge_range('H5:I5', 'Booking To', format1)
        sheet.merge_range('E5:G5', lines.from_date, format3)
        sheet.merge_range('J5:L5', lines.to_date, format3)
        sheet.merge_range('C8:E8', 'Number Of Seats', format1)
        sheet.merge_range('F8:H8','Rate Per Hour',format1)
        sheet.merge_range('I8:J8','Total Hour',format1)
        sheet.merge_range('K8:L8','Sub Total',format1)
        sheet.merge_range('C9:E9',lines.car_id.number_of_seats, format2)
        sheet.merge_range('F9:H9', lines.car_id.amount_per_hour, format2)
        sheet.merge_range('I9:J9', lines.rental_lines.total_hour, format2)
        sheet.merge_range('K9:L9', lines.rental_lines.sub_total, format2)

