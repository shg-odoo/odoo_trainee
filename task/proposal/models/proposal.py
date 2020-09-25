from odoo import api, fields, models


class Order(models.Model):
    _name = "proposal.order"
    _description = "Order"

    customer_name = fields.Many2one('res.partner')
    proposal_date = fields.Date()
    product_line = fields.One2many('proposal.orderline', 'product', string="Product Id")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')])
    untaxed_amount = fields.Float()
    taxes = fields.Float()
    total_amount = fields.Float(string="Total")

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = False

        if force_confirmation_template or (self.state == 'sale' and not self.env.context.get('proforma', False)):
            template_id = int(self.env['ir.config_parameter'].sudo().get_param('sale.default_confirmation_template'))
            template_id = self.env['mail.template'].search([('id', '=', template_id)]).id
            if not template_id:
                template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.mail_template_sale_confirmation', raise_if_not_found=False)
        if not template_id:
            template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.email_template_edi_sale', raise_if_not_found=False)

        return template_id

    def send_email(self):
        self.ensure_one()
        template_id = self._find_mail_template()
        template = self.env['mail.template'].browse(template_id)
        context = {
            'default_model': 'proposal.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
        }

        return {
            'type': 'ir.actions.act_windows',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(template, 'form')],
            'view_id': False,
            'target': 'new',
            'context': context,
        }


class OrderLine(models.Model):
    _name = "proposal.orderline"

    product = fields.Many2one('proposal.order', string="Product Id")
    lable = fields.Text(string="Description")
    product_name = fields.Many2one('product.product', string='Product Name')
    proposed_quantity = fields.Integer()
    accepted_quantity = fields.Integer()
    accepted_price = fields.Float()
    proposed_price = fields.Float()
    subtotal = fields.Float(compute="subtotal_compute")

    def subtotal_compute(self):
        for record in self:
            record.subtotal = record.accepted_price * record.accepted_quantity

    @api.onchange('product_name')
    def set_price(self):
        product_info = self.env['product.product'].browse(self.product_name.id)
        self.proposed_price = product_info.list_price
        self.lable = str(product_info.description)

    def name_get(self):
        result = []
        for so_line in self.sudo():
            name = '%s - %s' % (so_line.order_id.name, so_line.name and so_line.name.split('\n')[0] or so_line.product_id.name)
            if so_line.order_partner_id.ref:
                name = '%s (%s)' % (name, so_line.order_partner_id.ref)
            result.append((so_line.id, name))
        return result
