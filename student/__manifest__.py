{
    'name': 'student',
    'version': '1.0',
    'summary': 'practice odoo',
    'sequence' : 1,
    'category': 'Management',
    'depends': ['base','website'],
    'data': [
            'security/ir.model.access.csv',
            'security/sequence.xml',
    		'views/st_view.xml',
    		'data/st_data.xml',
            'wizard/student_wizard.xml',
            'reports/report.xml',
            'views/cont.xml',
    ],
    'application' : True,
}