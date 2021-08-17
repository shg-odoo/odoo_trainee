{
    'name': 'student',
    'version': '1.0',
    'summary': 'First Model',
    'category': 'practice',
    'depends': ['base'],


    'data': [
        'security/ir.model.access.csv',
        'security/sec.xml',
        'data/std_data.xml',
        'views/student.xml',
        'wizard/std_wizard.xml',
        'report/std_report.xml',
    ],

    'application' : True,
}
