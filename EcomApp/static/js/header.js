
export class Header {
    constructor(targetELm) {
        this.target = targetELm;
    }
    render() {
        let headerRenderdata = `
        <header class="main-header">
        <nav class="main-nav nav">
            <ul>
                <li><a href="store.html">STORE</a></li>
            </ul>
        </nav>
        <h1 class="band-name band-name-large">Here and Now</h1>
    </header>
    <h2 class="section-header">Clothing</h2>
    <section class="container content-section">
        <div class="shop-items" id="myData">

        </div>
    </section>
        `;

        this.target.innerHTML = headerRenderdata;
    }
};