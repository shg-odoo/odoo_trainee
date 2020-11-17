odoo.define('product_proposal.portal', function (require) {
    'use strict';

window.addEventListener('load',function(e){
    console.log('document.onload');

   var elementsMin = document.getElementsByClassName("minus");
   var elementsPlu = document.getElementsByClassName("plus");
    var accept_price = document.getElementsByClassName("accept_price");
   console.log("price.....",accept_price)
   console.log('elementsMin................',elementsMin)
   var element,closestMin,closestPlu

       for (element of elementsMin) {
        element.addEventListener("click", function(e){
        console.log('inner funcn', e.target);
//        console.log('inner elemnt', e.nextElementSibling);
        closestMin = element.nextElementSibling("accepted_quantity");
        console.log("closest..",closest)
        if (closestMin.value > 0 ){
                        closestMin.value --
                                   }
                                                    });
                                     }



//        input_text = document.querySelectorAll(".number > .accepted_quantity");
//        console.log("input_text............",input_text)
//        var list = document.getElementById("minus-btn").nextSibling.innerHTML;
//        console.log("lilst.............",list)



          for (element of elementsPlu) {
           element.addEventListener("click", function(e){
           var closestPlu = element.ElementSibling("accepted_quantity");
           closestPlu.value ++
                                                        });
                                         }

      var sumTotal =0.0;
      for (price of accept_price){
      price.addEventListener("oninput", function(e){
        sumTotal = sumTotal+price.value
      });
      }

    });
});