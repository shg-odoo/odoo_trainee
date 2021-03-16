# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
	'name': "Manufacturers Info",
	'description': """Detailed Information about Manufacturers""",

	'author': 'Karan',
	'category': 'Test',
	'version': '0.1',

	'depends': ['base', 'website'],

	'data': [
		'views/cloth_manufacturer_views.xml',
		'views/cloth_manufacturer_web_view.xml',
		'report/manufacturer_report_view.xml',
		'report/labourers_report_view.xml',
		'wizard/labourer_add_wizard_view.xml'
	],

	'application': True


}

