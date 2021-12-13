export class CartProductItem {

	constructor(product){
		this.product = product;	
	}
	mount(target){
		const div = document.createElement("div");
		div.className="itemBox";
		this.el=div;
        div.innerHTML =`<div class="shop-item-details">
        					<img class="shop-item-image" src=${this.product['image']}>
		        			<span class="shop-item-price-symbol"><strong>₹</strong></span>
	    	    			<span class="shop-item-price">${this.product['price']}</span>
							<button class="btn btn-primary shop-item-button remove-btn" data-id="${this.product['id']}" type="button">Remove</button>
						</div>
						<br>`;
		target.appendChild(div);
		div.querySelector('.remove-btn').addEventListener('click',this.removeFromCart.bind(this));
	}

	removeFromCart(){ 
		const removeFromCartEvent = new CustomEvent("removeFromCart", { bubbles : true,detail : { product : this.product } });
		this.el.dispatchEvent(removeFromCartEvent);
		this.el.remove();

	}

}