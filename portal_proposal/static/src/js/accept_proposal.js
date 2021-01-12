odoo.define('portal_proposal.proposal_page_template', function (require) {
'use strict';

var publicWidget = require('web.public.widget');


publicWidget.registry.ProposalPage = publicWidget.Widget.extend({
    selector: '.oe_proposal_form',
    events: {        
        'click .accept_data': '_accept_data', 
    },

    _accept_data: function(e) {
        e.stopPropagation();
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
                args: [this.value,qty_lst,price_lst,document.getElementById('proposalId').value],
                context: this.context,
            }); 
    }
    
});
    
    document.getElementById("price").addEventListener("change", function onchange_sum(e) {
        var sum = 0
        const inputs = document.querySelectorAll('input[name=price_accepted]');
        const tot = document.getElementById('total_acc_amt');
        for (var input in inputs) {
            if (inputs[input].textContent != undefined || !isNaN(inputs[input].value)) {
                /*inputs[input].oninput = updateValue(e);*/
                sum += parseInt(inputs[input].value);
            }
        }
        tot.textContent = sum;
    }); 

    /*function updateValue(e) {
        var pr_table = document.getElementById('pr_table');
        var sum = 0;        
        for (var i = 1, row; row = pr_table.rows[i]; i++) {
            var y = pr_table.rows[i].querySelectorAll('input[name=price_accepted]');
            var x = pr_table.rows[i].cells[6].children[0].value;
            sum += parseInt(y);            
        }
        return sum;
    }   */

});