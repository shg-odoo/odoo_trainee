function load() {
			let tag = document.getElementById('container')
      		itemsArrayStr = localStorage.getItem('cart');
      		itemsArray = JSON.parse(itemsArrayStr);

      		let labels=document.querySelectorAll("label");
      		if(itemsArray==null || itemsArray.length==0) {
      			// let labels=document.querySelectorAll("label");
      			labels[0].style.display="none";
      			labels[1].style.display="block";
      		}
      		else {
      			labels[0].style.display="block";
      			labels[1].style.display="none";
      		}

      		let str="";
      		if(itemsArray!=null) {
      			itemsArray.forEach((element) => {
       
      	 		str += `<div class="product" id="${element[0]}">
							<div class="itemBox">
								<img src=${element[1]} alt="Image not found">
								<p><strong>Name : </strong><span  name="itemName">${element[2]}</span></p>
								<p><strong>Price : </strong><span  name="price" value="${element[3]}">499 Rs.</span></p>
							</div>
							<div class="itembox">
								<h1>Quantity : <input type="number" name="quantity" min="0" placeholder="${element[4]}" oninput="changeCost(this)"></h1>
			    				<h1>Cost : <strong name="totalprice">${element[3] * element[4]}</strong></h1>
			    				<button onclick="del(this)" id="btn-del">Remove</button>
							</div>
						</div>`
      			});
      		}

     		tag.innerHTML=str;
     		totalCost();

		}

		function totalCost() {
			let totalPrices=document.querySelectorAll(`strong[name="totalprice"]`);
			// console.log(totalPrices);
			let sum=0;
			totalPrices.forEach(element => {
				sum=sum+Number(element.textContent);
			})
			let labelTag=document.getElementById("totalCost");
			labelTag.textContent=sum;

		}



		function changeCost(inpt) {
			let productId=inpt.parentNode.parentNode.parentNode.id;

			itemsArrayStr = localStorage.getItem('cart');
      		itemsArray = JSON.parse(itemsArrayStr);

      		let index=-1;
      		for(let i=0;i<itemsArray.length;i++) {
      			if(itemsArray[i][0] == productId) {
      				index=i;
      				break;
      			}
      		}

      		itemsArray[index][4] =Number(inpt.value);
  			// console.log(itemsArray[index][4]);

      		let totalPriceTag=inpt.parentNode.parentNode.childNodes[3].childNodes[1];
			totalPriceTag.textContent=itemsArray[index][3]*itemsArray[index][4];

			localStorage.setItem('cart', JSON.stringify(itemsArray));


			// let quantity=Number(inpt.value);
			// // console.log(quantity);

			// let price=Number(inpt.parentNode.parentNode.parentNode.childNodes[1].childNodes[5].childNodes[1].getAttribute("value"));
			// // console.log(price);

			// let totalPriceTag=inpt.parentNode.parentNode.childNodes[3].childNodes[1];
			// totalPriceTag.textContent=quantity*price;

			totalCost();

		}

		function del(btn) {
			let productId=btn.parentNode.parentNode.id;
			// console.log(productId);
			itemsArrayStr = localStorage.getItem('cart');
      		itemsArray = JSON.parse(itemsArrayStr);
      		for(let i=0;i<itemsArray.length;i++) {
      			if(itemsArray[i][0] == productId) {
      				itemsArray.splice(i,1);
      				break;
      			}
      		}
      		// itemsArray.forEach((element,index) => {
      		// 	if(btn.parentNode.parentNode.id == element[0]) {
      		// 		itemsArray.splice(index,1);
      		// 		break;
      		// 	}
      		// })
      		localStorage.setItem('cart', JSON.stringify(itemsArray))
      		load();
		}