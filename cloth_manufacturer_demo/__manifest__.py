# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
	'name': "Manufacturers Info",
	'description': """Detailed Information about Manufacturers""",

	'author': 'Karan',
	'category': 'Test',
	'version': '0.1',

	'depends': ['base'],

	'data': [
		'views/cloth_manufacturer_views.xml',
		'wizard/labourer_add_wizard_view.xml'
	],

	'application': True


}

