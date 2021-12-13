export class ProductItem {
	constructor(product){
		this.product = product;
	}
	mount(target){
		const div = document.createElement("div");
		div.className="itemBox";
        div.innerHTML =`<img class="shop-item-image" src=${this.product['image']}>
        				<h3>${this.product['name']}</h3>
        				<div class="shop-item-details">
		        			<span class="shop-item-price-symbol"><strong>₹</strong></span>
	    	    			<span class="shop-item-price">${this.product['price']}</span>
							<button class="btn btn-primary shop-item-button" data-id="${this.product['id']}" type="button">ADD TO CART</button>
						</div>
						<br>`;

		target.appendChild(div);
		div.querySelector('.shop-item-button').addEventListener('click', this.addToCart.bind(this));
	}

	addToCart() {
		const addToCartEvent = new CustomEvent("addItemToCart", { detail : { product : this.product } });
		window.dispatchEvent(addToCartEvent);
	}	
}

