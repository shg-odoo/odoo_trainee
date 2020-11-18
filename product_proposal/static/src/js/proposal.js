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
            ajax.jsonRpc('/my/proposals/<int:order_id>/accept', 'call', {
                'data': dict, 'access_token': access_token
            },
            location.reload())

        },
    })
});



//});

