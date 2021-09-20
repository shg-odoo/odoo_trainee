const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class Login extends Component {
    constructor() {
        super(...arguments);
        this.state = useState({
            invalid: undefined
        });
    }
    
    OnLoginsubmit(ev){
        const xhr = new window.XMLHttpRequest();
        xhr.open('POST', '/do_login');
        const formData = new FormData(ev.currentTarget);
        xhr.send(JSON.stringify(Object.fromEntries(formData.entries())));
        xhr.onload = async () => {
            
            const response = JSON.parse(xhr.response);
            console.log(response.role);
            if (response.email === false)
            {
                this.state.invalid = "email is wrong";
            }
            else if(response.pass === false) 
            {
                this.state.invalid = "password is wrong";
            }
            else if(response.role === "engineer"){
                document.cookie = `session_id=${response.session_id}`;
                owl.session_info = {
                    user_id: response.user_id,
                    fname: response.fname,
                    is_valid: response.is_valid,
                    session_id: response.session_id,
                    role: response.role
                }
                alert("engineer login")
                this.env.bus.trigger('login_changed');
                this.env.router.navigate({to:'HomeEngineer'});
            }
            else if(response.role === "client"){
                document.cookie = `session_id=${response.session_id}`;
                owl.session_info = {
                    user_id: response.user_id,
                    fname: response.fname,
                    is_valid: response.is_valid,
                    session_id: response.session_id,
                    role: response.role
                }
                alert("client login")
                this.env.bus.trigger('login_changed');
                this.env.router.navigate({to:'HomeClient'});
            }
        };
    }

    static template = xml`<div>
        <div class="container mt-5">
            <h1 class="mb-4">Login Here</h1>
            <form action="#" t-on-submit.prevent="OnLoginsubmit">
                <div class="form-group">
                    <label for="email">Email address:</label>
                    <input type="email" class="form-control" name="email" placeholder="Enter email" id="email" required="true"/>
                </div>
                <div class="form-group">
                    <label for="pwd">Password:</label>
                    <input type="password" class="form-control" name="password" placeholder="Enter password" id="pwd" required="true"/>
                </div>
                <div class="text text-danger"><t t-esc="state.invalid"/></div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>`;
}

    