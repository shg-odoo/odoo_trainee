const { Component, mount } = owl;
const { useRef } = owl.hooks;

export class Header extends Component {
    static template = "Header";

    inputRef = useRef("search-text");

    mounted() {
        this.inputRef.el.focus();
    }

    searchProducts() {
        const text = this.inputRef.el.value;
        if(text !== "") {
            this.env.bus.trigger("searchProducts", { searchText: text });
        }
        else {
            alert("Enter valid input to search");
        }
    }

    search(ev) {
        if(ev.keyCode == 13) {
            this.searchProducts();
        }
    }
}
