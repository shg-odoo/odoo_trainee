const { Component, mount } = owl;
const { xml } = owl.tags;


export class FooterComponent extends Component {
  static template = xml`<div>
                                <nav class="navbar navbar-expand-lg navbar-light bg-info mb-0 mt-5 fix-bottom" >
                                      <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                       <h3>@Engineer as a service</h3>
                                      </div>
                                    </nav>
                                </div>`;
    
}