{
    'name': 'student',
    'version': '1.0',
    'summary': 'First Model',
    'category': 'practice',
    'depends': ['base','website'],


    'data': [
        'security/ir.model.access.csv',
        'security/sec.xml',
        'data/std_data.xml',
        'views/student.xml',
        'views/templates.xml',
        'wizard/std_wizard.xml',
        'report/std_report.xml'
    ],

    'application' : True,
}
