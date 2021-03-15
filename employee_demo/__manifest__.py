# -*- coding: utf-8 -*-

{
    'name': "Employee",
    'description': """
        Employee Details
    """,

    'author': "Karan",
    'category': 'Test',
    'version': '0.1',

    'depends': ['base', 'website'],

    'data': [
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/employee_web_view.xml',
        'data/data.xml',
        'data/sequence.xml',
        'wizard/employee_add_comp_views.xml',
        'report/employee_report.xml',
    ],

    'application': True

}
