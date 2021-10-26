{
    'name': 'Employee',
    'version': '1.1.1',
    'summary': 'Practice module',
    'author': 'Aman Jolhe',
    'sequence' : 5,
    'category': 'Tool',
    'depends': ['base','website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/employee_view.xml',
        'views/template.xml',
        'static/employee_static.xml',
        'wizard/employee_wizard.xml'
    ],
    'application' : True,
}
