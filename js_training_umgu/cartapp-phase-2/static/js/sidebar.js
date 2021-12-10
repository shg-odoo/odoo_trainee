import { CartProductItem } from './cart-product-item.js';

export class SideBar {
	constructor() {
		this.items = [];
		window.addEventListener("addItemToCart", this.addItemToCart.bind(this));
	}

	mount(target) {
		this.items.forEach((item) => {
			const cartProductItem = new CartProductItem(item);
			cartProductItem.mount(target);
		});
		this.el = target;
		this.el.addEventListener('removeItemFromCart', this.removeItemFromCart.bind(this));
	}

	addItemToCart(ev) {
		const clickedProduct = ev.detail.product;
		const isPresent = this.items.find((item) => item.productId === clickedProduct.productId);
		if(!isPresent) {
			this.items.push(clickedProduct);
			const cartProductItem = new CartProductItem(clickedProduct);
			cartProductItem.mount(this.el);

		}
		
	}

	removeItemFromCart(ev) {
		const clickedProduct = ev.detail.product;
		const index = this.items.indexOf((item) => item.productId === clickedProduct.productId);
		this.items.splice(index, 1);
	}

}