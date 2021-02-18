{
    'name': 'student',
    'version': '1.0',
    'category': 'Training practice',
    'summary': 'Student details',
    'description': """making odoo tree for first 
    time""",

    'depends':[
        'base','mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_wizard_view.xml',
        'views/student_viewtree.xml',
        'data/student_data.xml',
        'data/sequence.xml',
        'report/student_report.xml',
        'data/mail_temp.xml',
        'security/security.xml',
    ],

    'application' : True
}
