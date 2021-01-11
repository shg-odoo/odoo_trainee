odoo.define('portal_proposal.proposal_page_template', function (require) {
'use strict';

var publicWidget = require('web.public.widget');


publicWidget.registry.ProposalPage = publicWidget.Widget.extend({
    selector: '.oe_proposal_form',
    events: {        
        'click .accept_data': '_accept_data',   
        'change .get_acc_sum': '_get_acc_sum',   
        'click .onchange_sum': '_onchange_sum', 
    },

    _accept_data: function(e) {
        e.stopPropagation();
        e.preventDefault();
        var qty_lst = [];
        var price_lst = [];
        var pr_table = document.getElementById('pr_table');
        for (var i = 1, row; row = pr_table.rows[i]; i++) {        
            var qty = pr_table.rows[i].cells[4].children[0].value;
            var price = pr_table.rows[i].cells[6].children[0].value;  
            var prod = pr_table.rows[i].cells[1].children[1].value;
            qty_lst.push({prod,qty});
            price_lst.push({prod,price});        
        }
        
    	this._rpc({
                model: 'portal.proposal',
                method: 'accept_qty_price',
                args: [this.value,qty_lst,price_lst,document.getElementById('proposalId').value],
                context: this.context,
            });  

        return this._rpc({                
                route: '/proposal/accept',
            });      
    },

    _get_acc_sum: function(e) {
        console.log("ONCHANGE....");
    },

    _onchange_sum: function(e) {
        document.getElementById("price").addEventListener("change", myFunction);

        function myFunction() {
            var lst = [];
            var sum = 0;
            var pr_table = document.getElementById('pr_table');
            for (var i = 1, row; row = pr_table.rows[i]; i++) {
                var x = pr_table.rows[i].cells[6].children[0].value;
                lst.push(parseInt(x));                            
            }
            for (var l in lst) {
                if (!isNaN(lst[l])){
                    sum += lst[l];
                }                
            }
            return sum;
        }
        
    }
});

});