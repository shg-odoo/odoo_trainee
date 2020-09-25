odoo.define('proposal_order', function (require) {"use strict";


    var ajax = require('web.ajax');
    var rpc = require('web.rpc');
    var token = (location.search.split('token' + '=')[1] || '').split('&')[0];
    $(document).ready(function() {  
      $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
      });
      $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
      });
    });

    $(document).ready(function() { $("#accept_btn").click(
        function showtProposalData() {
            var dataarray  =[];
            var qty,price,line_id,state;
            var acc_qty = document.getElementsByClassName('accept_qty');
            var acc_price = document.getElementsByClassName('accept_price');
            var rec_id = document.getElementsByClassName("record_id")[0].value
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
                            'state':'confirm',
                            'price_acept': price,
                        })
                }
                console.log(dataarray)
                ajax.jsonRpc('/proposal/accepted', 'call', { 'data' : dataarray }).then(function (url){})
            })
})
});