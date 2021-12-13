export class Footer{
	constructor(targetElement) {
        this.target = targetElement;
    }
    render() {
        let footerdata = `
        <Footer class="main-footer">
        <nav class="main-navv nav">
            <h3>Fresh Fruits</h3>
            <p>Fruits are an excellent source of essential vitamins and minerals, and they are high in fiber</p>
            <ul>
                <li></li>
            </ul>
        </nav>
    	</Footer>
        `;
        this.target.innerHTML = footerdata;
    }
};

