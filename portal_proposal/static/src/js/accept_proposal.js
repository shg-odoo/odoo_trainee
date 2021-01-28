odoo.define('portal_proposal.proposal_page_template', function (require) {
'use strict';

var publicWidget = require('web.public.widget');


publicWidget.registry.ProposalPage = publicWidget.Widget.extend({
    selector: '.oe_proposal_form',
    events: {        
        'click .accept_data': '_accept_data', 
        'click .reject_data': '_reject_data',
    },

    _accept_data: function() {
        var self = this;
        var qty_lst = [];
        var price_lst = [];
        
        $('table > tbody  > tr').each(function(index, tr) {     
            var prod = $('#productId', tr).val();        
            var qty = $('#qty', tr).val();
            $( "#qty", tr ).replaceWith( "<p>" + qty + "</p>" );
            var price = $('#price', tr).val();
            $('#price', tr).replaceWith( "<p>" + price + "</p>" );
            if (qty != undefined && price != undefined) {
                qty_lst.push({prod,qty});
                price_lst.push({prod,price}); 
            }            
        });  
        $('#acc_btn').hide();
        $('#rej_btn').hide();
           
        $("#success_div").addClass("alert alert-success text-center");
        $("#success_div").html("<p><strong>The proposal has been accepted.</strong></p>");

        return this._rpc({
            route: '/proposal/accept',
            params: {
                qty_list: qty_lst,
                price_list: price_lst,
                pro_id: $('#proposalId').val(),
                token: $('#proposalToken').val(),
            },
        });
    },

    _reject_data: function() {
        $('#acc_btn').hide();
        $('#rej_btn').hide();
        return this._rpc({
            route: '/proposal/reject',
            params: {                
                pro_id: $('#proposalId').val(),
                token: $('#proposalToken').val(),
            },
        });       
    }
    
});

    if (document.getElementById('pr_table') != null) {
        document.getElementById('pr_table').addEventListener('input', function onchange_sum(e) {
        var sum = 0;
        var qty = 0;
        var res = 0;
        const inputs = document.querySelectorAll('input[name=price_accepted]');
        const qty_inputs = document.querySelectorAll('input[name=qty_accepted]');
        const tot = document.getElementById('total_acc_amt');
        for (var qty_input in qty_inputs) {
            for (var input in inputs) {
                if (qty_input == input) {
                    if (qty_inputs[qty_input].textContent != undefined || !isNaN(qty_inputs[qty_input].value) || inputs[input].textContent != undefined || !isNaN(inputs[input].value)) {
                        qty = parseInt(qty_inputs[qty_input].value);
                        sum = parseFloat(inputs[input].value);
                        res += qty * sum;
                    }
                }
            }
        }        
        
        tot.textContent = res;
    });
    }
});