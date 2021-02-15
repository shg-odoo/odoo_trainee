{
    'name': 'student_inherit',
    'version': '1.0',
    'category': 'Training practice for inheritance',
    'summary': 'Student inherited details details',
    'description': """making odoo tree for first 
    time using inheritance""",

    'depends':[
        'base','mail'
        ,'student'
    ],
    'data': [

        'views/inherit.xml',
    ],

    'application' : True
}
