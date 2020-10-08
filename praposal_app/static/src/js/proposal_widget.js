odoo.define('praposal_order.ProposalWidget', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    var ProposalSidebar = require('portal.PortalSidebar');
    publicWidget.registry.ProposalWidget = ProposalSidebar.extend({
    selector: '.proposal_content',
    events: {
        'click .plus': '_on_Plus',
        'click .minus': '_on_Minus',

    },

    /**
     * Hook for proposal_order_portal_content based configurators
     * (add accepted product qty).
     *
     * @private
     */
    _on_Plus: function (ev){
        var $alltdplus = $(ev.currentTarget);
        var $input_value = $alltdplus.closest('.number').find("input");
        var count = parseInt($input_value.val()) + 1;
        count = count < 1 ? 1 : count;
        $input_value.val(count);
        },

    /**
     * Hook for proposal_order_portal_content based configurators
     * (remove accepted product qty).
     *
     * @private
     */    
    _on_Minus: function (ev) {
        var $alltdplus = $(ev.currentTarget);
        var $input_value = $alltdplus.closest('.number').find("input");
        var count = parseInt($input_value.val()) - 1;
        count = count < 1 ? 1 : count;
        $input_value.val(count);
        },  

    
    })
});    

odoo.define('praposal_order.ProposalacceptWidget', function (require) {
    "use strict";

    var proposalAcceptWidget = require('web.public.widget');
    var ProposalAccept = require('portal.PortalSidebar');
    var ajax = require('web.ajax');
    var rpc = require('web.rpc');

    proposalAcceptWidget.registry.ProposalacceptWidget = ProposalAccept.extend({
    selector: '.accept_reject_content',
    events: {
        'click .accept_btn': '_on_AcceptBtn',
        'click .reject_btn': '_on_RejectBtn'

    },
    /**
     * Hook for proposal_order_portal_template based configurators
     * (Button to Accept Proposal).
     *
     * @private
     */    
    _on_AcceptBtn: function () { 

        $("#buttons_id").hide();
        var dataarray  =[];
        var qty,price,line_id,state;
        var acc_qty = document.getElementsByClassName('accept_qty');
        var acc_price = document.getElementsByClassName('accept_price');
        var rec_id = document.getElementsByClassName("record_id")[0].value
        var access_token = new URLSearchParams(window.location.search).get('access_token');
        for (var i = 0; i < acc_qty.length; i++) {
            var qtyobj = acc_qty[i];
            var priceobj =acc_price[i]
            qty = qtyobj.value
            price = priceobj.value;
            line_id = qtyobj.getAttribute('line_id')
            dataarray.push({
                    'rec_id' : rec_id,
                    'line_id' : line_id,
                    'qty_acept': qty,
                    'price_acept': price,
                })
        }
            ajax.jsonRpc('/proposal/accepted/', 'call', { 'data' : dataarray,'access_token':access_token }).then(function (url){})
            },
    /**
     * Hook for proposal_order_portal_template based configurators
     * (Button to Reject Proposal).
     *
     * @private
     */            
    _on_RejectBtn:function () {

        var rec_id = document.getElementsByClassName("record_id")[0].value
        if (confirm("Are You Sure...")) {
            ajax.jsonRpc('/proposal/rejected/', 'call',{'record_id':rec_id}).then(function (url){})
            $("#buttons_id").hide()
        } 

    }

    })
})