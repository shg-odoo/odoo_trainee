export class Header {
	mount(target) {
		this.header = document.createElement("header");
		this.header.innerHTML = window.qweb.render("Header");
		target.appendChild(this.header);	
		this.header.querySelector("#search-btn").addEventListener('click', this.searchResult.bind(this));
	}

	searchResult() {
		const text = this.header.querySelector("#input-text").value;
		if(text !== "") {
			const searchEvent = new CustomEvent("displaySearchedResult", { detail: {searchText :  text } });
  			window.dispatchEvent(searchEvent);
		}
		else {
			alert("Enter the correct input to search");
		}
	}
}