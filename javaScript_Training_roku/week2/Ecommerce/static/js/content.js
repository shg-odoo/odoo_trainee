import {productList} from './productList.js';
import {SideBar} from './sidebar.js';

export class Content{
	constructor(Element){
		this.target = Element;
	}
	mount(){
		let mainContainer = document.getElementById("product");
		let productlist =  new productList();
		productlist.mount(mainContainer);
		let cartdiv = document.querySelector('.sidecart');

		let sideBar = new SideBar();
		sideBar.mount(cartdiv);
	}
}