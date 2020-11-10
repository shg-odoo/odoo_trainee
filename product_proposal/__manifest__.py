{
    'name': 'Product Proposal',
    'version': '1.0',
    'description': """This module enables to negotiate on the product proposals send via email""",
    'depends': ['sale', 'mail', 'website', 'portal', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'report/report_portal.xml',
        'data/mail_data.xml',
        'data/ir_sequence.xml',
        'views/product_proposal_view.xml',
        'views/proposal_portal_view.xml'

    ],
    'installable': True,
    'application': True
}
