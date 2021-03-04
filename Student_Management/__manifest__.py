{
    'name':'Student',
    'version':'1.0',
    'catagory': 'Extra Tools',
    'author': 'Meet Patel (mte)',
    'summery': 'Student Management Software',
    'depends': ['base','website','mail'],
    'data':[
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/student_data.xml',
        'views/student.xml',
        'views/template.xml',
        'wizard/add_college_wizard_view.xml',
        'report/student_report.xml',
        'report/report_inherit.xml',
        'data/sequence.xml',

    ],
    'application':True,
}