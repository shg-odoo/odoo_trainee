from odoo import api, fields, models


class Order(models.Model):
    _name = "proposal.order"
    _description = "Order"
    _inherit = ['mail.thread', 'mail.activity.mixin', ]

    user_id = fields.Many2one('res.user')
    customer_name = fields.Many2one('res.partner')
    proposal_date = fields.Date()
    product_line = fields.One2many('proposal.orderline', 'product', string="Product Id")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')], default='draft')
    untaxed_amount = fields.Float()
    total = fields.Float(string="Total", compute="compute_total")
    total_amount_tax = fields.Float(compute="compute_total_tax_amount")

    def send_email(self):
        template_id = self.env.ref('proposal.email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
        return self.write({'state': 'sent'})

    def confirm_action(self):
        return self.write({'state': 'confirm', 'proposal_date': fields.Date.today()})

    def cancel_action(self):
        return self.write({'state': 'cancel'})

    @api.depends('product_line')
    def compute_total_tax_amount(self):
        for order in self:
            untaxed_amount = total_amount_tax = total = 0.0
            for line in self.product_line:
                untaxed_amount += line.product_subtotal
                total_amount_tax += line.product_tax
                print("&&&"*12, untaxed_amount)
                order.update({
                    'untaxed_amount': untaxed_amount,
                    'total_amount_tax': total_amount_tax,
                    'total': total_amount_tax+untaxed_amount
                })


class OrderLine(models.Model):
    _name = "proposal.orderline"

    product = fields.Many2one('proposal.order', string="Product Id")
    lable = fields.Text(string="Description")
    product_name = fields.Many2one('product.product', string='Product Name')
    proposed_quantity = fields.Integer(default="1")
    accepted_quantity = fields.Integer(default="1")
    proposed_price = fields.Float()
    accepted_price = fields.Float()
    product_tax = fields.Float()
    product_subtotal = fields.Float()

    @api.onchange('product_name')
    def set_price(self):
        product_info = self.env['product.product'].browse(self.product_name.id)
        self.proposed_price = product_info.list_price
        self.accepted_price = self.proposed_price
        self.lable = str(product_info.description)

    @api.onchange('accepted_price', 'accepted_quantity')
    def subtotal_compute(self):
            self.product_subtotal = self.accepted_price * self.accepted_quantity
            print("###"*10, self.product_subtotal)

    @api.onchange('product_subtotal')
    def _onchange_product_tax(self):
            self.product_tax = (self.product_subtotal * 10) / 100
            print("@@@@"*10, self.product_tax)
