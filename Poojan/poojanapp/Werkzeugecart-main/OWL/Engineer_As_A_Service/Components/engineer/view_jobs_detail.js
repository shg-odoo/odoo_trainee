const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class view_jobs_detail extends Component {
	constructor() {
        super(...arguments);
        this.env.bus.on('view_job_list', this, this.view_job_list);
        this.state = useState({
            data: [],
        });

    }

    view_job_list (ev) {
        this.valid=ev.valid
        this.state.data = this.valid
    }
	
    static template = xml`<div class="container mt-5">
            <div>
                <h3 class="container mb-5" style="font-size:36px;">Service Job Detail</h3>
            </div>
            <table class="table table-striped">
                <thead class="bg-dark text-white">
                    <tr>
                        <th data-field="key" scope="col" class="key">Key</th>
                        <th data-field="value" scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    <t t-foreach="state.data" t-as="task">
                    <tr>
                        <td>Id</td>
                        <td><t t-esc="task.order_id" /></td>
                    </tr>
                    <tr>
                        <td>Name</td>
                        <td><t t-esc="task.client_name" /></td>
                    </tr>
                     <tr>
                        <td>Order Date</td>
                        <td>
                            <t t-esc="task.created_day" />/
                            <t t-esc="task.created_month" />/
                            <t t-esc="task.created_year" />
                        </td>
                    </tr>
                    <tr>
                        <td>Order Time</td>
                        <td>
                            <t t-esc="task.created_hour" />:
                            <t t-esc="task.created_minute" />
                        </td>
                    </tr>
                    <tr>
                        <td>Mobile No</td>
                        <td><t t-esc="task.mobile_no" /></td>
                    </tr>
                    <tr>
                        <td>Specialist</td>
                        <td><t t-esc="task.email" /></td>
                    </tr>
                    <tr>
                        <td>experience</td>
                        <td><t t-esc="task.address" /></td>
                    </tr>
                    </t>
                </tbody>
            </table>
        </div>`;
    }

    