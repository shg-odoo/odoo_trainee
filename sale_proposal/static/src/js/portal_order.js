odoo.define('sale_proposal.portal_order', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    publicWidget.registry.WebsiteSalePayment = publicWidget.Widget.extend({
        selector: '.sale_tbody',
        events: {
            'click .plus_qunatity_class': '_plus_Click',
            'click .minus_qunatity_class': '_minus_Click',
            'change .accepted_quantity_by_cust,.accepted_price_by_cust': '_test',
            'click .plus_qunatity_class,.minus_qunatity_class' : '_test'
        },
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
        /**
         * @private
         * @param {Event} ev
         */
        _test : function(ev) {
            var accepted_quantity = document.getElementsByClassName('accepted_quantity_by_cust')
            var accepted_price = document.getElementsByClassName('accepted_price_by_cust')
            console.log(accepted_quantity,"this is accepted quantity!!!")
            console.log(accepted_price,"this is accepted price!!!")
            var total = 0
            for (var i = 0; i < accepted_quantity.length; i++) {
                var line_total = 0
                var line_id = accepted_quantity[i].id.slice(-2)
                for (var j=0; j < accepted_price.length; j++){
                    if (accepted_price.id == line_id){
                        line_total = line_total + accepted_price.value
                        total = total + line_total
                    }
                }
              }
            console.log(total,"this is tot")
        }
    })
});