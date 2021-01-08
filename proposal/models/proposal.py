from odoo import api, fields, models, _


class Proposal(models.Model):
    _name = "proposal.proposal"
    _inherit = ['mail.thread','portal.mixin','mail.activity.mixin']
    _description = "Manage Proposal" 
    _rec_name = "customer_id"

    seq = fields.Char(string="Number", readonly="True")
    proposal_date = fields.Date(string="Proposal Date", default=fields.Datetime.now, required=True)
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    salesman_id = fields.Many2one("res.users",string="Sales Person", default =lambda self: self.env.user, required=True)
    proposal_line_ids = fields.One2many("proposal.line", "proposal_id")
    state = fields.Selection([('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')],default="draft", string="Status")
    proposed_total_price = fields.Float(compute = '_compute_proposed_total', default = 0.0, store=True, readonly=True, string="Proposed Total")
    accepted_total_price = fields.Float(compute = '_compute_accepted_total', default = 0.0, store=True, readonly=True, string="Accepted Total")
    proposal_status = fields.Selection([('accept', 'Accepted'),
        ('reject', 'Rejected'),
        ('no_response', 'No Response')],default="no_response")


    @api.model
    def create(self, values):
            if values.get('seq', _('New')) == _('New'):
                values['seq'] = self.env['ir.sequence'].next_by_code('proposal.proposal') or _('New')
            crt = super(Proposal, self).create(values)
            return crt

    @api.depends('proposal_line_ids')
    def _compute_proposed_total(self):
        proposed_total = []
        if self.proposal_line_ids:
            for line in self.proposal_line_ids:
                line.proposed_sub_total = line.qty_proposed * line.price_proposed
                proposed_total.append(line.proposed_sub_total)
            self.proposed_total_price = sum(proposed_total)

    @api.depends('proposal_line_ids')
    def _compute_accepted_total(self):
        total = []
        if self.proposal_line_ids:
            for line in self.proposal_line_ids:
                line.accepted_sub_total = line.qty_accepted * line.price_accepted
                total.append(line.accepted_sub_total)    
            self.accepted_total_price = sum(total)

    def action_proposal_mail_send(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('proposal', 'email_template')[1]
            print("$$$"*20, template_id)
        except ValueError:
            template_id = False
        ctx = {
            'default_model': 'proposal.proposal',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    def action_proposal_mail_send(self):
        self.state = "sent"

    # def action_proposal_mail_send(self):
    #     self.state = "sent"            
    #     template_id = self.env.ref('sale_proposal.email_template_proposal_mail').id
    #     self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)

    def action_confirmed_proposal(self):
        self.state = "confirmed"
        sale_order_line_ids = []
        sale_order_tuple_line_ids = ()
        for rec in self:
            for line in rec.proposal_line_ids:
                sale_order_list_line_ids = [0,0]
                sale_order_list_line_ids.append(({'product_id':line.product_id.id,'name':line.description,'product_uom_qty':line.qty_accepted,'price_unit':line.price_accepted}))
                sale_order_tuple_line_ids = tuple(sale_order_list_line_ids)
                sale_order_line_ids.append(sale_order_tuple_line_ids)    
        self.env['sale.order'].create({'partner_id':self.customer_id.id,'order_line':sale_order_line_ids,'state':'sale'})

    def action_confirmed_proposal(self):
        # self.write({'state': 'confirmed'})
        self.state = "confirmed"

    def action_cancel_proposal(self):
        self.state = "cancel"

    def preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': f'/my/proposals/{self.id}'
        }


class ProposalLine(models.Model):
    _name = "proposal.line"
    _description = "Proposal Line" 
    _rec_name = "product_id"

    proposal_id = fields.Many2one("proposal.proposal", string="Proposal Id")
    product_id = fields.Many2one("product.product")
    product_id = fields.Many2one("product.product", string="Product", required=True)
    description = fields.Text()
    qty_proposed = fields.Integer(string="Proposed Quantity", required=True, default=1)
    price_proposed = fields.Char(string=" Price Proposed(per unit)")
    qty_accepted = fields.Integer(default=1)
    price_accepted = fields.Float(string="Accepted Price(per unit)")
    proposed_sub_total = fields.Float(default = 0.0, readonly=True)
    accepted_sub_total = fields.Float(default = 0.0, readonly=True)

    @api.onchange('price_proposed', 'qty_proposed')
    def accepted_price_qty_change(self):
        self.qty_accepted = self.qty_proposed
        self.price_accepted = self.price_proposed 

    @api.onchange('product_id')
    def DEscription_change(self):
        self.description = self.product_id.name