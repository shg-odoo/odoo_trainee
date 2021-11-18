{
	'name': 'roku_app',
    'version': '1.0',
    'summary': 'practice odoo',
    'sequence' : 5,
    'category': 'Management',
    'depends': ['base'],

    'data': [
            
            'security/security.xml',
            'security/ir.model.access.csv',
    		'data/s_data.xml',
    		'view/student.xml',
            'wizard/s_wizard.xml',
            'report/repo_student.xml'



    		],
            
    'application' : True,


}
