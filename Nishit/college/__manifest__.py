{
    'name': 'Student',
    'version': '1.0',
    'category': 'Trainee Demo',
    'sequence': 5,
    'summary': 'Trainee demo module',
    'depends': ['base','website'],

    'description': """
            module for trainee demo
            """,

    'data' : [
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/template.xml',
        'reports/studentreport.xml',
        'wizard/wizard.xml'
      #  'views/teacher.xml'
            ],

    'application' : True

}
