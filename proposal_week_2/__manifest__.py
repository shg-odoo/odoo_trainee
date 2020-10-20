# -*- coding: utf-8 -*-
{
    'name': "Final Proposal",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','mail'],

    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/proposal_view.xml',
        'views/sale.xml',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
        'report/proposal_report.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
