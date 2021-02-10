{
    'name': 'odoo trainee',
    'version': '1.0',
    'summary': 'practice odoo',
    'sequence' : 5,
    'category': 'Management',
    'depends': ['base', 'mail'],
    'data': [
        'data/student_data.xml',
        'views/student.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv'
    ],
    'application' : True,
}
