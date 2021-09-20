(function () {
  console.log("hello owl", owl.__info__.version);
})();

const { Component} = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;

// Owl Components
class App extends Component {
  static template = xml`<div style="font-size: 200px;" t-on-click="increment"><t t-esc="state.value"/></div>`;
  state = { value : 0 };

  increment(){
  	this.state.value++;
  	this.render()
  }
}

// Setup code
function setup() {
  const app = new App();
  app.mount(document.body);
}

whenReady(setup);