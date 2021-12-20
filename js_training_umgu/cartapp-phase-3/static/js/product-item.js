import { CommonItemView } from "./common-item-view.js";
const { Component, mount } = owl;

export class ProductItem extends Component {
    static template = "ProductItem";
    static props = ["product"];
    static components = { CommonItemView };

    addToCart(ev) {
        this.env.bus.trigger("addToCart", {product: this.props.product});
    }
}