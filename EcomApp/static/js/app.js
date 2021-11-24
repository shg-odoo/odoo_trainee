import { Header } from './header.js'
import { Footer } from './footer.js'
import { Content } from './content.js'
class Application {
  constructor() {

  }
  mount() {
    //HEADER OBJECT
    let headerobj = new Header(document.querySelector('.header-container'));
    headerobj.render();

    //FOOTER OBJECT 
    let footerobj = new Footer(document.querySelector('.footer-alldata'));
    footerobj.render();
    
    //Content Container
    $.ajax({
      type: "POST",
      url: "/get_products",
    })
      .done(function (data) {
        let jsondata = data["result"];
        let products = JSON.parse(jsondata);
        this.contentobj = new Content(products, document.querySelector('.content-section'));
        this.contentobj.el = this.contentobj.render()
      });
  }
};
window.onload = function () {
  let appobj = new Application(document.querySelector('body'));
  appobj.mount();
}
