import { ProductItem } from './product-item.js';
export class ProductList {
	constructor(target) {
		this.target = target;
		window.addEventListener("displaySearchedResult",this.displaySearchedResult.bind(this));
	}

	async mount() {
		await this.willStart();
		this.displayProducts();
	}

	willStart() {
		return this.fetchProducts('/products').then((products) => {
			this.data = products
  		}, function (error) {
    		console.log(error);
  		});
	}

	fetchProducts(urlString) {
		const xhr = new XMLHttpRequest();
		xhr.open('POST', urlString);

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

	displayProducts() {
		const keys = [];
		for (let k in this.data) keys.push(k);
  		this.target.innerHTML = "";
  		keys.forEach(category => {
  			const mainDiv = document.createElement("div");
    		mainDiv.className = "container";

    		const h1 = document.createElement("h1");
    		h1.innerHTML = category;

    		mainDiv.appendChild(h1);

    		const subDiv = document.createElement("div");

    		this.data[category].forEach(product => {
      			const productItem = new ProductItem(product);
      			productItem.mount(subDiv);
    		});

    		mainDiv.appendChild(subDiv);
    		this.target.appendChild(mainDiv);
  		});
	}

	searchProducts(urlString) {
		return this.fetchProducts(urlString).then((result) => {
			debugger;
			this.data = result
  		}, function (error) {
    		console.log(error);
  		});
	}

	async displaySearchedResult(ev) {
		const searchText = ev.detail.searchText;
		await this.searchProducts(`/search?searchText=${searchText}`);

		if(Object.keys(this.data).length != 0) {
			this.displayProducts();	
		}
		else {
			this.target.innerHTML =`<center style="margin:30%">
										<h1>No items found!!!!!!!</h1>
									</center>`;
		}
	}
} 