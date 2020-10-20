{
    'name': 'Sale Proposal',
    'version': '1.0',
    'description': """Sale Proposal""",
    'depends': ['sale','mail','website','portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_proposal_view.xml',
        'data/sequence.xml',
        'data/mail_template.xml',

    ],
    'installable': True,
}
