function jsonrpc(rpcId, url, params, settings = {}) {
	var xhttp = new XMLHttpRequest();
	const data = {
		id: rpcId,
    	jsonrpc: "2.0",
    	method: "call",
    	params: params ,
	};
	return new Promise((resolve,reject) => {
    	xhttp.open("POST", url, true);
    	xhttp.setRequestHeader("Content-Type", "application/json");
   		xhttp.send(JSON.stringify(data));
    	xhttp.onload = () => {
        
        	const { error: responseError, result: responseResult }  = JSON.parse(xhttp.response)
        	if (!responseError) {
            	resolve(responseResult);
        	}
        	else {
        		reject(responseError);
        	}
    	}
	});
}

let rpcId=0;
export function rpc(route, params = {}, settings) {
	return jsonrpc(rpcId++, route, params, settings);
}