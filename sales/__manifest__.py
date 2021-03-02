{
    'name': ' sales',
    'version': '1.0',
    'summary': 'sales odoo',
    'sequence' : 5,
    'category': 'Management',
    'depends': ['base','mail'],
    'data': [
        'data/sequence.xml',
        'views/sales.xml',
    ],
    'application' : True,
}
