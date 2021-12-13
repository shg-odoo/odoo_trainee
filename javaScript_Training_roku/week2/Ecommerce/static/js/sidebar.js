import { CartProductItem } from './cartproductitem.js';
export class SideBar {
	constructor(){
        this.Cartitems = [];
		window.addEventListener('addItemToCart', this.addToCart.bind(this));
	}
	mount(target){
		this.target = target;
		this.target.addEventListener("removeFromCart", this.removeFromCart.bind(this));
		const sidebarElement = document.createElement("div");
		sidebarElement.classList.add("empty_cart_message");
		sidebarElement.textContent = "Cart is empty!"
		target.appendChild(sidebarElement);
	}

	addToCart(ev) {
		const product = ev.detail.product;
		const isPresent = this.Cartitems.find((item) => product.id === item.id);
		if(!isPresent) {
			const emptyMessage = this.target.querySelector(".empty_cart_message");
			if (emptyMessage) {
				emptyMessage.remove();
			}
			this.Cartitems.push(product);
			let productitem = new CartProductItem(product)
        	productitem.mount(this.target)
		}
	}

	removeFromCart(ev) {
		debugger
		const product = ev.detail.product;
		const index=this.Cartitems.indexOf((item) => item.id === product.id);
		this.Cartitems.splice(index,1);
	}
}