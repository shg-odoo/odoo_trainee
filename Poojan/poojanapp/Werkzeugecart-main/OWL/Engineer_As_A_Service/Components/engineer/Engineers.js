const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class client_Engineer_list extends Component {
	 constructor() {
        super(...arguments);
        // this.env.bus.on('session_val', this, this.session_val);
        this.state = useState({
            'engineer_id': users.engineer_list.engineer_id,
            'email': users.engineer_list.email,
            'specialist': users.engineer_list.specialist,
            'mobile_no': users.engineer_list.mobile_no,
            'experience': users.engineer_list.experience,
        });

    }

    async book_engineer(ev){debugger
        console.log(this.state.email)
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/book_engineer');
            xhr.send(JSON.stringify(this.state));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                if(response.book_engineer === "success"){
                    this.env.router.navigate({to:'jobs'});
                }
                else{
                    this.env.router.navigate({to:'homee'});
                }
               
            }
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
    								<th>Specialist</th>
    								<th>Mobile No</th>
    								<th>Experience</th>
                                    <th>Action</th>
    								<th>View</th>
    							</tr>
    						</thead>
    						<tbody>
        							<tr>
        								<td><t t-esc="state.engineer_id" /></td>
        								<td><t t-esc="state.email" /></td>
        								<td><t t-esc="state.specialist" /></td>
        								<td><t t-esc="state.mobile_no" /></td>
        								<td><t t-esc="state.experience" /></td>
        								<td><button type="submit" class="btn btn-danger" t-on-click="book_engineer">Book</button></td>
                                        <td><button type="submit" class="btn btn-success">View</button></td>
        							</tr>
    						</tbody>
    					
    					</table>
                    </div>
					
		</div>`;

        
}

    