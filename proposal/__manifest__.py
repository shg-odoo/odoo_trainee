# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Business',
    'version' : '1.1',
    'summary': 'With this module you will able to manage a proposal of a list of product to a customer',
    'sequence': 10,
    'description': """
Manage list of product to a customer
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Business',
    # 'website': 'https://www.odoo.com/page/billing',
    'depends' : ['base', 'contacts', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/product.xml',
        'report/proposal_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
