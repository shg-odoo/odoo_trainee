import { CartProductItem } from "./cart-product-item.js";

const { Component, mount } = owl;
const { useState, useStore, useDispatch } = owl.hooks;

export class Cart extends Component {
    static template = "Cart";
    static components = { CartProductItem };
    
    constructor() {
        super(...arguments);
        this.items = useStore((state) => state.items);
        this.dispatch = useDispatch();
        this.env.bus.on("addToCart", this, this.addToCart.bind(this));
    }

    addToCart(ev) {
        const clickedProduct = ev.product;
        this.dispatch("addItem", clickedProduct);
    }

    removeFromCart(ev) {
        const clickedProduct = ev.detail.product;
        this.dispatch("removeItem", clickedProduct);
    }
}