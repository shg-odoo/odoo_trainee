{
    'name': 'odoo trainee',
    'version': '1.0',
    'summary': 'practice odoo',
    'sequence' : 5,
    'category': 'Management',
    'depends': ['website', 'base', 'mail'],
    'data': [
        'data/mail_template.xml',
        'data/student_data.xml',
        'wizard/student_wizards.xml',
        'views/student.xml',
        'views/template.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'report/report_student.xml',
    ],
    'application' : True,
}
