{
    'name': 'Student',
    'version': '1.0',
    'category': 'Trainee Demo',
    'sequence': 5,
    'summary': 'Trainee demo module',
    'depends': ['base'],

    'description': """
            module for trainee demo
            """,

    'data' : [
        'data/student_data.xml',
        'views/st_view.xml',
    ],
    'installable'          : 'True',
    'application'          : 'True',

}