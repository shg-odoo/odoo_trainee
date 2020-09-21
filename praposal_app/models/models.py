# -*- coding: utf-8 -*
from odoo import models, fields, api, _
from datetime import datetime, timedelta
from odoo.addons import decimal_precision as dp


class Proposal(models.Model):
    _name = 'proposal.order'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = 'Proposal'


    name = fields.Char(string="Proposal No", required=True, copy=False, store=True,
                        readonly=True, index=True, default=lambda self: _('New'))
    proposal_line= fields.One2many('proposal.order.line',"proposal_id",string="Proposal Lines")
    date_order = fields.Datetime(string='Proposal Date', required=True, readonly=True, index=True ,default=fields.Datetime.now)
    total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', track_visibility='always')   
    note =fields.Text('Note')
    state = fields.Selection(string="Status", selection=[('draft','Draft'),('sent','Sent'),('confirm','Confirmed'),('cancel','Cancel')], default="draft")
    confirm_date = fields.Datetime(string='Confirm Date')
    types_name = fields.Char('Types Name', compute='_compute_types_name')
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, required=True, change_default=True, index=True, track_visibility='always', track_sequence=1)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env['res.company']._company_default_get('proposal.order'))
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist',readonly=True,)
    currency_id = fields.Many2one("res.currency", related='company_id.currency_id', string="Currency", readonly=True, )
    amount_tax = fields.Float(string='Taxes', store=True, readonly=True, compute='_amount_all')
    amount_untaxed = fields.Monetary(string='Untaxed Amount', store=True, readonly=True, compute='_amount_all', track_visibility='onchange', track_sequence=5)
    


    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('proposal.order') or _('New')
        return super(Proposal, self).create(vals)

    
    @api.depends('proposal_line.price_subtotal')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.proposal_line:
                amount_untaxed+=line.price_subtotal
                amount_tax+=line.price_tax
            order.update({
                'amount_untaxed':amount_untaxed,
                'amount_tax':amount_tax,
                'total':amount_untaxed +amount_tax
                })

    @api.multi
    def action_sent(self):
        return self.write({'state': 'sent'})

    @api.multi
    def action_confirm(self):
        return self.write(
            {'state': 'confirm',
            'confirm_date': fields.Datetime.now(),
            }) 

    @api.multi
    def action_cencle(self):
        return self.write({'state': 'cancel'})


    def preview_proposal_order(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    def _compute_access_url(self):
        super(Proposal, self)._compute_access_url()
        for order in self:
            order.access_url = '/my/proposal/%s' % (order.id)


    @api.multi
    @api.depends('state')
    def _compute_types_name(self):
        for record in self:
            record.types_name = _('Proposal') if record.state in ('draft', 'sent', 'cancel') else _('Proposal Order')


    @api.multi
    def action_proposal_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('proposal', 'email_template_edi_sale')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        lang = self.env.context.get('lang')
        template = template_id and self.env['mail.template'].browse(template_id)
        if template and template.lang:
            lang = template._render_template(template.lang, 'proposal.order', self.ids[0])
        ctx = {
            'default_model': 'proposal.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'model_description': self.with_context(lang=lang).types_name,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }       
    
    
    @api.multi
    def force_proposal_send(self):
        for order in self:
            email_act = order.action_proposal_send()
            if email_act and email_act.get('context'):
                email_ctx = email_act['context']
                email_ctx.update(default_email_from=order.company_id.email)
                order.with_context(**email_ctx).message_post_with_template(email_ctx.get('default_template_id'))
        return True



class Proposallines(models.Model):
    _name = 'proposal.order.line'
    _description = 'Proposal Lines'

    proposal_id = fields.Many2one('proposal.order','Proposal Id')
    product = fields.Many2one('product.product','Products')
    name = fields.Char("Description")
    qty_propos = fields.Integer("Proposed Quantity",default=1)
    price_propos = fields.Float("Price Proposed",default=0.0)
    qty_acept = fields.Integer("Qty Accepted")
    price_acept = fields.Float("Price Accepted",default=0.0)
    price_subtotal = fields.Float(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_tax = fields.Float(compute='_compute_amount', string='Total Tax', readonly=True, store=True)
  
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False, help="Technical field for UX purpose.")

    @api.depends('qty_propos','price_propos')
    def _compute_amount(self):
        price_sub = 0.0
        for line in self:
            price_sub =line.qty_propos * line.price_propos
            line.update({
                    'price_subtotal': price_sub
            })


    @api.onchange('product')
    def _onchange_price(self):
        price_obj = self.env['product.product'].browse(self.product.id)
        self.price_propos=price_obj.list_price
                