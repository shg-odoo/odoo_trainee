odoo.define('product_proposal.portal', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');

window.addEventListener('load',function(e){
    console.log('document.onload');

   var elementsMin = document.getElementsByClassName("minus");
   var elementsPlu = document.getElementsByClassName("plus");
   var accept_price = document.getElementsByClassName("accept_price");

   var element;

       for (element of elementsMin) {
        element.addEventListener("click", function(e){
        if (e.target.nextElementSibling.value > 0 ){
                        e.target.nextElementSibling.value --
                                   }
                                                    });
                                     }

          for (element of elementsPlu) {
           element.addEventListener("click", function(e){
           e.target.previousElementSibling.value ++
                                                        });
                                         }
//on change for both qty change and accepted total
//    var sumTotal =0.0;
//const accepted_qty = document.querySelector('.accepted_quantity')
//
//const element2 = document.querySelector('.accept_price')
//console.log('!!!!', element2)
//document.addEventListener('change', event => {
//  if (event.target !== accepted_qty && event.target !== element2) {
//    return
//  }
//  //handle  change
//  console.log("event...........")
//  console.log("accepted_qty....",accepted_qty)


    });

  publicWidget.registry.ProposalWidget = publicWidget.Widget.extend({
        selector: '#accept',
        events: {
            'click .accept_button': 'clicking_accept_btn',
        },
        clicking_accept_btn: function () {
            const accepted_quantity = document.getElementsByClassName('accepted_quantity')
            const price_accept = document.getElementsByClassName('accept_price')

            let quantity
            let price
            let record_id
            let proposal_line_id
            const proposal_id = document.getElementsByClassName('proposal_id')
            const dict = [];
            const access_token = new URLSearchParams(window.location.search).get('access_token');

            for (var i = 0; i < accepted_quantity.length; i++) {
                var qty_linebyline = accepted_quantity[i];
                var price_linebyline = price_accept[i]
                quantity = qty_linebyline.value
                price = price_linebyline.value
                record_id = proposal_id[0].value
                proposal_line_id = qty_linebyline.getAttribute('line_id')

                dict.push({
                    'qty_accepted': quantity,
                    'price_accepted': price,
                    'proposal_id': record_id,
                    'accepted_total': quantity * price,
                    'line_id': proposal_line_id,
                });
            ajax.jsonRpc('/my/proposals/<int:order_id>/accept', 'call', {
                'data': dict, 'access_token': access_token
            },
            location.reload())
            alert("Your Proposal Have Been Accepted!");
            location.reload();
        }
    }
});



});

