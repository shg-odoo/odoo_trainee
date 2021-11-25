# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Teacher',
    'version': '1.0',
    'category': 'Management',
    'sequence': 1,
    'summary': 'Teacher details management module',
    'description': """This app manages the student detalails
    """,
    'depends': ['Student_module'],
    'data' : ['views/teacher_details_views.xml',
              'data/teacher_details_data.xml',
              'wizard/teacher_salary_update_view.xml'
    ],
    'application': True,
    
}