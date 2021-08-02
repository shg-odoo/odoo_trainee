a = int(input("Enter a:"))    
b = int(input("Enter b:"))    
try:    
    
    c = a/b  
    print("a/b = %d"%c)    
  
except Exception:    
    print("can't divide by zero")    
    print(Exception)  
