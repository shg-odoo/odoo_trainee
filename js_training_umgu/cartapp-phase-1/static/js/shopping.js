function fetchProducts() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', '/products', true);

    return new Promise((resolve, reject) => {
        xhr.onload = function() {
            if(this.status === 200) {
                let obj = JSON.parse(this.responseText);
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

function displayProducts(obj) {
    const keys = [];
    for (let k in obj) keys.push(k);

    let idIndex = 1;
    const productsBody = document.getElementById("products");
    keys.forEach(category => {
        const mainDiv = document.createElement("div");
        mainDiv.className = "container";

        const h1 = document.createElement("h1");
        h1.innerHTML = category;

        mainDiv.appendChild(h1);
        const subDiv = document.createElement("div");

        obj[category].forEach( (product) => {
            let productDiv = document.createElement("div");
            productDiv.className = "itemBox";
            productDiv.id = `${idIndex++}`;
            productDiv.innerHTML = `<img src=${product['img']} alt="Image not found">
                                    <p><strong>Name : </strong><span  name=${product['name']}>${product['name']}</span></p>
                                    <p><strong>Price :</strong><span  name="Price" value="${product['price']}">${product['price']} Rs.</span></p>
                                    <button onclick="addToCart(this)">Add To Cart</button>`;
            subDiv.appendChild(productDiv);
        });
        mainDiv.appendChild(subDiv);
        productsBody.appendChild(mainDiv);
    });
}

function load() {
    fetchProducts().then( function(products) {
        displayProducts(products);
    }, function(error) {
        console.log(error);
    });
}

document.addEventListener("addToCart",function(e) {
    const btn = e.detail;
    const productId = btn.parentNode.id;
    const cartBody = document.getElementById('cart');
    const cartItems = cartBody.children;

    let isPresent=false;
    for(let i = 1; i < cartItems.length; i++){
        if(cartItems[i].id == productId) {
            isPresent = true;
            break;
        }
    }

    if(!isPresent) {
        const list = btn.parentNode.children;
        const productImg = list[0].src;
        const productName = list[1].childNodes[1].getAttribute('name');
        const productPrice = Number(list[2].childNodes[1].getAttribute('value'));
        const productDiv = document.createElement("div");
        productDiv.className = "itemBox";

        productDiv.id = `${productId}`;
        productDiv.innerHTML = `<img src=${productImg} alt="Image not found">
                                <p><strong>Name : </strong><span  name=${productName}>${productName}</span></p>
                                <p><strong>Price :</strong><span  name="Price" value="${productPrice}">${productPrice} Rs.</span></p>
                                <button onclick="removeItem(this)">Remove</button>`;
        cartBody.appendChild(productDiv);
    }
});


function addToCart(e){
  const eventAddToCart = new CustomEvent("addToCart", {detail:e});
  document.dispatchEvent(eventAddToCart);
}


function removeItem(e) {
  const tag = e.parentNode;
  tag.remove();
}

