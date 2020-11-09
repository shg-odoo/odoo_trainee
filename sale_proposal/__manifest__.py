# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "sale_proposal",
    'summary': """Portal Proposal for customers""",
    'description': """This module will help you to send product proposal to customers""",
    'website': "https://www.odoo.com/page/billing",
    'category': 'Sales/Sales',
    'version': '14.0.0.0',
    'depends': ['base','sale','portal'],
    'data': [
        'security/proposal_security.xml',
        'security/ir.model.access.csv',
        'data/mail_data.xml',
        'data/ir_sequence_data.xml',
        'report/proposal_report_portal_template.xml',
        'report/proposal_report_template.xml',
        'report/proposal_report.xml',
        'views/sale_proposal_view.xml',
        'views/template.xml',
    ],
}
