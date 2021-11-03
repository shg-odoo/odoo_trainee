
function setCookie(cname,cvalue,exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires=" + d.toGMTString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

// function check() {
//   let user = getCookie("username");
//   if (user != "") {
//     alert("Welcome again " + user);
//   } else {
//      user = prompt("Please enter your name:","");
//      if (user != "" && user != null) {
//        setCookie("username", user, 30);
//      }
//   }
// }

let itemsArray;
function check() {
	let cookie=getCookie("items");
	if(cookie=="") {
		itemsArray=[];
		setCookie("items",JSON.stringify(itemsArray), 30);
	}
	else
	{
		itemsArray=JSON.parse(cookie);
	}
}

// console.log(document.cookie);

function addToCart(btn) {
			let productId=btn.parentNode.id;
			// console.log(productId);

			let list=btn.parentNode.childNodes;

			let productImg=list[1].src;
			// console.log(productImg);

			let productName=list[3].childNodes[1].getAttribute('name');
			// console.log(productName);

			let productPrice=Number(list[5].childNodes[1].getAttribute('value'));
			// console.log(productPrice);

			let quantity=1;
			// console.log(quantity);


			let isPresent=false;
        	for(let i=0;i<itemsArray.length;i++) {
        		if(itemsArray[i][0] == productId) {
        			isPresent=true;
        		}
        	}
        	if(!isPresent) {
        		itemsArray.push([productId,productImg,productName,productPrice,quantity]);
        		setCookie("items",JSON.stringify(itemsArray), 30);
        	}

			// if (localStorage.getItem('cart') == null) {
   //      		itemsArray = [];
   //      		itemsArray.push([productId,productImg,productName,productPrice,quantity]);
   //      		localStorage.setItem('cart', JSON.stringify(itemsArray))

   //    		}
   //    		else {
   //      		itemsArrayStr = localStorage.getItem('cart');
   //      		itemsArray = JSON.parse(itemsArrayStr);

   //      		let isPresent=false;
   //      		for(let i=0;i<itemsArray.length;i++) {
   //      			if(itemsArray[i][0] == productId) {
   //      				isPresent=true;
   //      			}
   //      		}
   //      		if(!isPresent) {
   //      			itemsArray.push([productId,productImg,productName,productPrice,quantity]);
   //      			localStorage.setItem('cart', JSON.stringify(itemsArray))
   //      		}

   //    		}

		}