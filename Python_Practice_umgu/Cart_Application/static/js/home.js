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

			if (localStorage.getItem('cart') == null) {
        		itemsArray = [];
        		itemsArray.push([productId,productImg,productName,productPrice,quantity]);
        		localStorage.setItem('cart', JSON.stringify(itemsArray))

      		}
      		else {
        		itemsArrayStr = localStorage.getItem('cart');
        		itemsArray = JSON.parse(itemsArrayStr);

        		let isPresent=false;
        		for(let i=0;i<itemsArray.length;i++) {
        			if(itemsArray[i][0] == productId) {
        				isPresent=true;
        			}
        		}
        		if(!isPresent) {
        			itemsArray.push([productId,productImg,productName,productPrice,quantity]);
        			localStorage.setItem('cart', JSON.stringify(itemsArray))
        		}

      		}

		}