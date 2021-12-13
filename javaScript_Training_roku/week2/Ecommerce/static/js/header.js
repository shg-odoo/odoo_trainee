export class Header {
    constructor(targetElement) {
        this.target = targetElement;
    }
    render() {
        let headerdata =`<div class="logo"><img class="logoimg" src="./static/images/logo2.png"></div>
                        <header class="main-header">
                            <nav class="main-nav nav">
                                <li>Home</li>
                                <li>About Us</li>
                                <li>Fruits</li>
                                <li>Contact</li>
                                <div>
                                    <input type="text"  class="Searchtext" placeholder="Search.." name="search" >
                                    <button class="btnSearch" >search</button>
                                </div>
                            </nav>
                            <marquee behavior="scroll" direction="left" class="scroll">***Welcome To Roku Mart.... Take your Favourite Fruits</marquee>
                        </header>
                        `;
        this.target.innerHTML = headerdata;
        this.target.querySelector('.btnSearch').addEventListener('click',this.SearchProduct.bind(this));
    }
    SearchProduct(){
        const text = this.target.querySelector('.Searchtext').value;
        const SearchProductEvent = new CustomEvent("DisplaySearchProduct", {detail : { searchText : text }});
        window.dispatchEvent(SearchProductEvent);
    }

};
