export class Footer{
    constructor(targetELm) {
        this.target = targetELm;
    }
    render() {
        let footerRenderdata = `
        <footer class="main-footer">
            <div class="container main-footer-container">
                <h3 class="band-name">Here and Now</h3>
                <ul class="nav footer-nav">
                    <li>
                        <a href="https://www.youtube.com" target="_blank">
                            <img src="../static/images/ytlogo.png">
                        </a>
                    </li>
                    <li>
                        <a href="https://www.spotify.com" target="_blank">
                            <img src="../static/images/Spotify.png">
                        </a>
                    </li>
                    <li>
                        <a href="https://www.facebook.com" target="_blank">
                            <img src="../static/images/fblogo.png">
                        </a>
                    </li>
                </ul>
            </div>
        </footer>
        `;
    
        this.target.innerHTML = footerRenderdata;
    }
};