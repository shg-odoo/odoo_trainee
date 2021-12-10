import { ProductList } from './product-list.js';
import { SideBar } from './sidebar.js';

export class Content {
	mount(target) {
		const div = document.createElement("div");
		div.id = "content";
		div.innerHTML = `<div id="products">
					     </div>
					     <div id="cart">
					   	 	<h1>Cart</h1>
					     </div>`;
		target.appendChild(div);

		const productsDiv = document.getElementById("products");
		const product_list = new ProductList(productsDiv);
		product_list.mount();

		const cartDiv = document.getElementById("cart");
		const cart = new SideBar();
		cart.mount(cartDiv);
	}
	
}