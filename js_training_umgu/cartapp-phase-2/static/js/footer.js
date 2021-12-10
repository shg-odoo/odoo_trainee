export class Footer {
	mount(target) {
		const footer = document.createElement("footer");
		footer.className = "page-footer font-small blue";
		footer.innerHTML = window.qweb.render("Footer");
		target.appendChild(footer);
	}

}