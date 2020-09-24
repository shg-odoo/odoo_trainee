from odoo import fields, models


class Order(models.Model):
    _name = "proposal.order"
    _description = "Order"

    customer_name = fields.Many2one('res.partner')
    proposal_date = fields.Date()
    product_line = fields.One2many('proposal.orderline', 'product', string="Product Id")
    description = fields.One2many('proposal.orderline', 'lable')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')])


class OrderLine(models.Model):
    _name = "proposal.orderline"

    product = fields.Many2one('proposal.order', string="Product Id")
    lable = fields.Many2one('description', string="Description")
    product_name = fields.Many2one('product.product', string='Product Name')
    proposed_quantity = fields.Integer(default='1')
    accepted_quantity = fields.Integer()
    accepted_price = fields.Float()
    proposed_price = fields.Float()
    subtotal = fields.Float(compute="subtotal_compute")

    def subtotal_compute(self):
        for record in self:
            record.subtotal = record.accepted_price * record.accepted_quantity
