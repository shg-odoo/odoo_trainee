# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time

from odoo import api, fields, models


class SummaryReports(models.TransientModel):

    _name = 'summary.report.proposal'
    _description = 'Sale proposal Summary Report'

    date_from = fields.Datetime('From', default=lambda self: fields.Datetime.now())
    date_to = fields.Datetime('To', default=lambda self: fields.Datetime.now())
    state = fields.Selection([
        ('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')], default='draft')

    def print_report(self):
        obj_sp = self.env['sale.proposal'].search([
            ('proposal_date','>=',self.date_from),
            ('proposal_date','<',self.date_to),
            ('state','=',self.state)])
        return self.env.ref('odoo_trainee.report_sale_proposal').report_action(obj_sp)