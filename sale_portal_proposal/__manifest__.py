# -*- coding: utf-8 -*-
{
    'name': "Sale Portal Proposal",

    'summary': """
    With this module you will able to manage a proposal of a list of product to a customer
        """,
    'author': "vva-odoo",
    'website': "http://www.odoo.com",
    'category': 'Sales/Sales',
    'version': '14.01',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/mail_template.xml',
        'security/proposal_security.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/report_sale_portal_proposal.xml',
        'views/sale_portal_proposal.xml',
        'views/portal_proposal.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
