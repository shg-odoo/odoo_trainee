from odoo.tests import tagged
from odoo.addons.portal_proposal.tests.common import PortalProposal


@tagged('post_install', '-at_install')
class PortalProposalTest(PortalProposal):

	def test_proposal_record(self):
		vals = {'user_id':self.env['res.users'].search([('login', '=', 'admin')]).id,
				'partner_id':self.env['res.partner'].browse(10).id,
				'pricelist_id':self.env['product.pricelist'].browse(1).id,
				}
		proposal = self.env['portal.proposal'].create(vals)
		vals = {'proposal_id':proposal.id,
				'product_id':self.env['product.product'].browse(20).id,
				'proposed_qty':5,
				'proposed_price':100,
				}
		line = self.env['portal.proposal.line'].create(vals)
		
		self.assertEqual(line.proposed_qty, 5)
		self.assertEqual(line.proposed_price, 100)
		self.assertEqual(line.proposal_id, proposal.id)
		print('The test was succesfull!')

		proposal.send()
