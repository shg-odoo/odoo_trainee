odoo.define('sale_portal_proposal.sale_portal_proposal', function (require) {
'use strict';
var publicWidget = require('web.public.widget');

publicWidget.registry.SaleProposalUpdateLineButton = publicWidget.Widget.extend({
    selector: '.o_portal_sale_proposal_sidebar',
    events: {
        'click a.js_update_line_json': '_onClick',
        'change .o_input': '_onChangePrice',
        'click #accept_button': '_onClickAcceptReject',
        'click #reject_button': '_onClickAcceptReject',
    },
    /**
     * @override
     */
    async start() {
        await this._super(...arguments);
        this.orderDetail = this.$el.find('table#sales_order_table').data();
        this.elems = this._getUpdatableElements();
    },
    /**
     * Reacts to the Accept/Reject Proposal
     *
     * @param {Event} ev
     */

     _onClickAcceptReject(ev) {
        ev.preventDefault();
        let self = this,
            $target = $(ev.currentTarget)
        return this._rpc({
            route: "/my/proposals/" + self.orderDetail.orderId + "/accept_proposal",
            params: {
                    'access_token': self.orderDetail.token,
                    'accept' : $target.data('accept'),
                    'reject' : $target.data('reject'),
            }
        });
     },
    /**
     * Reacts to the change price
     *
     * @param {Event} ev
     */

    _onChangePrice(ev) {
        ev.preventDefault();
        let self = this,
            $target = $(ev.currentTarget),
            $price = parseFloat($target.val())
        this._callUpdateLineRoute(self.orderDetail.orderId, {
            'line_id': $target.data('lineId'),
            'price'  : $price,
            'access_token': self.orderDetail.token
        }).then((data) => {
            var $saleTemplate = $(data['sale_template']);
//            self._updateOrderLineValues($target.closest('tr'), data);
            self._updateOrderValues(data);
        });

    },

    /**
     * Reacts to the click on the -/+ buttons
     *
     * @param {Event} ev
     */
    _onClick(ev) {
        ev.preventDefault();
        let self = this,
            $target = $(ev.currentTarget),
            $targetinput = $target.closest('tr').find('.js_quantity'),
            $remove = $target.data('remove'),
            $add= $target.data('add'),
            $qty = parseFloat($targetinput.val());
        if ($add && $add !== undefined) {
            $targetinput.val($qty + 1)
        }
        if ($remove && $remove !== undefined) {
            $targetinput.val($qty - 1)
        }
        this._callUpdateLineRoute(self.orderDetail.orderId, {
            'line_id': $target.data('lineId'),
            'remove': $target.data('remove'),
            'access_token': self.orderDetail.token
        }).then((data) => {
            var $saleTemplate = $(data['sale_template']);
//            self._updateOrderLineValues($target.closest('tr'), data);
            self._updateOrderValues(data);
        });
    },
    /**
     * Calls the route to get updated values of the line and order
     * when the quantity of a product has changed
     *
     * @private
     * @param {integer} proposal_id
     * @param {Object} params
     * @return {Deferred}
     */
    _callUpdateLineRoute(proposal_id, params) {
        return this._rpc({
            route: "/my/proposals/" + proposal_id + "/update_proposals_line_dict",
            params: params,
        });
    },
    /**
     * Processes data from the server to update the UI
     *
     * @private
     * @param {Object} data: contains order and line updated values
     */
    _updateOrderValues(data) {
        let orderAmountTotal = data.order_amount_total,
            orderAmountUntaxed = data.order_amount_untaxed,
            $orderTotalsTable = $(data.order_totals_table);
        if (orderAmountUntaxed !== undefined) {
            this.elems.$orderAmountUntaxed.text(orderAmountUntaxed);
        }

        if (orderAmountTotal !== undefined) {
            this.elems.$orderAmountTotal.text(orderAmountTotal);
        }
        if ($orderTotalsTable.length) {
            this.elems.$orderTotalsTable.find('table').replaceWith($orderTotalsTable);
        }
    },
    /**
     * Locate in the DOM the elements to update
     * Mostly for compatibility, when the module has not been upgraded
     * In that case, we need to fall back to some other elements
     *
     * @private
     * @return {Object}: Jquery elements to update
     */
    _getUpdatableElements() {
        let $orderAmountUntaxed = $('[data-id="total_untaxed"]').find('span, b'),
            $orderAmountTotal = $('[data-id="total_amount"]').find('span, b')


        if (!$orderAmountUntaxed.length) {
            $orderAmountUntaxed = $orderAmountTotal.eq(1);
            $orderAmountTotal = $orderAmountTotal.eq(0).add($orderAmountTotal.eq(2));
        }

        return {
            $orderAmountUntaxed: $orderAmountUntaxed,
            $orderAmountTotal: $orderAmountTotal,
            $orderTotalsTable: $('#total'),
        };
    }
});
});