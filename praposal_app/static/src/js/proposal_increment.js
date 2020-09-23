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

$('.accept').click(function() {

function showtProposalData() {
 var dataarray  =[] 
        var acc_qty = document.getElementsByClassName('accept_qty');
        var acc_price = document.getElementsByClassName('accept_price');
        for (i = 0; i < acc_qty.length; i++) {
            var qtyobj = acc_qty[i];
            var priceobj =acc_price[i]
            qty = qtyobj.value
            price = priceobj.value
            line_id = qtyobj.getAttribute('line_id')
            dataarray.push({
                    'line_id' : line_id,
                    'qty_acept': qty,
                    'price_acept': price,
                })
        }console.log(dataarray)
    } 

});
