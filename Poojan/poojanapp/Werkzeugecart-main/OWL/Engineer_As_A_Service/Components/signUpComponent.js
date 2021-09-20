const { Component, mount, useState } = owl;
const { xml } = owl.tags;

export class Signup extends Component {
        constructor() {
        super(...arguments);
        this.state = useState({
            pwd: "",
            repwd: "",
            pwmatch: undefined,
            invalid_eml:"",
        });
    }

    onFormSubmit(ev){
        const xhr = new window.XMLHttpRequest();
        xhr.open('POST', '/do_signup');
        const formData = new FormData(ev.currentTarget);
        xhr.send(JSON.stringify(Object.fromEntries(formData.entries())));
        xhr.onload = async () => {
            const response = JSON.parse(xhr.response);
            console.log(response)
            if (response.credentials === false) {
                this.state.invalid_eml = "Emailid already exist";
            }
            else{
                alert("registeration Successfullly")
                this.env.router.navigate({to:'login'});
            }
        };
    }
  

    _checkPwd() {
        if (!this.state.pwd || !this.state.repwd) {
            return;
        }
        if (this.state.pwd === this.state.repwd) {
            this.state.pwmatch = true;
            this.el.querySelector('button[type="submit"]').removeAttribute('disabled');
        } else {
            this.state.pwmatch = false;
            this.el.querySelector('button[type="submit"]').setAttribute('disabled', true);
        }
    }

    _onKeyUpRePwd(ev) {
        this._checkPwd();
    }

    _onKeyUpPwd(ev) {
        this._checkPwd();
    }
    signup_engineer(ev){
         this.env.router.navigate({ to: 'signup_engineer' });
    }
    
    

   static template = xml`<div>
        <div class="container mt-5">
        <h1>SignUp Here</h1>
        <div class="mb-5 mt-5">
        <label for="engineer_signup">Are you want to join as a engineer ? </label>
        <button type="button" class="btn btn-primary ml-2" t-on-click="signup_engineer">Engineer</button>
        </div>
        <form action="#" t-on-submit.prevent="onFormSubmit">
            <div id="customer">
                 <h2 class="mb-3">Customer Signup</h2>
                <div class="form-group">
                    <label for="email">Email address:</label>
                    <input type="email" class="form-control" placeholder="Enter email" name="email" id="email" required="true"/>
                </div>
                <div class="form-group">
                    <label for="fname">Name:</label>
                    <input type="text" class="form-control" placeholder="Enter Name" name="fname" id="fname" required="true"/>
                </div>
                <div class="form-group">
                    <label for="pwd">Password:</label>
                    <input type="password" t-model="state.pwd" t-on-keyup="_onKeyUpPwd" class="form-control" placeholder="Enter password" name="password" id="pwd" required="true"/>
                </div>
                <div class="form-group">
                    <label for="repwd">Re-Enter Password:</label>
                    <input type="password" t-model="state.repwd" t-on-keyup="_onKeyUpRePwd" class="form-control" placeholder="Enter password" name="repwd" id="repwd" required="true"/>
                </div>
                <div t-if="state.pwmatch === false">
                    <h4>Password Does not match</h4>
                </div>
                <div class="form-group">
                    <label for="Address">Address:</label>
                    <input type="text" class="form-control" placeholder="Enter Address" name="address" id="add" required="true"/>
                </div>
                <div class="form-group">
                    <label for="mobile-no">Mobile No:</label>
                    <input type="text" class="form-control" placeholder="Enter Mobile number" name="mobno" id="mobile-no" required="true"/>
                </div>
                <div class="text text-danger"><t t-esc="state.invalid_eml"/></div>
                <button type="submit" class="btn btn-primary ml-2" disabled="True">Submit</button>
            </div>
        </form>
        </div>
        </div>`;
}