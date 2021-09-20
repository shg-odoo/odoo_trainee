const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class HeaderComponent extends Component {

    constructor() {
        super(...arguments);
        this.env.bus.on('login_changed', this, this._loginChanged);
        // this.env.bus.on('session_val', this, this.session_val);
        this._updateState();
    }




    _updateState() {
        this.state = useState({
            user_id: owl.session_info.user_id,
            fname: owl.session_info.fname,
            is_valid: owl.session_info.is_valid,
            session_id: owl.session_info.session_id,
            role: owl.session_info.role
        });
    }
    // before loging
    Home(){
         this.env.router.navigate({ to: 'home' });
    }
    signup(){
         this.env.router.navigate({ to: 'signup' });
    }
    login(){
         this.env.router.navigate({ to: 'login' });
    }
    // engineer
    HomeEngineer(){
         this.env.router.navigate({ to: 'HomeEngineer' });
    }
    engineers(){
         this.env.router.navigate({ to: 'engineers' });
    }
    jobs(ev){
        const user_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_fetch_jobs');
            xhr.send(JSON.stringify({'user_id': user_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('arrives_jobs', {valid: response.arrives_jobs});
            }
        this._updateState();
        this.env.router.navigate({ to: 'jobs' });       
    }
    Engineer_profile(ev){
        const user_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_fetch_engineer_profile');
            xhr.send(JSON.stringify({'user_id': user_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                console.log(response)
                this.env.bus.trigger('client_Engineer_profile', {valid: response.engineer_profile});
            }
        this.env.router.navigate({ to: 'Engineer_profile' });
    }
    new_jobs_engineer(){
         this.env.router.navigate({ to: 'new_jobs_engineer' });
    }
    // client
    homeclient(){
         this.env.router.navigate({ to: 'HomeClient' });
    }
    client_Engineer_list(ev){
                const xhr = new window.XMLHttpRequest();
                xhr.open('POST', '/client_engineer_list');
                xhr.send(JSON.stringify({'session_id': 'blank'}));
                xhr.onload = async () => {
                    const response = JSON.parse(xhr.response);
                    this.env.bus.trigger('client_Engineer_list', {valid: response.engineer_list});
                }
                this.env.router.navigate({ to: 'client_Engineer_list' });
    }
    
    Orders(ev){
        const eng_name = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_fetch_orders');
            xhr.send(JSON.stringify({'fname': eng_name}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('client_orders_list', {valid: response.engineer_list});
            }
            this.env.router.navigate({ to: 'Orders' });
    }

    client_profile(ev){debugger
        const user_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_fetch_client_profile');
            xhr.send(JSON.stringify({'user_id': user_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('client_client_profile', {valid: response.client_profile});
            }
        this.env.router.navigate({ to: 'client_profile' });
    }

    logout(ev){
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_logout');
            xhr.send(JSON.stringify({'session_id': this.state.session_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                if (response.logout === 'success') {
                    document.cookie = 'session_id=null';
                    owl.session_info = {
                        user_id: null,
                        fname:null,
                         is_valid: false,
                        session_id: null,
                        role: null,
                    };
                    this._updateState();
                    this.env.router.navigate({ to: 'home' });
                }
            }
        }
  
    
    _loginChanged (ev) {
        this._updateState();
    }
   


    static template = xml`<div>
        <nav class="navbar navbar-expand-md  navbar-light bg-info">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <t t-if="state.user_id and state.is_valid">
                        <t t-if="state.role === 'engineer'">
                            <a class="navbar-brand" t-on-click="HomeEngineer">LOGO</a>
                                <li class="nav-item active">
                                   <button class="nav-link btn-warning mr-2" t-on-click="HomeEngineer">Home</button>
                                </li>
                                <li class="nav-item">
                                    <button class="nav-link btn-warning mr-2" href="#" t-att-id="state.user_id" t-on-click="jobs">Jobs</button>
                                </li>
                                <li class="nav-item">
                                    <button class="nav-link btn-warning mr-2" href="#" t-att-id="state.user_id" t-on-click="Engineer_profile">Profile</button>
                                </li>
                                <li class="nav-item">
                                    <button class="nav-link btn-warning ml-3" href="#" t-on-click="logout">Logout</button>
                                </li> 
                        </t>
                        <t t-else="">
                        <a class="navbar-brand" t-on-click="homeclient">LOGO</a>
                            <li class="nav-item active">
                               <button class="nav-link btn-warning mr-2" t-on-click="homeclient">Home</button>
                            </li>
                            <li class="nav-item">
                                    <button class="nav-link btn-warning mr-2" href="#" t-on-click="client_Engineer_list">Engineers</button>
                            </li>
                            <li class="nav-item">
                                    <button class="nav-link btn-warning mr-2" href="#" t-att-id="state.fname" t-on-click="Orders">Orders</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning mr-2" href="#" t-att-id="state.user_id" t-on-click="client_profile">Profile</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning ml-3" href="#" t-on-click="logout">Logout</button>
                            </li>
                        </t>
                        <li style="margin-left: 700px;">
                            <h5> <t t-esc="'welcome '+state.fname" /></h5>
                        </li>
                    </t>     
                    <t t-else="">
                        <a class="navbar-brand" t-on-click="Home">LOGO</a>
                        <li class="nav-item active">
                           <button class="nav-link btn-warning mr-2" t-on-click="Home">Home</button>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link btn-warning mr-2" href="#" t-on-click="login">Login</button>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link btn-warning mr-2" href="#" t-on-click="signup">Signup</button>
                        </li>
                    
                    </t>
                </ul>
                
            </div>
        </nav>
        </div>`;
}