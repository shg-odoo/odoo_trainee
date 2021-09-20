const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class client_Engineer_list extends Component {
     constructor() {
        super(...arguments);
        this.env.bus.on('client_Engineer_list', this, this.client_Engineer_list);
        this.state = useState({
            data: [],
        });

    }

    client_Engineer_list (ev) {
        this.valid=ev.valid
        this.state.data = this.valid

    }
   

    async book_engineer(ev){
        const eng_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/book_engineer');
            xhr.send(JSON.stringify({'eng_id': eng_id,'fname': owl.session_info.fname}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                if(response.book_engineer === "success"){
                    alert("Engineer book successfully")
                    this.env.router.navigate({to:'Orders'});
                }
                else{
                    this.env.router.navigate({to:'home'});
                }
               
            }
        }

    view_engineer_detail(ev){
        const eng_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/view_engineer_detail');
            xhr.send(JSON.stringify({'id': eng_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('view_engineer_detail', {valid: response.view_engineer_detail});
            }
        this.env.router.navigate({ to: 'view_engineer_detail' });

    }



    static template = xml`<div class="container">  
                    <div class="mt-5 mb-5">
                       <h1>Engineers list </h1> 
                    </div>
                    <div>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>id</th>
                                    <th>Email</th>
                                    <th>Mobile No</th>
                                    <th>Specialist</th>
                                    <th>Experience</th>
                                    <th>Action</th>
                                    <th>View</th>
                                </tr>
                            </thead>
                            <tbody>
                                    <t t-foreach="state.data" t-as="i">
                                        <tr>
                                            <td><t t-esc="i.engineer_id"/></td>
                                            <td><t t-esc="i.email"/></td>
                                            <td><t t-esc="i.mobile_no"/></td>
                                            <td><t t-esc="i.specialist"/></td>
                                            <td><t t-esc="i.experience"/></td>
                                            <td><button type="submit" class="btn btn-danger" t-att-id="i.engineer_id" t-on-click="book_engineer">Book</button></td>
                                            <td><button type="submit" class="btn btn-success" t-att-id="i.engineer_id" t-on-click="view_engineer_detail">View</button></td>
                                        </tr>
                                    </t>
                            </tbody>
                        
                        </table>
                    </div>
                    
        </div>`;

        
}

    