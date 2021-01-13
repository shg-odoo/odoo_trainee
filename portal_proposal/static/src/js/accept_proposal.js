odoo.define('portal_proposal.proposal_page_template', function (require) {
'use strict';

var publicWidget = require('web.public.widget');


publicWidget.registry.ProposalPage = publicWidget.Widget.extend({
    selector: '.oe_proposal_form',
    events: {        
        'click .accept_data': '_accept_data', 
    },

    _accept_data: function() {
        var self = this;
        /*console.log("VAL..",this.$el.html(''));*/
        var qty_lst = [];
        var price_lst = [];
        var pr_table = document.getElementById('pr_table');
        for (var i = 1; i < pr_table.rows.length; i++) {        
            var qty = pr_table.rows[i].cells[4].children[0].value;
            var price = pr_table.rows[i].cells[6].children[0].value;  
            var prod = pr_table.rows[i].cells[1].children[1].value;
            qty_lst.push({prod,qty});
            price_lst.push({prod,price});      
        }

    	return this._rpc({
                model: 'portal.proposal',
                method: 'accept_qty_price',
                args: [qty_lst,price_lst,document.getElementById('proposalId').value],
            }).then(function (data) {
                self.data = data;
            }); 
    }
    
});

    if (document.getElementById("pr_table") != null) {
        document.getElementById("pr_table").addEventListener('input', function onchange_sum(e) {
        var sum = 0
        const inputs = document.querySelectorAll('input[name=price_accepted]');
        const tot = document.getElementById('total_acc_amt');
        for (var input in inputs) {
            if (inputs[input].textContent != undefined || !isNaN(inputs[input].value)) {
                sum += parseInt(inputs[input].value);
            }
        }
        tot.textContent = sum;
    });
    }
});