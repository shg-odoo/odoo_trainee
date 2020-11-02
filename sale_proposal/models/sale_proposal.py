from odoo import api, models, fields

Class SaleProposal(models.Model):
    _name = "proposal.order"
    _inherit = ['portal.mixin', 'mail.thread',
                'mail.activity.mixin', 'utm.mixin']
    _discription = "Portal proposal"

    name = fields.Char(string='Portal Reference', required=True, copy=False, readonly=True, states={
                       'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    user_id = fields.Many2one(
        'res.users', string='Salesperson', index=True, tracking=2, default=lambda self: self.env.user,
        domain=lambda self: [('groups_id', 'in', self.env.ref('sales_team.group_sale_salesman').id)])
    partner_id = fields.Many2one(
        'res.partner', string='Customer', readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        required=True, change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)
    
    pricelist_id = fields.Many2one(
        'product.pricelist', string='Pricelist', check_company=True,  # Unrequired company
        required=True, readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", tracking=1,
        help="If you change the pricelist, only newly added lines will be affected.")

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('confirmed', 'Confirmed'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')