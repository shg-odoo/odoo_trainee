# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class PortalProposal(TransactionCase):

	@classmethod
	def setUpClass(cls):
		res = super(PortalProposal, cls).setUpClass()
		return res