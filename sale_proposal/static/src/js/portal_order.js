odoo.define('sale_proposal.portal_order', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    publicWidget.registry.WebsiteSalePayment = publicWidget.Widget.extend({
        selector: '.sale_tbody',
        events: {
            'click .plus_qunatity_class': '_plus_Click',
            'click .minus_qunatity_class': '_minus_Click',
            'change .accepted_quantity_by_cust,.accepted_price_by_cust': '_count_total_accepted_amount',
            'click .plus_qunatity_class,.minus_qunatity_class' : '_count_total_accepted_amount'
        },
        // To add quantity while customer clicks on plus button
        /**
         * @private
         * @param {MouseEvent} ev
         */
        _plus_Click: function (ev) {
            var line_id = ev.currentTarget.attributes.value.nodeValue
            if (line_id){
                var input_line_id = 'accepted_quantity-' + line_id
                var old_value = document.getElementById(input_line_id).value
                document.getElementById(input_line_id).value = parseFloat(old_value) + 1.0;
            }
            
        },
        // // To substract quantity while customer clicks on minus button
        /**
         * @private
         * @param {MouseEvent} ev
         */
        _minus_Click: function (ev) {
            var line_id = ev.currentTarget.attributes.value.nodeValue
            if (line_id){
                var input_line_id = 'accepted_quantity-' + line_id
                var old_value = document.getElementById(input_line_id).value
                if (old_value > 1){
                    document.getElementById(input_line_id).value = parseFloat(old_value) - 1.0;
            }
            }
            
        },
        // for count total amount and take updated values to backend
        /**
         * @private
         * @param {Event} ev
         */
        _count_total_accepted_amount : function(ev) {
            var customer_accepted_values = []
            var accepted_quantity = document.getElementsByClassName('accepted_quantity_by_cust')
            var accepted_price = document.getElementsByClassName('accepted_price_by_cust')
            var total = 0
            for (var i = 0; i < accepted_quantity.length; i++) {
                var line_total = 0
                var line_id = accepted_quantity[i].id.slice(-2)
                for (var j=0; j < accepted_price.length; j++){
                    if (accepted_price[j].id == line_id){
                        line_total = parseFloat(accepted_quantity[i].value) * parseFloat(accepted_price[j].value)
                        total = total + line_total
                        // Assigning update values to list for update in backend
                        var vals = {'line_id' : line_id,'qty_accepted' : accepted_quantity[i].value, 'price_accepted' : accepted_price[j].value}
                        customer_accepted_values.push(JSON.stringify(vals))
                    }
                }
              }

            var total_amount = document.getElementsByClassName('oe_currency_value')
            for (var total_amt = 0; total_amt < total_amount.length; total_amt++){
                total_amount[total_amt].innerHTML = total
            }
            document.getElementById('customer_accepted_values').value = customer_accepted_values
        }
    })
});