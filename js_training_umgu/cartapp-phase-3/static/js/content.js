import { ProductList } from "./product-list.js";
import { Cart } from "./cart.js";

const { Component, mount } = owl;

export class Content extends Component {
	static template = "Content";
	static components = { ProductList, Cart};
}