# -*- coding: utf-8 -*-
{
    'name': "Student Application",

    'summary': """Student Model First Application""",

    # 'description': """
    #     Open Academy module for managing trainings:
    #         - training courses
    #         - training sessions
    #         - attendees registration
    # """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    'depends': ['base'],

    # always loaded
    'data': [
        'views/student_view.xml',
        'data/student_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable':True,
    'application':True,
    'auto_install':False,
}