# -*- coding: utf-8 -*-

{
    'name': "Employee",
    'description': """
        Employee Details
    """,

    'author': "Karan",
    'category': 'Test',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/tree.xml',
        'data/data.xml',
        'wizard/employee_add_comp_views.xml',
        'report/employee_report.xml'
    ],

    'application': True

}