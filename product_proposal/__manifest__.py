{
    'name': 'Product Proposal',
    'version': '1.0',
    'description': """This module enables to negotiate on the product proposals send via email""",
    'depends': ['sale', 'mail', 'website', 'portal', 'sale_management'],
    'data': [
        'views/product_proposal_view.xml',
        'data/sequence.xml',

    ],
    'installable': True,
}
