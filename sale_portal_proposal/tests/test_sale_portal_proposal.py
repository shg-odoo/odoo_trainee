from odoo.tests import common


class TestSalePortalProposal(common.TransactionCase):

    def setUp(self):
        super(TestSalePortalProposal, self).setUp()

        self.tax_model = self.env['account.tax']
        self.so_model = self.env['sale.order']
        self.so_line_model = self.env['sale.order.line']
        self.res_partner_model = self.env['res.partner']
        self.product_tmpl_model = self.env['product.template']
        self.product_model = self.env['product.product']
        self.product_uom_model = self.env['uom.uom']
        self.pricelist_model = self.env['product.pricelist']

    def test_sale_portal_proposal(self):
        # group_sale_user = self.env.ref('sale.group_sale_salesman')
        # group_proposal_user = self.env.ref('sale_portal_user.group_sale_portal_proposal_manager')
        # user = self.env['res.users'].create({
        #     'name': 'Because I am saleman!',
        #     'login': 'saleman',
        #     'groups_id': [(6, 0, [group_sale_user, group_proposal_user])],
        # })
        # user.partner_id.email = 'saleman@test.com'
        #
        # # Shadow the current environment/cursor with the newly created user.
        # self.env = self.env(user=user)
        # self.cr = self.env.cr
        #
        # company = self.env['res.company'].create({
        #     'name': 'Test Company',
        #     'currency_id': self.env.ref('base.USD').id,
        # })
        # company_data = self.setup_sale_configuration_for_company(self.company)

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
            'list_price': 180.0,
            'taxes_id': [(6, 0, [tax_exclude_id.id])]
        })
        sale_proposal = self.env['sale.portal.proposal'].with_context(mail_notrack=True, mail_create_nolog=True).create(
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
        self.assertEqual(sale_proposal.amount_total, 360.0, 'Sale: total amount is wrong')
        sale_proposal.action_send_mail()
        self.assertTrue(sale_proposal.state == 'sent', 'Sale Proposal: state after sending is wrong')
