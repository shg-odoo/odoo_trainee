export class Cartitem {
    constructor(targetElement) {
        this.Cartitems = [];
        this.target = targetElement;
        window.addEventListener('add-item-to-cart', (ev) => {
            ev.preventDefault();
            this.Cartitems.push(ev.detail.product_obj);
            this.render(this.Cartitems);
            this.Cartitems = [];
        });
        window.addEventListener('btn-purchase', (ev) => {
            alert('Thank you for your purchase')
            var cartItems = document.querySelectorAll('.cart-items')[0].getElementsByClassName('cart-row')
            for (var i = cartItems.length - 1; i >= 0; i--) {
                cartItems[i].remove();
            }
            this.updateCartTotal();
        });
    }
    render(data) {
        if (this.Cartitems.length == 0) {
            let cartinitialValue = document.createElement('div')
            cartinitialValue.classList.add('empty-class')
            cartinitialValue.innerHTML = "Cart is Empty"
            this.target.appendChild(cartinitialValue);
        } else {
            console.log("this.target ------------->", this.target);
            if (document.querySelector('.empty-class')) {
                document.querySelector('.empty-class').style.display = 'none';
            }
            var mainContainer = this.target;
            for (var i = 0; i < data.length; i++) {
                var cartRow = document.createElement("div");
                cartRow.classList.add('cart-row');
                cartRow.innerHTML += `<div class="cart-item cart-column">
                    <span class="cart-item-id" hidden>${data[i].id}</span>
                    <span><img class="cart-item-image" src=${data[i].image}></span>
                    <span class="cart-item-title">${data[i].title}</span>
                </div>
                <span class="cart-price cart-column">${data[i].price}</span>
                <div class="cart-quantity cart-column">
                    <input class="cart-quantity-input" type="number" value="1">
                    <button class="btn btn-danger btn-remove-item" type="button">REMOVE</button>
                </div>
                `
                mainContainer.appendChild(cartRow);
                [...cartRow.querySelectorAll('.btn-remove-item')].forEach((elem) => {
                    elem.addEventListener('click', this.onRemoveItemFromCart.bind(this));
                    this.updateCartTotal();
                });
                cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', this.quantityChanged.bind(this))

                this.updateCartTotal();
            }
        }
    }
    updateCartTotal() {
        var cartItemContainer = document.getElementsByClassName('cart-items')[0]
        var cartRows = cartItemContainer.getElementsByClassName('cart-row')
        var total = 0
        for (var i = 0; i < cartRows.length; i++) {
            var cartRow = cartRows[i]
            var priceElement = cartRow.getElementsByClassName('cart-price')[0]
            var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
            var price = parseFloat(priceElement.innerText.replace('₹', ''))
            var quantity = quantityElement.value
            total = total + (price * quantity)
        }
        if (cartRows.length) {
            document.querySelector('.btn-purchase').style.display = 'block';

        } else {
            document.querySelector('.btn-purchase').style.display = 'none';
            document.querySelector('.empty-class').style.display = 'block';
        }
        total = Math.round(total * 100) / 100
        document.getElementsByClassName('cart-total-price')[0].innerText = '₹' + total
    }

    quantityChanged(event) {
        var input = event.target
        if (isNaN(input.value) || input.value <= 0) {
            alert('Only positive numbers allowed')
            input.value = 1
        }
        this.updateCartTotal()
    }
    onRemoveItemFromCart(event) {
        var buttonClicked = event.target
        buttonClicked.parentElement.parentElement.remove()
        this.updateCartTotal();
    }

}
