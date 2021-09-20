<html>
   <head>      
      <script type = "text/javascript">
          
	      function helloKishan()
      	      {
               console.log("first print")
 
		for(var i = 0; i < 5000; i++) 
		{
		    setTimeout(() => {
		    console.log("this is async example "+ i)
		  }, 3000);
		}
		console.log("print end")
              }
      </script>     
   </head>
   
   <body>
      <input type = "button" onclick = "helloKishan()" value = "Say Hello" />
   </body>  
</html>

