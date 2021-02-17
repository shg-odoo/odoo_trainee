{
    'name': 'sales practice',
    'version': '1.0',
    'summary': 'practice sales',
    'sequence' : 5,
    'category': 'Sales',
    'depends': ['base', 'mail'],
    'data': [
        'views/sales_view.xml',
        'data/sequence.xml',
        'report/report_sales.xml'
    ],
    'application' : True,
}
