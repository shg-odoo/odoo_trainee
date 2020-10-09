# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
    this is sunil`s academy in odoo india""",

    'description': """
        This is module for academy application,
        we can manange all the courses, classes and sessions
        in one module.
    """,

    'author': "Sunil Shrimali",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
