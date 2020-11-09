from odoo.tests import common
import datetime
 
 
class TestProposalOrder(common.TransactionCase):
    def test_proposal_order_flow(self):

        # create customer
        partner_vals = {
            'name' : 'Asusteck',
            'property_product_pricelist' : self.env.ref('product.list0')
        }
        partner = self.env['res.partner'].create(partner_vals)
        print(partner,partner.name,"Partner Created!!\n")

        # Test code for creating proposal order
        proposal_vals = {
            'partner_id' : partner.id,
            'pricelist_id' : partner.property_product_pricelist.id,
            'date_order' : datetime.datetime.now(),
            'user_id' : self.env.ref('base.user_demo').id,

        }
        proposal_order = self.env['proposal.order'].create(proposal_vals)
        print(proposal_order,proposal_order.user_id.name,"Proposal created for customer Asusteck!!\n")

        #Creating new product called Product A
        product_val = {
            'name' : 'Product A',
            'type' : 'product'
        }
        product = self.env['product.template'].create(product_val)
        print(product,product.name,"Product Created!!!\n")

        # Test code for creating Poposal order lines
        product_id = self.env['product.product'].search([('product_tmpl_id', '=', product.id)])
        proposal_order_line_vals = {
            'product_id' : product_id.id,
            'name' : product_id.name,
            'qty_proposed' : 5,
            'qty_accepted' : 5,
            'price_proposed' : 5,
            'price_accepted' : 5,
            'product_uom' : product_id.uom_id.id if product_id.uom_id else 1,
            'proposal_id' : proposal_order.id,
        }
        
        proposal_order_line = self.env['proposal.order.line'].create(proposal_order_line_vals)
        print(proposal_order_line,"this is line!!\n\n")

        #sending mail to customer
        email_ctx = proposal_order.send_mail_customer().get('context', {})
        proposal_order.with_context(**email_ctx).message_post_with_template(email_ctx.get('default_template_id'))
        self.assertTrue(proposal_order.state == 'sent', 'proposal order: state after sending is wrong')
        print(proposal_order.state,"proposal order state")

