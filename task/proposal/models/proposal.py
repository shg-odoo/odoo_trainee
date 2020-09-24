from odoo import fields, models


class Order(models.Model):
    _name = "proposal.order"
    _description = "Order"

    customer_name = fields.Many2one('res.partner')
    proposal_date = fields.Date()


class OrderLine(models.Model):
    _name = "proposal.orderline"

    product_id = fields.Many2one('product.product')
