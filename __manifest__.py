# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'sales_proposal',
    'version': '0.1',
    'category': 'Uncategorized',
    'summary': 'Sales Proposal',
    'description': """
        This module contains all Proposal.
    """,
    'depends': ['sale','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/summary_report.xml',
        'views/proposal.xml',
        'views/menu.xml',
        'views/seq_and_mail.xml',
        'views/template.xml',
        'views/assets.xml',
        'report/report.xml',
        'report/wizard_report_template.xml',
    ],
    'demo': []
}
