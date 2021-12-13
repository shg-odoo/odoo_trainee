import {Header} from './header.js';
import {Footer} from './footer.js';
import {Content} from './content.js';

class App {
    mount() {
        let headerobj = new Header(document.querySelector('.header-container'));
        headerobj.render();

        let content = new Content();
        content.mount(document.querySelector('.content'));

        let footer = new Footer(document.querySelector('.footer-container'));
        footer.render();
        
    }
};

window.onload = function() {
    let objofapp = new App(document.querySelector('body'));
    objofapp.mount();

  	
};

