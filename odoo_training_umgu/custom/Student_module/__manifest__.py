# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Student',
    'version': '1.0',
    'category': 'Management',
    'sequence': 1,
    'summary': 'Student details management module',
    'description': """This app manages the students detalails
    """,
    'depends': ['website'],
    'data' : ['views/student_details_views.xml',
              'views/other_task_views.xml',
              'data/student_details_data.xml',
              'reports/report.xml',
              'security/security.xml',
              'views/templates.xml',
              'security/ir.model.access.csv',
              
    ],

    'application': True,
}