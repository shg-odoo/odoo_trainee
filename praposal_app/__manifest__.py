# -*- coding: utf-8 -*-
{
    'name': "Praposal Application",
    'sequence':'1',
    'summary': "Proposal Application",
    'description': "This app for the sent the proposal to customer for the products",
    'author': "Odoo India ,Roopam Rathod(rrt)",
    'website': "http://www.odoo.com",
    'category': 'Uncategorized',
    'version': '12.0.0.1',
    'depends': ['base','sale','sale_management','web','website','portal'],
    'data': [
        'security/ir.model.access.csv',
        'report/proposal_report.xml',
        'data/proposal_sequence.xml',
        'data/proposal_mail.xml',
        'views/proposal_templates.xml',
        'views/proposal_portal_template.xml',
        'views/proposal.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
