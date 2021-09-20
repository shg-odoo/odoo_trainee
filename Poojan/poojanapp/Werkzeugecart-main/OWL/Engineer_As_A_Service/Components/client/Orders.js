const { Component, mount,useState } = owl;
const { xml } = owl.tags;


export class Orders extends Component {
    constructor() {
        super(...arguments);
        this.env.bus.on('client_orders_list', this, this.client_orders_list);
        this.state = useState({
            data: [],
            fname: owl.session_info.fname,
        });
    }
    client_orders_list (ev) {
        this.valid=ev.valid
        this.state.data = this.valid
    }

    view_orders_detail(ev){
        const order_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/view_orders_detail');
            xhr.send(JSON.stringify({'order_id': order_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('view_orders_detail', {valid: response.view_orders_detail});
            }
        this.env.router.navigate({ to: 'view_orders_detail' });
    }
    
    static template = xml`<div class="container">  
                    <div class="mt-5 mb-5">
                       <h1>Orders list </h1> 
                    </div>
                    <div>
                        <table class="table" style="width:50%">
                            <thead>
                                <tr>
                                    <th>id</th>
                                    <th>Name</th>
                                    <th>Order Date</th>
                                    <th>Order Time</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                    <t t-foreach="state.data" t-as="task" t-key="task.id">
                                        <tr>
                                            <td><t t-esc="task.order_id" /></td>
                                            <td><t t-esc="task.fname" /></td>
                                            <td>
                                                <t t-esc="task.created_day" />/
                                                <t t-esc="task.created_month" />/
                                                <t t-esc="task.created_year" />
                                            </td>
                                             <td>
                                                <t t-esc="task.created_hour" />:
                                                <t t-esc="task.created_minute" />
                                            </td>
                                            <td><button type="submit"  t-att-id="task.order_id" t-on-click="view_orders_detail" class="btn btn-success">View</button></td>
                                        </tr>
                                    </t>
                            </tbody>
                        
                        </table>
                    </div>
                    
        </div>`;
    }

    
