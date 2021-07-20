# a python program that accepts two values and finds their sum 

# a function to accept two values

def sum(a,b):
	"""this is a doc string """
	c = a+b
	print(c)
# calling function 
sum(10,15)
sum(50,25)

# a python program to find the sum of two  numbers and return their results 

# a function to add two numbers 

def sum (a,b):
	''' doc string is important for documentaion '''
	c = a+b
	return c 

# calling a a function 
x = sum(10,52)
y = sum(10,10)

print(x,y)

# a python program to test whether a number is even or odd 
# a program to check whether a given number is even or odd 

def even_odd(num):
	''' to test whether a given number is even or odd '''
	if num % 2 == 0:
		print('the given num is even',num)
	else:
		print('the given number is odd',num)

# call the function

even_odd(9)
even_odd(8)

# a python program to calculate factorial of a given number 

def fact(n):
	''' to find factorial of given  number '''
	prod = 1
	while n >= 1:
		prod*=n
		n-=1
	return prod

# display factorials of first 10 numbers

for i in range(1,11):
	x = fact(i)
	print('factorial of {} is {}'.format(i,x))

# a pythoin program to check if a given number is prime or not

def prime(n):
	''' to check if n is prime or not '''
	x = 1 # this will be 0 if not prime 
	for i in range(2,n):
		if n % i == 0:
			x = 0 
			break 
		else:
			x = 1
	return x 


# testing the functions 

num = int(input('Enter a number '))

# check if num is prime or not 

result = prime(num)
if result == 1:
	print(num , 'is prime')
else :
	print(num, ' is not prime ')


# a python program that generates prime numbers with the help o a function to test prime or not

# a function to test whether a number is prime or not 

def prime(n):
	''' to check if n is prime or not  '''
	x = 1 # this is will be zero if not prime
	for i in range(2,n):
		if n%i == 0:
			 x = 0 
			 break 
		else:
			x = 1 
	return x 


# generate prime number series 
num = int(input('How many primes do you want?'))
i = 2 
c = 1 
while True :
	if prime(i):
		print(i)
		c+=1
	i+=1
	if c > num :
		break 

# a python program to understand  how a function returns two values 

def sum_sub(a,b):
	'''  this function returns addition and subtacion of two vaiables  '''
	c = a+b
	d =a-b
	return c , d

# get the results from the above function
x , y = sum_sub(10,15)

# display the results

print('the addition is ', x)
print('result of subtacion is ', y )


# a python program that returns the result of addition , subtraction , multiplication , division 
def pro(a,b):
	''' this funtion returns the addition subtraction , multiplicaion and division of the given varibles '''
	x = a+b
	y = a-b
	z = a*b
	p = a/b
	return x , y , z ,p

# get the results from function

o = pro(10,5)

for i in o :
	print(i , end = ' ')
n = len(o)
print()
for i in range(n):
	print(o[i])


# a python program to see how many to assign a function to a variable 

def  display(str):
	return 'hai '+str

# assign funtion to variable x 
x = display('krishna ')
print(x)

# a python program to define a funtion inside a another function

def display(str):
	def message():
		return ' how are you?'
	result = message() + str
	return  result

# calling function 

print(display('vishal'))


# a python program to know how to pass a function as parameter to another 

def display(fun):
	return 'hai ' + fun 


def message():
	return ' How are you ?'

# call display() function   and pass 
print (display(message()))

# a python program to know how a function can return another function

# functions can return other functions 

def display():
	def message():
		return 'how are you ?'

	return message 

# call display() funtion and it  returns message() funtion
# in the following code , fun refers to the name : message 

fun = display()
print(fun())

# a python program to pass an integer to function and modify it 
# passing an integer to a function

def modify(x):
	''' reassign a value to the variable '''
	x = 15
	print(x, id(x))

# call modify and pass x

x = 10

modify(x)
print(x,id(x))

# a python program to pass a list to a function and modify it 

# passing a list to aa function

def modify(lst):
	''' add new element to list '''
	lst.append(9)
	print(lst,id(lst))

# call modify () pass list

lst =[1,2,3]
modify(lst)
print(lst,id(lst))

# a python program to create a new object inside the function does not modify outside object

def modify(lst):
	''' to create a new lst '''
	lst = [10,11,12]
	print(lst,id(lst))


# call modify( ) and pass lst 

lst = [1,2,3,4]
modify(lst)

print(lst,id(lst))

# a python program to understand the positional arguments of a function 

# positional arugments demo

def attach(s1,s2):
	''' to join s1 , s2 and display total sting '''
	s3 = s1+s2
	print('Total string ' +s3)


# call attach()

attach('new ' , 'york ') 


# a python program to understand the keyword arguments of a function\
# keyword arugments demo 

def grocery(item,price):
	''' to display item and price '''
	print('Item = %s ' %item)
	print('Price = %.2f' %price)

# call grocery () and pass arguments 

grocery(item = 'Sugar',price = 50.75)
grocery(price = 75.05, item = 'oil')



# a python program to understand the keyword arguments of a function

# keyword arguments demo 

def grocery(item , price= 40.00):
	''' to display the given arguments '''
	print('item = %s' %item)
	print('pirce = %.2f' %price)

grocery(item = 'sugar ', price = 35)
grocery(item = 'rice')

# a python program to find the sum of passed variables 

def add(farg , *args):
	''' formal arguments given to add '''
	print('Formal arguments = ',farg )

	sum = 0 
	for i in args :
		sum += i 
	print('sum of arguments  ', (farg+sum))


# call the function and pass arguments 

add(5,10)
add(10,50,60,40,30,10)

# a python program to understand keyword variable argument

# keyword variable argument demo

def display(farg, **kwargs):
	''' to display given values '''
	print('formal argument ', farg)

	for x , y in kwargs.items():
		print('key = {}, value = {}'.format(x,y))

	# pass formal argument and 2 keyword arguments 

display(5, rno=10)
print()

	# pass 1 formal argument and 4 keyword arguments 
display(4, rno = 90 , name = 'vishal')

# a python program to understand global and local variables
a = 1 
def myfun():
	a = 2 
	print('a = ',a)

myfun()
print('a = ',a)

