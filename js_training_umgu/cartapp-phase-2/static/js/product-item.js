export class ProductItem {
	constructor(product) {
		this.product = product;
	}
	
	mount(target) {
		const productDiv = document.createElement("div");
		productDiv.className = "itemBox";
		productDiv.id = this.product.productId;
		productDiv.innerHTML = window.qweb.render("ProductItem", { product: this.product })
    target.appendChild(productDiv)
    productDiv.querySelector(".addToCart").addEventListener("click", this.addToCart.bind(this));
	}

	addToCart() {
  		const addItemEvent = new CustomEvent("addItemToCart", { detail: { product: this.product } });
  		window.dispatchEvent(addItemEvent);
	}
}