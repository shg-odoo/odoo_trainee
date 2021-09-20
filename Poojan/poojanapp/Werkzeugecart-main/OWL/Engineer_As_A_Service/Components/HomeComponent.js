const { Component, mount } = owl;
const { xml } = owl.tags;


export class Home extends Component {
  static template = xml`<div>   
                                <div class="mb-5 ml-5 mt-5">
                                <div class="row">
                                    <div class="col-sm-6"><br></br>
                                        <h3><font color="orange"> Best Solution of your Product</font> </h3><br></br>
                                        <h1><font color="orange">We have the amzing staff of engineer</font></h1><br></br>
                                       
                                        <button t-on-click="Signup" class="btn btn-dark">Get started</button>
                                        <button t-on-click="Login" class="btn btn-danger ml-3">Login</button>
                                    </div>
                                    <div class="col-sm-6">
                                        <img src="static/images/engineer.jpg" class="img-fluid mt-5 rounded zoom" alt="Responsive image"/>
                                    </div>
                                </div>
                            </div>
                            </div>`;
    Login(ev){
         this.env.router.navigate({ to: 'login' });
    }
    Signup(ev){
         this.env.router.navigate({ to: 'signup' });
    }
        
}

    