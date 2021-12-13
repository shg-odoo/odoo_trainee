import {rpc} from './rpc.js';
import { ProductItem } from './productitem.js';

export class productList{
	constructor() {
		window.addEventListener("DisplaySearchProduct", this.searchProducts.bind(this));
	}

	async mount(target){
		await this.willStart();
		this.productListDiv = document.createElement("div");
    	this.products.forEach((prod) => {
        	let productitem = new ProductItem(prod);
        	productitem.mount(this.productListDiv);
		});     
		target.appendChild(this.productListDiv);
	}

	async willStart() {
        const data = await rpc("/shoping_page", {});
        this.products = JSON.parse(data);
        console.log(this.products);
	}	

	async searchProducts(ev) {
		const value = ev.detail.searchText
		this.productListDiv.innerHTML=""
		this.products = await rpc("/searchproducts", {
			val:value,
		});
		this.products.forEach((prod) => {
        	let productitem = new ProductItem(prod);
        	productitem.mount(this.productListDiv);
		});   
		target.appendChild(this.productListDiv);
	}
}