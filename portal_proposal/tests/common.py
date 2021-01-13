from odoo.tests.common import TransactionCase, tagged



@tagged('post_install', '-at_install')
class PortalProposal(TransactionCase):

	@classmethod
	def setUpClass(cls, chart_template_ref=None):
		res = super(PortalProposal, cls).setUpClass()
		return res