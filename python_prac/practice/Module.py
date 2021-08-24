import math
import listl as l
print(math.sqrt(16)) 

print(math.celi(2.6))
print(math.floor(2.6))
print(l.a)




fetch("./items.json")

		.then(function(response){
			return response.json();
		})
		.then(function(data){
			appendData(data);
		})
		.catch(function(err){
			console.log("error : "+ err)
		})

	function appendData(data){
		var mainContainer = document.getElementById('myData');
		for (var i=0;i<data.length;i++){
			var div = document.createElement("div");
			div.innerHTML = "id" +data[i].name+"  "+data[i].price;
			mainContainer.appendChild(div);
		}
	}