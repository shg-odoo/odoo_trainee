from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    
    response =Response ('''
        <html>
        <head>
       
        <script language="javascript">
        	function pro1(){
        		var quantity = document.getElementById('que').value;
        		document.getElementById('pro1Disp').innerHTML= "<b>"+"Product Name:- "+"</b>"+"Shirt"+"<br>" +"<b>"+"Qty:-"+ "</b>"+quantity +"<br>"+"<b>"+"Price:-"+"</b>"+"150"+"<br>" +"<b>"+"Total:-"+"</b>"+quantity*150 +"<br>"+"<center>"+"<input type='button' id='remove1' value='Remove' onclick='remove1()'><br><br>"+"</center>";
        	}
           	
           	function remove1(){
              var quantity = document.getElementById('que').value;
           	  document.getElementById('pro1Disp').innerHTML="";
              document.getElementById('que').value="";
           	}
           	function pro2(){
        		var quantity = document.getElementById('que2').value;
        		document.getElementById('pro2Disp').innerHTML= "<b>"+"Product Name:- "+"</b>"+"T-Shirt"+"<br>" +"<b>"+"Qty:-"+ "</b>"+quantity +"<br>"+"<b>"+"Price:-"+"</b>"+"200"+"<br>" +"<b>"+"Total:-"+"</b>"+quantity*200 +"<br>"+"<center>"+"<input type='button' id='remove2' value='Remove' onclick='remove2()'><br><br>"+"</center>";
        	}
           	
           	function remove2(){
              var quantity = document.getElementById('que2').value;
           	  document.getElementById('pro2Disp').innerHTML="";
              document.getElementById('que2').value="";
           	}
           	function pro3(){
        		var quantity = document.getElementById('que3').value;
        		document.getElementById('pro3Disp').innerHTML= "<b>"+"Product Name:- "+"</b>"+"Jeans"+"<br>" +"<b>"+"Qty:-"+ "</b>"+quantity +"<br>"+"<b>"+"Price:-"+"</b>"+"500"+"<br>" +"<b>"+"Total:-"+"</b>"+quantity*500 +"<br>"+"<center>"+"<input type='button' id='remove3' value='Remove' onclick='remove3()'><br><br>"+"</center>";
        	}
           	
           	function remove3(){
              var quantity = document.getElementById('que3').value;
           	  document.getElementById('pro3Disp').innerHTML="";
              document.getElementById('que3').value="";
           	}


        </script>

        <center><h1 style="color : white;text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px darkblue;">Product</h1></center>
        </head>
        <body>
        <div id="hel">
        <div style="padding-left:190px;">
        	<div style="border : 3px solid black; width:250px; height:300px;float: left;margin: 10px;box-shadow: 5px 10px 10px 10px;">
        		<b>ProductName:-</b>Shirt <br><b>Price:-</b>150<br>
       			<b>Enter No of Qty:-</b><input type="text" id="que" name="que"> <br><br><center><input type="button" id="pro1" value="Add to cart" style="margin-right: 80px" onclick="pro1()"></center><br><br><br>
       			<span id="pro1Disp"></span>
       		</div>
       		<div style="border : 3px solid black; width:250px; height:300px;float: left;margin: 10px;box-shadow: 5px 10px 10px 10px;">
        		<b>ProductName:-</b>T-Shirt<br><b>Price:-</b>200<br>
       			<b>Enter No of Qty:-</b><input type="text" id="que2" name="que2"> <br><br><center><input type="button" id="pro2" value="Add to cart" style="margin-right: 80px" onclick="pro2()"></center><br><br><br>
       			<span id="pro2Disp"></span>
       		</div>
       		<div style="border : 3px solid black; width:250px; height:300px;float: left;margin: 10px;box-shadow: 5px 10px 10px 10px;">
        		<b>ProductName:-</b>Jeans <br><b>Price:-</b>500<br>
       			<b>Enter No of Qty:-</b><input type="text" id="que3" name="que3"> <br><br><center><input type="button" id="pro3" value="Add to cart" style="margin-right: 80px" onclick="pro3()"></center><br><br><br>
       			<span id="pro3Disp"></span>
       		</div>
       	</div>

        <br><br>
        </div>
        </body>
        </html>
    ''')
    response.headers['content-type'] = 'text/html'
    return response 

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 1313, application)
