window.onload = function(event){
  console.log("Hello World!");
  // document.getElementById("container").innerHTML = '<div><input placeholder="Enter your search here">  <button>Search</button></div>';

  var div = document.createElement("div");
  var input = document.createElement("input");
  input.setAttribute('id', 'search');
  var button = document.createElement("button");
  button.setAttribute('id', 'button');
  var buttontext = document.createTextNode("Search");
  button.appendChild(buttontext);
  var div_items = document.createElement("div");
  div_items.setAttribute('id', 'divsearch');
  var container = document.getElementById("container");
  container.appendChild(div);
  div.appendChild(input);
  div.appendChild(button);
  container.appendChild(div_items);
  // var span = document.createElement("span");
  // var addtocart = document.createElement("button");
  // addtocart.setAttribute('id', 'addtocart');
  // function ajaxReq() {
  //     if (window.XMLHttpRequest) {
  //         return new XMLHttpRequest();
  //     } else if (window.ActiveXObject) {
  //         return new ActiveXObject("Microsoft.XMLHTTP");
  //     } else {
  //         alert("Browser does not support XMLHTTP.");
  //         return false;
  //     }
  // }

  button.addEventListener("click", function(){
    var search_text =document.getElementById("search").value;
    var payload = {'value': search_text};
    var z = JSON.stringify(payload);
    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:8080/search";
    xmlhttp.open("POST", url, true); // set true for async, false for sync request
    //xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.send(z); // or null, if no parameters are passed

    xmlhttp.onreadystatechange = function (){
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var obj = JSON.parse(xmlhttp.responseText);

   			// console.log(xmlhttp.responseText);
   			// button.insertAdjacentElement("afterend", divsearch);
   			// var span = document.createElement("span");
   			// divsearch.appendChild(span);
   			// var string = ''	;
   		  // span.setAttribute('id', 'span');
   		  // document.getElementById('span').innerHTML = ""
        div_items.replaceChildren();
 			  for (var i=0; i< obj.length; i++){
   				// console.log(obj);
   				// console.log(obj.length);
   			  // var span = document.createElement("span");
   				// divsearch.appendChild(span);
          var div = document.createElement("div");
   			  var span = document.createElement("span");
          span.innerText=obj[i].name;
          var span1 = document.createElement("span");
          span1.innerText=obj[i].price;
          var addtocart = document.createElement("button");
          addtocart.setAttribute('id', `button${i}`);
          addtocart.setAttribute('data-id', `${obj[i]._id}`);
          addtocart.innerText = 'Add to Cart';
          addtocart.addEventListener("click", function(event){

            // var search_text =document.getElementById("addtocart").value;
            var payload = {'product-id': event.srcElement.dataset.id};
            var z = JSON.stringify(payload);
            var xmlhttp = new XMLHttpRequest();
            var url = "http://localhost:8080/add_to_cart";
            xmlhttp.open("POST", url, true); // set true for async, false for sync request
            xmlhttp.send(z); // or null, if no parameters are passed

            xmlhttp.onreadystatechange = function (){
              if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                var obj = JSON.parse(xmlhttp.responseText);
              }
            }
          });
          div.appendChild(span);
          div.appendChild(span1);
          div.appendChild(addtocart);
          div_items.appendChild(div);
          console.log(div);
          
   				// span.insertAdjacentElement("afterend", span);
   			  //document.getElementById('span'+'${i}').innerHTML = "<br><br>"+ "Product Name: " + obj[i].name +"<br>"+ "  Product Price: "+ obj[i].price+ "<br>";
   				//span.appendChild(addtocart);
   				//document.getElementById('addtocart'+'${i}').innerHTML = "Add to Cart";
   				// var span = document.createElement("span");
   				// span.setAttribute('id', 'span');
   				// span.insertAdjacentElement("afterend", span+i)
   				// document.getElementById('divsearch').innerHTML = "Product Price: "+ 	obj[i].price;
   				// console.log();
   			  // console.log(dict(obj));
   			}
      }
    }
  });
}