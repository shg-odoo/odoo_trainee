const { Component, mount } = owl;
const { xml } = owl.tags;


export class HomeEngineer extends Component {
  static template = xml`<div class="container">   
                                <div class="mb-5 ml-5 mt-5">
                                <div class="row">
                                    <div class="col-sm-6"><br></br>
                                        <h3><font color="orange">You Are In Our Engineer Team</font> </h3><br></br>
                                        <h1><font color="orange">Give your Best</font></h1><br></br>
                                       
                                        <button  class="btn btn-dark">Get started</button>
                                        <button  class="btn btn-danger ml-3">Jobs</button>
                                    </div>
                                    <div class="col-sm-6">
                                        <img src="static/images/eng.jpg" class="img-fluid mt-2 rounded zoom" alt="Responsive image"/>
                                    </div>
                                </div>
                            </div>
                            </div>`;
}

    