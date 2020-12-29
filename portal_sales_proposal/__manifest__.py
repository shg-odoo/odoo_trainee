# -*- coding: utf-8 -*-
{
    'name': "Portal Sales Proposal",
    'summary': """With this module you will able to manage Sales Proposal of a list of product to a customer""",
    'author': "aoh-odoo",
    'website': "http://www.odoo.com",
    'category': 'Sales/Sales',
    'version': '14.00',
    'depends': ['sale_management'],
    'data': [
        'data/sequence.xml',
        'data/proposal_mail_template.xml',
        'security/proposal_security.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/report_portal_sales_proposal.xml',
        'views/portal_sales_proposal.xml',
        'views/proposal_portal.xml',
        'views/templates.xml',
    ],
}
