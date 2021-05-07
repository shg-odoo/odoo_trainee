{
    'name': "Student Application",
    'summary': """Student Model""",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/student_view.xml',
        'data/student_data.xml',
        'wizard/student_wizard.xml',
        'report/student_report.xml',
    ],
    'demo': [],
    'installable':True,
    'application':True,
    'auto_install':False,
}