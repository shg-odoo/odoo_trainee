from odoo.tests import common


class TestPortalSalesProposal(common.TransactionCase):

    def setUp(self):
        super(TestPortalSalesProposal, self).setUp()
        self.tax_model = self.env['account.tax']
        self.so_model = self.env['sale.order']
        self.so_line_model = self.env['sale.order.line']
        self.res_partner_model = self.env['res.partner']
        self.product_tmpl_model = self.env['product.template']
        self.product_model = self.env['product.product']
        self.product_uom_model = self.env['uom.uom']
        self.pricelist_model = self.env['product.pricelist']

    def test_portal_sales_proposal(self):

        partner_a = self.env['res.partner'].create({
            'name': 'partner_a',
            'company_id': False,
        })
        # user.company_ids |= self.company
        # user.company_id = self.company
        uom_id = self.product_uom_model.search([('name', '=', 'Units')])[0]
        pricelist = self.pricelist_model.search([('name', '=', 'Public Pricelist')])[0]
        tax_exclude_id = self.tax_model.create(dict(name="Exclude tax",
                                                    amount='0.00',
                                                    type_tax_use='sale'))
        product = self.env['product.product'].create({
            'name': "ProductA",
            'list_price': 200.0,
            'taxes_id': [(6, 0, [tax_exclude_id.id])]
        })
        sale_proposal = self.env['portal.sales.proposal'].with_context(mail_notrack=True, mail_create_nolog=True).create(
            {
                'partner_id': partner_a.id,
                'pricelist_id': pricelist.id,
                'user_id': self.env.ref('base.user_admin').id,
                'line_ids': [
                    (0, 0, {
                        'name': product.name,
                        'product_id': product.id,
                        'product_uom_qty': 2,
                        'product_uom': uom_id.id,
                        'price_unit': product.list_price,
                    }),
                ],
            })
        for line in sale_proposal.line_ids:
            line.product_id_change()
        sale_proposal.onchange_partner_id()
        self.assertEqual(sale_proposal.amount_total, 400.0, 'Sale: Wrong total amount')
        sale_proposal.action_send_mail()
        self.assertTrue(sale_proposal.state == 'sent', 'Sale Proposal: Email sending failed!')
