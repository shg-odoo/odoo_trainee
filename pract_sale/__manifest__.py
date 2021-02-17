# -*- coding: utf-8 -*-
{
    'name': "Pract_sale",

    'summary': """
        For Practice odoo modules """,

    'description': """
        Build Model like sale for trainning
    """,

    
    'category': 'Uncategorized',
    'version': '0.1',

    
    'depends': ['base'],

   
    'data': [
        'security/ir.model.access.csv',
        'views/sales_view.xml',
        'data/sequence.xml',
    ],
    'application' : True
}
