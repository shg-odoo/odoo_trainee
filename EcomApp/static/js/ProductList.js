export class ProductList {
    constructor(data, targetELm) {
        this.data = data;
        this.target = targetELm;
    }
    loadhtml() {
        let data = this.data;
        var mainContainer = this.target;
        for (var i = 0; i < data.length; i++) {
            var div = document.createElement("div");
            div.innerHTML += `<div class="shop-item">
            <span class="shop-item-title">${data[i].title}</span>
            <img class="shop-item-image" src=${data[i].image}>
            <div class="shop-item-details">
                <span class="shop-item-price-symbol"><strong>₹</strong></span>
                <span class="shop-item-price">${data[i].price}</span>
                <button class="btn btn-primary shop-item-button add-item-to-cart" data-id="${data[i].id}" type="button">ADD TO CART</button>
            </div>
        </div><tr>`
            mainContainer.appendChild(div);
            [...div.querySelectorAll('.add-item-to-cart')].forEach((elem) => {
                elem.addEventListener('click', this.onAddItemToCart.bind(this));
            });
        }
    }
    onAddItemToCart(ev) {
        const productId = ev.currentTarget.getAttribute('data-id');
        var currentProduct = this.data.find(item => item.id == productId);  //find the product with the id
        window.dispatchEvent(new CustomEvent('add-item-to-cart', { detail: { product_obj: currentProduct } }));
    }
}