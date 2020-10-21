from odoo.tests.common import TransactionCase

class ProposalTest(TransactionCase):
	def setUp(self):
		super(ProposalTest, self).setUp()
		print("==================================")
		self._record = self.env['proposals_proposals'].create({'sales_man_id': '2'})
		self.assertEqual(self._record.sales_man_id, 2, msg="Error is there")
