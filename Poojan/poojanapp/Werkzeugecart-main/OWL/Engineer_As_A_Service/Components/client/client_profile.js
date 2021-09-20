const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class client_profile extends Component {
	  constructor() {
        super(...arguments);
        this.env.bus.on('client_client_profile', this, this.client_client_profile);
        this.state = useState({
            data: [],
        });

    }

    client_client_profile (ev) {
        this.state.data = ev.valid
    }

  	static template = xml`<div class="d-flex justify-content-center mt-5">
						<div class="card text-center" style="width:35em;">
						  <div class="card-header">
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
								    <th>Address:</th>
								    <td><t t-esc="i.address"/></td>
								  </tr>
								</t>
								</table>
						  </div>
						  <div class="card-footer text-muted">
						  </div>
						</div>
						</div>`;
}

    