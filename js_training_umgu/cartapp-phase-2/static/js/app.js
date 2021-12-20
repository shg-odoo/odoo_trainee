import { Header } from './header.js' ;
import { Footer } from './footer.js' ;
import { Content } from './content.js' ;

class App {

  mount(body) {
    const header = new Header();
    header.mount(body)
    const content = new Content();
    content.mount(body)
    const footer = new Footer();
    footer.mount(body)
  }
}

window.addEventListener('DOMContentLoaded', init);

async function init() {
  window.qweb = new QWeb2.Engine();

  const xmlTemplate = await fetch('static/xml/app.xml');
  const xmlTemplateText = await xmlTemplate.text();
  debugger;
  window.qweb.add_template(xmlTemplateText);

  const app = new App();
  app.mount(document.body);
}



