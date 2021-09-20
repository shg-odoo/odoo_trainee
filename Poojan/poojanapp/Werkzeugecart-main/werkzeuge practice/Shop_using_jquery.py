from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    
    response =Response ('''
        <html>
        <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
        <script>
            $(document).ready(function(){ 
          
                var quantity = $('#que').val();
                if(quantity=="")
                {
                    $("#pro1").click(function()
                    { 
                        var quantity = $('#que').val();
                        $("#pro1Disp").text("Shirt     ->    ");
                        $("#pro1Disp").append(+ quantity + ' * 150=');
                        pro1total = quantity * 150
                        $("#pro1Disp").append(+pro1total+ '  ');
                        var html ='<input type="button" id="remove1" value="Remove"><br><br>'
                        $("#pro1Disp").append(html) 

                        $("#remove1").click(function(){
                            $("#que").val("");
                            $("#pro1Disp").empty();
                        });
                    });

                    $("#pro2").click(function()
                    { 
                        var quantity = $('#que2').val();
                        $("#pro2Disp").text("Cap     ->    ");
                        $("#pro2Disp").append(+ quantity + ' * 800=');
                        pro2total = quantity * 800
                        $("#pro2Disp").append(+pro2total+ '  ');
                         var html ='<input type="button" id="remove2" value="Remove"><br><br>'
                        $("#pro2Disp").append(html) 

                        $("#remove2").click(function(){
                            $("#que2").val("");
                            $("#pro2Disp").empty();
                         });
                    });

                    $("#pro3").click(function()
                    { 
                        var quantity = $('#que3').val();
                        $("#pro3Disp").text("Cap     ->    ");
                        $("#pro3Disp").append(+ quantity + ' * 1500=');
                        pro3total = quantity * 1500
                        $("#pro3Disp").append(+pro3total+ '  ');
                         var html ='<input type="button" id="remove3" value="Remove"><br><br>'
                        $("#pro3Disp").append(html) 

                        $("#remove3").click(function(){
                            $("#que3").val("");
                            $("#pro3Disp").empty();
                         });
                    });

                    $("#pro4").click(function()
                    { 
                        var quantity = $('#que4').val();
                        $("#pro4Disp").text("Shorts     ->    ");
                        $("#pro4Disp").append(+ quantity + ' * 2000=');
                        pro4total = quantity * 2000
                        $("#pro4Disp").append(+pro4total+ '  ');
                         var html ='<input type="button" id="remove4" value="Remove"><br><br>'
                        $("#pro4Disp").append(html) 

                        $("#remove4").click(function(){
                            $("#que4").val("");
                            $("#pro4Disp").empty();
                         });
                    });

                    $("#pro5").click(function()
                    { 
                        var quantity = $('#que5').val();
                        $("#pro5Disp").text("Jacket     ->    ");
                        $("#pro5Disp").append(+ quantity + ' * 5000=');
                        pro5total = quantity * 5000
                        $("#pro5Disp").append(+pro5total+ '  ');
                         var html ='<input type="button" id="remove5" value="Remove"><br><br>'
                        $("#pro5Disp").append(html) 

                        $("#remove5").click(function(){
                            $("#que5").val("");
                            $("#pro5Disp").empty();
                         });
                    });
                }
        }); 
        </script>

        <center><h1<b>Shop.com</b></h1></center>
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
            <td>  <input type="text" id="que" name="que"> <input type="button" id="pro1" value="Add to cart" style="margin-right: 80px"></td><br><br><br>
            <td><span id="pro1Disp"></span>  </td>
        </tr>


        <tr>
            <td>
                <h1><b>Cap</b> 800</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que2"> <input type="button" id="pro2" value="Add to cart" style="margin-right: 80px"></td>
             <td><span id="pro2Disp"></span></td> 
        </tr>

         <tr>
            <td>
                <h1><b>Trouser</b> 1500</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que3"> <input type="button" id="pro3" value="Add to cart" style="margin-right: 80px"></td>
            <td><span id="pro3Disp"></span></td> 
        </tr>


        <tr>
            <td>
                 <h1><b>shorts</b> 2000</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que4"> <input type="button" id="pro4" value="Add to cart" style="margin-right: 80px"></td>
            <td><span id="pro4Disp"></span></td> 
        </tr>

        <tr>
            <td>
                <h1><b>jacket</b> 5000</h1>
            </td>
        </tr>
        <tr>
            <td>  <input type="text" id="que5"> <input type="button" id="pro5" value="Add to cart" style="margin-right: 80px"></td>
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
