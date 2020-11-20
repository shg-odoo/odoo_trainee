# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Test Module',
    'category': 'Sales'
                '',
    'summary': 'test',
    'description': "",
    'version': '1.0',
    'depends': ['website','contacts'],
    'data': [
        'views/website_form.xml'

    ],
    'installable': True,
    'auto_install': False,
    'application': True,

}
