import { ProductList } from './ProductList.js'
import { Cartitem } from "./SidebarItem.js"

export class Content {
    constructor(data, targetELm) {
        this.data = data;
        this.target = targetELm;
    }
    render() {
        let productConatiner = document.createElement('div');
        productConatiner.classList.add('shop-items');
        this.ProductList = new ProductList(this.data, productConatiner);
        this.ProductList.el = this.ProductList.loadhtml();
        this.target.appendChild(productConatiner);
        document.querySelector('.shop-items');
        let cartContainer = document.createElement('div');
        cartContainer.classList.add('cart-items');
        this.cartobj = new Cartitem(cartContainer);
        this.cartobj.el = this.cartobj.render();
        var cartTotal = document.createElement('div');
        cartTotal.classList.add('cart-total');
        cartTotal.innerHTML += `<strong class="cart-total-title">Total</strong>
        <span class="cart-total-price"> <b>₹</b> 0</span>
        <button class="btn btn-primary btn-purchase" type="button">PURCHASE</button>`;
        cartContainer.append(cartTotal)
        this.target.appendChild(cartContainer)
        document.querySelector('.btn-purchase').addEventListener('click', this.onPurchaseButton.bind(this));
    }
    onPurchaseButton() {    
    window.dispatchEvent(new CustomEvent('btn-purchase'));
    }
}