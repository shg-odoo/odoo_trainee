{
    'name': 'Car Rental',
    'version': '1.0',
    'description': """Car Rental""",
    'depends': ['website'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/css_styles.xml',
        'views/car_rental_views.xml',
        'views/car_rental_webpage.xml',
        'reports/car_rental_report.xml',
        'reports/report_template.xml',
        'data/sequence.xml',
        'data/car_rental_demo_data.xml',
    ],
    'installable': True,
}
