print(".......Welcome........")
print("1  viewing list")
print("2  Add item")         
print("3  Remove item")        
         
products={"computer":25000,"laptop":50000,"keyboard":1500,"mouse":600}
       
selection=input("Select your choice..")


if selection=='1':
    for item in products:
        print(item,":",products[item])
elif selection=='2':
    item=input("enter an item:")
    price=input("enter price:")
    products[item]=price

    for item in products:
        print(item,":",products[item])
elif selection=='3':
    for item in products:
        print(item,":",products[item])
    item=input("enter an item:")
    del products[item]

    for item in products:
        print(item,":",products[item])
    
else:
    print("pleas select valid choice..")







