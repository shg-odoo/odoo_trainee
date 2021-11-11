# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Student',
    'version': '1.0',
    'category': 'Management',
    'sequence': 1,
    'summary': 'Student Management software',
    'description': """This app manages the students detal
    """,
    'depends': ['base'],
    'data' : ['views/student_details_views.xml',
              'data/student_details_data.xml'
    ],
    'application': True,
    
}
