const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class view_engineer_detail extends Component {
	constructor() {
        super(...arguments);
        this.env.bus.on('view_engineer_detail', this, this.view_engineer_detail);
        this.state = useState({
            data: [],
        });

    }

    view_engineer_detail (ev) {
        this.valid=ev.valid
        this.state.data = this.valid
    }
	static template = xml`<div>  
        <div>
            <h4 class="container mt-3 mb-3">Engineer Detail</h4>
        </div>
        <div class="d-flex justify-content-center mt-5">
            <div class="card text-center" style="width:35em;">
                <div class="card-header bg-dark text-white">
                    Profile
                </div>
              <div class="card-body">
                    <table style="width:100%">
                    <t t-foreach="state.data" t-as="i">
                        <tr>
                            <th>Name:</th>
                            <td><t t-esc="i.fname"/></td>
                        </tr>
                        <tr>
                            <th>Mobile:</th>
                            <td><t t-esc="i.mobile_no"/></td>
                        </tr>
                        <tr>
                            <th>Email:</th>
                            <td><t t-esc="i.email"/></td>
                        </tr>
                        <tr>
                            <th>Specialist:</th>
                            <td><t t-esc="i.specialist"/></td>
                        </tr>
                        <tr>
                            <th>Experience:</th>
                            <td><t t-esc="i.experience"/></td>
                        </tr>
                    </t>
                    </table>
              </div>
              <div class="card-footer bg-dark texxt-white text-muted">
              </div>
            </div>
        </div></div>`;
}

    