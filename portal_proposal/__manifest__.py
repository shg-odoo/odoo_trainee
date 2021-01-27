# -*- coding: utf-8 -*-
{
    'name': 'Portal Proposal',
    'version': '1.1',
    'category': 'Sales',
    'sequence': 10,
    'summary': 'Proposal to Sales Order',
    'description': """Portal proposal helps propose a quotation for a sales order to a customer.""",
    'website': 'https://www.odoo.com',
    'depends': ['sale_management', 'website_sale'],
    'data': ['security/ir.model.access.csv', 'data/proposal_data.xml', 'views/proposal_view.xml', 'views/website_proposal_view.xml'],
    'qweb': [],
    'demo': [],
    'test': ['static/tests/proposal_tests.js'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
