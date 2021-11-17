{
	'name': 'roku_app',
    'version': '1.0',
    'summary': 'practice odoo',
    'sequence' : 5,
    'category': 'Management',
    'depends': ['base'],

    'data': [

    		'data/s_data.xml',
    		'view/student.xml',
            'wizard/s_wizard.xml',
            'report/repo_student.xml'


    		],
            
    'application' : True,


}
