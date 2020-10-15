from odoo import models, fields, api, exceptions,_


class Proposals(models.Model):
    _name = 'proposals.proposals'
    _description = "Sales Proposal"
    _inherit = ['mail.thread']

    def action_sent_proposal(self):
        self.state = "sent"
        # self.env['mail.template'].browse('proposal_email_template').send_mail({})

    def action_confirmed_proposal(self):
        self.state = "confirmed"
        sale_order_line_ids = []
        sale_order_list_line_ids = []
        sale_order_tuple_line_ids = (0,0)
        for rec in self:
            sale_order_list_line_ids.append((0, 0,{'product_id':rec.proposal_line_ids.product_id.id,'name':rec.proposal_line_ids.description,'product_uom_qty':rec.proposal_line_ids.qty_accepted,'price_unit':rec.proposal_line_ids.price_accepted}))
        self.env['sale.order'].create({'partner_id':self.customer_id.id,'order_line':sale_order_line_ids})

    proposal_name = fields.Char( default=" ")
    sales_man_id = fields.Many2one("res.users",string="Salesman")
    customer_id = fields.Many2one("res.partner")
    price_list = fields.Many2one("product.pricelist")
    proposal_line_ids = fields.One2many("proposals.line", 'proposal_id')
    state = fields.Selection([('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')],default="draft")
    date_time = fields.Datetime(default=fields.Datetime.now, readonly = True)
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    

class ProposaLisList(models.Model):
    _name = 'proposals.line'

    product_id = fields.Many2one("product.product")
    description = fields.Text()
    qty_proposed = fields.Integer()
    price_proposed = fields.Float()
    qty_accepted = fields.Integer()
    price_accepted = fields.Float()
    proposal_id = fields.Many2one("proposals.proposals")