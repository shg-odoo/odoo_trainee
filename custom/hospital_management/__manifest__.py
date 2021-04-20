# -*- coding: utf-8 -*-
{
	'name': "hospital_management",

	'summary': """
		Short (1 phrase/line) summary of the module's purpose, used as
		subtitle on modules listing or apps.openerp.com""",

	'description': """
		Long description of module's purpose
	""",

	'author': "My Company",
	'website': "http://www.yourcompany.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
	# for the full list
	'category': 'Uncategorized',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base','mail','website'],

	# always loaded
	'data': [
		'security/ir.model.access.csv',
		'security/security.xml',
		# 'views/views.xml',
		# 'views/patient.xml',
		'views/patient_1.xml',
		'wizards/patient_wizard.xml',
		'reports/patient_report.xml',
		'views/doctor.xml',
		'data/sequence.xml',
		'views/appointment.xml',
		'views/web_patient.xml',
		'views/patient_data_submit.xml'
		# 'views/templates.xml',
	],
	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}
