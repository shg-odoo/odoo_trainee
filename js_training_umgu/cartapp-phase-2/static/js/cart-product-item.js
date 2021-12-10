export class CartProductItem {
	constructor(product) {
		this.product = product;
	}

	mount(target) {
		const productDiv = document.createElement("div");
		this.el = productDiv;
		productDiv.className = "itemBox";
		productDiv.id = this.product.productId;

		productDiv.innerHTML = window.qweb.render("CartProductItem", {product : this.product});
    	
    	target.appendChild(productDiv);
    	this.el.querySelector(".removeFromCart").addEventListener("click", this.removeFromCart.bind(this));
	}

	destroy() {
		this.el.remove();
	}

	removeFromCart() {
		const removeItemEvent = new CustomEvent("removeItemFromCart", { bubbles: true, detail: { product: this.product } });
  		this.el.dispatchEvent(removeItemEvent);
  		this.destroy();
	}
}