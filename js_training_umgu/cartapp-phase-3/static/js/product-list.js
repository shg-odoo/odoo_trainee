import { ProductItem } from "./product-item.js";

const { Component, mount } = owl;
const { useState } = owl.hooks;

export class ProductList extends Component {
    static template = "ProductList";
    static components = { ProductItem };

    constructor() {
        super(...arguments);
        this.state = useState({ items: [] });
        this.env.bus.on("searchProducts", this, this.searchProducts.bind(this));
    }

    willStart() {
        return this.fetchProducts('/products').then((products) => {
            this.state.items = products;
        }, function (error) {
            console.log(error);
        });
    }

    fetchProducts(urlString) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', urlString);

        return new Promise((resolve, reject) => {
            xhr.onload = function() {
                if(xhr.status === 200) {
                    let obj = JSON.parse(xhr.responseText);
                    obj = JSON.parse(obj['result']);
                    resolve(obj);
                }
                else {
                    reject("Something went wrong!");
                }
            }
            xhr.send();
        });     
    }

    searchProducts(ev) {
        return this.fetchProducts(`/search?searchText=${ev.searchText}`).then((result) => {
            this.state.items = result;
        }, function (error) {
            console.log(error);
        });
    }

}