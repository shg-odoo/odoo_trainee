import { Header } from "./header.js";
import { Content } from "./content.js";
import { Footer } from "./footer.js";

const { Component, Store, mount } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;

//store
const actions = {
  addItem({ state }, item) {
    const isPresent = state.items.find((i) => i.productId === item.productId);
    if(!isPresent) {
        state.items.push(item);
    }
  },

  removeItem({ state }, item) {
    const index = state.items.findIndex( (i) => i.productId == item.productId);
    state.items.splice(index,1);
  },
};

const initialState = {
  items: [],
};

class App extends Component {
    static template = "App";
    static components = { Header, Content, Footer }; 
}


const setup = async () => {
    const xmlTemplates = await fetch('static/xml/app.xml');
    const xmlTemplateText = await xmlTemplates.text();
    const bus = new owl.core.EventBus();
     const store = new Store({ actions, state: initialState });
    const env = {
        qweb: new owl.QWeb(),
        bus: bus,
        store: store
    };
    env.qweb.addTemplates(xmlTemplateText);
    mount(App, {env, target: document.body });
};

whenReady(setup);