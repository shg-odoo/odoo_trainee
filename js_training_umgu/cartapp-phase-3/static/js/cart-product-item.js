import { CommonItemView } from "./common-item-view.js";

const { Component } = owl;
const { useDispatch, useStore } = owl.hooks;

export class CartProductItem extends Component {
	static template = "CartProductItem";
	static props = ["product"];
	static components = { CommonItemView };
	dispatch = useDispatch();

	removeFromCart() {
		this.trigger("remove-from-cart", {product : this.props.product});
	}
}