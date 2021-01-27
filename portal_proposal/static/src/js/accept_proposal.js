odoo.define('portal_proposal.proposal_page_template', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
const session = require('web.session');
var ajax = require('web.ajax');


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
        var pr_table = document.getElementById('pr_table');
        for (var i = 1; i < pr_table.rows.length; i++) { 
            if (pr_table.rows[i].cells[4].children[0] && pr_table.rows[i].cells[6].children[0] && pr_table.rows[i].cells[1].children[1]) {
                var qty = pr_table.rows[i].cells[4].children[0].value;
                pr_table.rows[i].cells[4].children[0].setAttribute('readonly', 'True');
                var price = pr_table.rows[i].cells[6].children[0].value;  
                pr_table.rows[i].cells[6].children[0].setAttribute('readonly', 'True');
                var prod = pr_table.rows[i].cells[1].children[1].value;
                qty_lst.push({prod,qty});
                price_lst.push({prod,price});
            }      
        }
        document.getElementById('acc_btn').setAttribute('hidden', 'True');
        document.getElementById('rej_btn').setAttribute('hidden', 'True');
        document.getElementById('success_div').className += 'alert alert-success text-center';
        document.getElementById('success_div').innerHTML = "<p><strong>The proposal has been accepted.</strong></p>";

        return this._rpc({
            route: '/proposal/accept',
            params: {
                qty_list: qty_lst,
                price_list: price_lst,
                pro_id: document.getElementById('proposalId').value,
                token: document.getElementById('proposalToken').value,
            },
        });
    },

    _reject_data: function() {
        document.getElementById('acc_btn').setAttribute('hidden', 'True');
        document.getElementById('rej_btn').setAttribute('hidden', 'True');
        return this._rpc({
            route: '/proposal/reject',
            params: {                
                pro_id: document.getElementById('proposalId').value,
                token: document.getElementById('proposalToken').value,
            },
        });       
    }
    
});

    if (document.getElementById("pr_table") != null) {
        document.getElementById("pr_table").addEventListener('input', function onchange_sum(e) {
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