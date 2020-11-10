from odoo.tests import common


class TestSalePortalProposal(common.TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.tax_model = cls.env['account.tax']
        cls.so_model = cls.env['sale.order']
        cls.so_line_model = cls.env['sale.order.line']
        cls.res_partner_model = cls.env['res.partner']
        cls.product_tmpl_model = cls.env['product.template']
        cls.product_model = cls.env['product.product']
        cls.product_uom_model = cls.env['uom.uom']
        cls.pricelist_model = cls.env['product.pricelist']



        cls.uom_id = cls.product_uom_model.search([('name', '=', 'Units')])[0]
        cls.pricelist = cls.pricelist_model.search([('name', '=', 'Public Pricelist')])[0]

        cls.partner_id = cls.res_partner_model.create(dict(name="Vishnu"))
        cls.tax_include_id = cls.tax_model.create(dict(name="Include tax",
                                                    amount='21.00',
                                                    price_include=True,
                                                    type_tax_use='sale'))
        cls.tax_exclude_id = cls.tax_model.create(dict(name="Exclude tax",
                                                    amount='0.00',
                                                    type_tax_use='sale'))

        product_tmpl_id = cls.product_tmpl_model.create(dict(name="PODSA",
                                                              list_price=120,
                                                              taxes_id=[(6, 0, [cls.tax_include_id.id])]))

        cls.product_id = product_tmpl_id.product_variant_id


    def test_sale_portal_proposal(self):
        pass
