
# {
#     'name': 'training_demo',
#     'version': '1.0',
#     'category': 'Tools',
#     'summary': 'papo-Training-odoo',
#     'depends': ['web'],
#     'data': [
#         'security/ir.model.access.csv',
#         'views/nursery_plant_views.xml',
#         'views/nursery_customer_views.xml',
#         'views/nursery_order_views.xml',
#         'views/nursery_plant_templates.xml',
#         'views/nursery_plant_quote_ask.xml',
#         'views/assets.xml',
#         'views/nursery_order_portal_templates.xml',
#         'data/ir_sequence_data.xml',
#         'data/mail_template_data.xml',
#         'data/plant_data.xml',
#         'security/security.xml',
#     ],
#     'application': True,
# }
{
    'name': 'training_demo',
    'version': '1.0',
    'summary': 'papo-practice odoo',
    'sequence' : 1,
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'data/employee_staticData.xml',
        'wizard/employee_wizards.xml',
        'views/employee.xml'
        # 'data/sequence.xml',
        # 'security/ir.model.access.csv',
        # 'report/report_student.xml'
    ],
    'application' : True,
}