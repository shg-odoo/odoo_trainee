from odoo import models, fields, api, exceptions,_


class Proposal(models.Model):
    _name = 'proposals.proposals'
    _description = "Sales Proposal"
    _inherit = ['mail.thread']


    def action_proposal_mail_send(self):
        self.state = "sent"
        self.ensure_one()
        
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data.get_object_reference('proposal_week_2', 'email_template_proposal_mail')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        template = template_id and self.env['mail.template'].browse(template_id)
        ctx={}
        ctx.update({
            'default_model': 'proposals.proposals',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            
        })
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
    
    def action_cancel_proposal(self):
        self.state = "cancel"

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

    @api.model
    def create(self, vals):
        if vals.get('proposal_name', _('New')) == _('New'):
            seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.now())
            vals['proposal_name'] = self.env['ir.sequence'].next_by_code('proposals.proposals', sequence_date=seq_date) or _('New')
        result = super(Proposal, self).create(vals)
        return result
    
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

    def preview_proposal(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': self.get_portal_url(),
        }

    proposal_name = fields.Char(default=lambda self: _('New'), readonly = True)
    sales_man_id = fields.Many2one("res.users",string="Salesman", default =lambda self: self.env.user, readonly = True)
    customer_id = fields.Many2one("res.partner", required=True)
    price_list_id = fields.Many2one("product.pricelist", required=True)
    proposal_line_ids = fields.One2many("proposals.line", 'proposal_id')
    state = fields.Selection([('draft','Draft'),
        ('sent','Sent'),
        ('confirmed','Confirmed'),
        ('cancel','Cancel')],default="draft")
    proposed_total_price = fields.Float(compute = '_compute_proposed_total', default = 0.0, store=True, readonly=True)
    accepted_total_price = fields.Float(compute = '_compute_accepted_total', default = 0.0, store=True, readonly=True)
    proposal_date = fields.Datetime(default = fields.Datetime.now)
    fiscal_position_id = fields.Many2one(
        'account.fiscal.position', string='Fiscal Position')
    partner_shipping_id = fields.Many2one(
        'res.partner')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True, default=lambda self: self.env.company)
    
class ProposaLisList(models.Model):
    _name = 'proposals.line'

    @api.onchange('product_id')
    def product_id_change(self):
        if not self.product_id:
            return
        valid_values = self.product_id.product_tmpl_id.valid_product_template_attribute_line_ids.product_template_value_ids
        # remove the is_custom values that don't belong to this template
        for pacv in self.product_custom_attribute_value_ids:
            if pacv.custom_product_template_attribute_value_id not in valid_values:
                self.product_custom_attribute_value_ids -= pacv

        # remove the no_variant attributes that don't belong to this template
        for ptav in self.product_no_variant_attribute_value_ids:
            if ptav._origin not in valid_values:
                self.product_no_variant_attribute_value_ids -= ptav

        vals = {}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['qty_proposed'] = self.qty_proposed or 1.0

        product = self.product_id.with_context(
            partner=self.proposal_id.customer_id,
            quantity=vals.get('qty_proposed') or self.qty_proposed,
            date=self.proposal_id.proposal_date,
            pricelist=self.proposal_id.price_list_id.id,
            uom=self.product_uom.id
        )

        vals.update(description=self.get_proposal_line_multiline_description_sale(product))

        self._compute_tax_id()

        if self.proposal_id.price_list_id and self.proposal_id.customer_id:
            vals['price_proposed'] = self.env['account.tax']._fix_tax_included_price_company(self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)
        self.update(vals)

        title = False
        message = False
        result = {}
        warning = {}
        if product.sale_line_warn != 'no-message':
            title = _("Warning for %s") % product.name
            message = product.sale_line_warn_msg
            warning['title'] = title
            warning['message'] = message
            result = {'warning': warning}
            if product.sale_line_warn == 'block':
                self.product_id = False

        return result

    def get_proposal_line_multiline_description_sale(self, product):
        print("=1=1=1=1=1=1=1==1=1=1=1")
        return product.get_product_multiline_description_sale() + self._get_proposal_line_multiline_description_variants()

    def _get_proposal_line_multiline_description_variants(self):
        print("2=2=2=2=2=2=2=2=2==2=2=")
        if not self.product_custom_attribute_value_ids and not self.product_no_variant_attribute_value_ids:
            return ""

        description = "\n"

        custom_ptavs = self.product_custom_attribute_value_ids.custom_product_template_attribute_value_id
        no_variant_ptavs = self.product_no_variant_attribute_value_ids._origin

        # display the no_variant attributes, except those that are also
        # displayed by a custom (avoid duplicate description)
        for ptav in (no_variant_ptavs - custom_ptavs):
            description += "\n" + ptav.with_context(lang=self.proposal_id.customer_id.lang).display_name

        # display the is_custom values
        for pacv in self.product_custom_attribute_value_ids:
            description += "\n" + pacv.with_context(lang=self.proposal_id.customer_id.lang).display_name

        return description
    
    def _compute_tax_id(self):
        print("3=3=3=3=3==3=3=3=3==3")
        for line in self:
            fpos = line.proposal_id.fiscal_position_id or line.proposal_id.customer_id.property_account_position_id
            # If company_id is set in the order, always filter taxes by the company
            taxes = line.product_id.taxes_id.filtered(lambda r: r.company_id == line.proposal_id.company_id)
            line.tax_id = fpos.map_tax(taxes, line.product_id, line.proposal_id.partner_shipping_id) if fpos else taxes

    @api.onchange('product_uom', 'qty_proposed')
    def product_uom_change(self):
        print("4=4=4=4==4=4==4=4=4=")
        # if not self.product_uom or not self.product_id:
        #     print("4=4=4=4==4=4==4=4=4=",self.product_uom)
        #     self.price_proposed = 0.0
        #     return
        if self.proposal_id.price_list_id and self.proposal_id.customer_id:
            product = self.product_id.with_context(
                lang=self.proposal_id.customer_id.lang,
                partner=self.proposal_id.customer_id,
                quantity=self.qty_proposed,
                date=self.proposal_id.proposal_date,
                pricelist=self.proposal_id.price_list_id.id,
                uom=self.product_uom.id,
                fiscal_position=self.env.context.get('fiscal_position')
            )
            print("====11111111111111111111111================")
            self.price_proposed = self.env['account.tax']._fix_tax_included_price_company(self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)

    def _get_display_price(self, product):
        print("====================")
        no_variant_attributes_price_extra = [
            ptav.price_extra for ptav in self.product_no_variant_attribute_value_ids.filtered(
                lambda ptav:
                    ptav.price_extra and
                    ptav not in product.product_template_attribute_value_ids
            )
        ]
        if no_variant_attributes_price_extra:
            product = product.with_context(
                no_variant_attributes_price_extra=tuple(no_variant_attributes_price_extra)
            )

        if self.proposal_id.price_list_id.discount_policy == 'with_discount':
            return product.with_context(pricelist=self.proposal_id.price_list_id.id).price
        product_context = dict(self.env.context, partner_id=self.proposal_id.customer_id.id, date=self.proposal_id.proposal_date, uom=self.product_uom.id)

        final_price, rule_id = self.proposal_id.price_list_id.with_context(product_context).get_product_price_rule(product or self.product_id, self.qty_proposed or 1.0, self.proposal_id.customer_id)
        base_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id, self.qty_proposed, self.product_uom, self.proposal_id.price_list_id.id)
        if currency != self.proposal_id.price_list_id.currency_id:
            base_price = currency._convert(
                base_price, self.proposal_id.price_list_id.currency_id,
                self.proposal_id.company_id or self.env.company, self.proposal_id.proposal_date or fields.Date.today())
        # negative discounts (= surcharge) are included in the display price
        return max(base_price, final_price)



    def _get_real_price_currency(self, product, rule_id, qty, uom, pricelist_id):
        print("5=5=5=5=5==5=5=5==5=5=")
        PricelistItem = self.env['product.pricelist.item']
        field_name = 'lst_price'
        currency_id = None
        product_currency = product.currency_id
        if rule_id:
            pricelist_item = PricelistItem.browse(rule_id)
            if pricelist_item.pricelist_id.discount_policy == 'without_discount':
                while pricelist_item.base == 'pricelist' and pricelist_item.base_pricelist_id and pricelist_item.base_pricelist_id.discount_policy == 'without_discount':
                    price, rule_id = pricelist_item.base_pricelist_id.with_context(uom=uom.id).get_product_price_rule(product, qty, self.order_id.partner_id)
                    pricelist_item = PricelistItem.browse(rule_id)

            if pricelist_item.base == 'standard_price':
                field_name = 'standard_price'
                product_currency = product.cost_currency_id
            elif pricelist_item.base == 'pricelist' and pricelist_item.base_pricelist_id:
                field_name = 'price'
                product = product.with_context(pricelist=pricelist_item.base_pricelist_id.id)
                product_currency = pricelist_item.base_pricelist_id.currency_id
            currency_id = pricelist_item.pricelist_id.currency_id

        if not currency_id:
            currency_id = product_currency
            cur_factor = 1.0
        else:
            if currency_id.id == product_currency.id:
                cur_factor = 1.0
            else:
                cur_factor = currency_id._get_conversion_rate(product_currency, currency_id, self.company_id or self.env.company, self.order_id.date_order or fields.Date.today())

        product_uom = self.env.context.get('uom') or product.uom_id.id
        if uom and uom.id != product_uom:
            # the unit price is in a different uom
            uom_factor = uom._compute_price(1.0, product.uom_id)
        else:
            uom_factor = 1.0

        return product[field_name] * uom_factor * cur_factor, currency_id

    def _get_protected_fields(self):
        return [
            'product_id', 'description', 'price_proposed', 'product_uom', 'qty_proposed',
            'tax_id', 'analytic_tag_ids'
        ]

    @api.onchange('price_proposed', 'qty_proposed')
    def accepted_price_qty_change(self):
        self.qty_accepted = self.qty_proposed
        self.price_accepted = self.price_proposed 

    product_id = fields.Many2one("product.product")
    description = fields.Text()
    qty_proposed = fields.Integer(default=1)
    price_proposed = fields.Float("Price Proposes(per unit)", digits='Product Price')
    qty_accepted = fields.Integer(default=1)
    price_accepted = fields.Float("Price Accepted(per unit)")
    proposal_id = fields.Many2one("proposals.proposals")
    proposed_sub_total = fields.Float(default = 0.0, readonly=True)
    accepted_sub_total = fields.Float(default = 0.0, readonly=True)
    product_custom_attribute_value_ids = fields.One2many('product.attribute.custom.value', 'sale_order_line_id', string="Custom Values", copy=True)
    product_no_variant_attribute_value_ids = fields.Many2many('product.template.attribute.value', string="Extra Values", ondelete='restrict')
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', domain="[('category_id', '=', product_uom_category_id)]")
    company_id = fields.Many2one(related='proposal_id.company_id', string='Company', store=True, readonly=True, index=True)
    tax_id = fields.Many2many('account.tax', string='Taxes')
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id', readonly=True)
    analytic_line_ids = fields.One2many('account.analytic.line', 'so_line', string="Analytic lines")
    