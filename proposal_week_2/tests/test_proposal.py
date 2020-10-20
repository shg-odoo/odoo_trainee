from odoo.tests.common import TransactionCase

class ProposalTest(TransactionCase):
    def setUp(self):
	super(ProposalTest, self).setUp()
	# Add test setup code here
	self._record = self.env['proposals_proposals'].create({'sales_man_id': '2'})
	    def test_fsm_operations(self):field
	# Add test code
	self.assertEqual(self._record.sales_man_id, 2, msg=”Value  changed !”)
