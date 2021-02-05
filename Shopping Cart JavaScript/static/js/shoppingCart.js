var cart = [];
        $(function () {
            if (localStorage.cart)
            {
                cart = JSON.parse(localStorage.cart);
                showCart();
            }
        });
        function addToCart() {
          let element = event.target.parentNode.parentNode;
          var link = element.querySelector("#image").getAttribute("data-link");
          var name = element.querySelector("#name").getAttribute("data-name");
          var id = element.querySelector("#name").getAttribute("data-id");
          var price = element.querySelector("#price").getAttribute("data-price");
          var quantity = element.querySelector("#quantity").getAttribute("data-qty");
            for (var i in cart) {
                if(cart[i].Product == name)
                {
                    cart[i].Id=id;
                    cart[i].Link=link;
                    cart[i].Name = name;
                    cart[i].Price=price;
                    showCart();
                    saveCart();
                    return;
                }
            }
            var item={ Id:id, Link:link, Name:name, Price:price }
            cart.push(item);
            saveCart();
            showCart();
        }

        function deleteItem(index){
            cart.splice(index,1); // delete item at index
            showCart();
            saveCart();
        }

        function saveCart() {
            if ( window.localStorage)
            {
                localStorage.cart = JSON.stringify(cart);
            }
        }

        function showCart(price) {
          
            if (cart.length == 0) {
                $("#cart").css("visibility", "hidden");
                return;
            }

            $("#cart").css("visibility", "visible");
            $("#cartBody").empty();
            for (var i in cart) {
                var item = cart[i];
                console.log(cart.length);
                var row = "<tr><td><img width=150 src="+item.Link+">"+"<td>"+item.Name+"</td>"+"</td>"+ "</td><td>" + item.Price + "</td>"+"<td><button type='button' class='btn btn-danger' onclick='deleteItem(" + i + ")'>"+"<i class='fa fa-trash'></i>"+" Delete</button></td></tr>";
                $("#cartBody").append(row);
            }
            
        }