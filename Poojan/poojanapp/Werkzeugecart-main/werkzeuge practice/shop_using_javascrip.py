from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    
    response =Response ('''
        <html>
        <head>
       
        <script language="javascript">
        	function pro1(){
        		var quantity = document.getElementById('que').value;
        		document.getElementById('pro1Disp').innerHTML= "Shirt  ->   " + quantity +"  *150  =" +quantity*150 + "<input type='button' id='remove1' value='Remove' onclick='remove1()'><br><br>";
        	}
           	
           	function remove1(){
              var quantity = document.getElementById('que').value;
           	  document.getElementById('pro1Disp').innerHTML="";
              document.getElementById('que').value="";
           	}



           	function pro2(){
        		var quantity2 = document.getElementById('que2').value;
        		document.getElementById('pro2Disp').innerHTML= "Cap  ->   " + quantity2 +"  *800  =" +quantity2*800 + "<input type='button' id='remove2' value='Remove' onclick='remove2()'><br><br>";
        	}
           	
           	function remove2(){
                var quantity2 = document.getElementById('que2').value;
                document.getElementById('que2').value="";
                document.getElementById('pro2Disp').innerHTML="";
           	}



           	function pro3(){
        		var quantity3 = document.getElementById('que3').value;
        		document.getElementById('pro3Disp').innerHTML= "Trouser  ->   " + quantity3 +"  *1500  =" +quantity3*800 + "<input type='button' id='remove3' value='Remove' onclick='remove3()'><br><br>";
        	}
           	
           	function remove3(){
           		document.getElementById('pro3Disp').innerHTML="";
                var quantity3 = document.getElementById('que3').value;
                document.getElementById('que3').value="";
           	}


           	function pro4(){
        		var quantity4 = document.getElementById('que4').value;
        		document.getElementById('pro4Disp').innerHTML= "Shorts  ->   " + quantity4 +"  *2000  =" +quantity4*2000 + "<input type='button' id='remove4' value='Remove' onclick='remove4()'><br><br>";
        	}
           	
           	function remove4(){
           	   document.getElementById('pro4Disp').innerHTML="";
               var quantity4 = document.getElementById('que4').value;
               document.getElementById('que4').value="";


           	}


           	function pro5(){
        		var quantity5 = document.getElementById('que5').value;
        		document.getElementById('pro5Disp').innerHTML= "Jacket  ->   " + quantity5+"  *5000  =" +quantity5*5000 + "<input type='button' id='remove5' value='Remove' onclick='remove5()'><br><br>";
        	}
           	
           	function remove5(){
           		document.getElementById('pro5Disp').innerHTML="";
                var quantity5 = document.getElementById('que5').value;
                document.getElementById('que5').value="";

           	}
        </script>

        <center><h1>Shop.com</h1></center>
        </head>
        <body bgcolor="cyan">
        <div id="hel">
        <center>
        <table>
        <tr>
            <td>
                 <h1><b>Shirt</b> 150</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que" name="que"> <input type="button" id="pro1" value="Add to cart" style="margin-right: 80px" onclick="pro1()"></td><br><br><br>
            <td><span id="pro1Disp"></span>  </td>
        </tr>


        <tr>
            <td>
                <h1><b>Cap</b> 800</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que2"> <input type="button" id="pro2" value="Add to cart" style="margin-right: 80px" onclick="pro2()"></td>
             <td><span id="pro2Disp"></span></td> 
        </tr>

         <tr>
            <td>
                <h1><b>Trouser</b> 1500</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que3"> <input type="button" id="pro3" value="Add to cart" style="margin-right: 80px" onclick="pro3()"></td>
            <td><span id="pro3Disp"></span></td> 
        </tr>


        <tr>
            <td>
                 <h1><b>shorts</b> 2000</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que4"> <input type="button" id="pro4" value="Add to cart" style="margin-right: 80px" onclick="pro4()"></td>
            <td><span id="pro4Disp"></span></td> 
        </tr>

        <tr>
            <td>
                <h1><b>jacket</b> 5000</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que5"> <input type="button" id="pro5" value="Add to cart" style="margin-right: 80px" onclick="pro5()"></td>
            <td><span id="pro5Disp"></span></td>
        </tr>

        <br><br>

        </center>

        <table>
        <br><br>
        </div>
        </body>
        </html>
    ''')
    response.headers['content-type'] = 'text/html'
    return response 

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application)
