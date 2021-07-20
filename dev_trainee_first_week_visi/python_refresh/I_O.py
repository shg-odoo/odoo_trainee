# a python program to accept a string from  keyboard and display it 
# accepting a string from keyboard 
str = input('Enter a string ')
print('you entered a str  :', str ) # the striung you entered is 


# A python program to accept a character as a string 
# accepting a single character or string from keyboard 
ch = input('Enter a char : ')
print("you entered :", ch)



# a python program to accept a single character from keyboard 
# accepting a single character from keyboard 
ch = input('enter the charater ')
print('the character you entered is ', ch[0])


# a python program to accept a integer number from keyboard 
str = input('enter a number ')
x = int(str)

print('the integer you entered is ',x)


# a python program to accept an integer number from keyboard - v2.0
# accepting a integer a number from keyboard - v2.0
x = int(input('Enter a number : '))
print('You entered: ', x ) # display the int  number 


# a python program to accept  a float number from keyboard 
# accepting float number from keyboard 
x = float(input('Enter a number :'))
print('you  entered ', x )

# a python program to accept two integer numbers from keyboard 
# accepting two numbers from keyboard 

x = int(input('Enter the first integer :'))
y = int(input('Enter the Second integer :'))

print('the integers you entered :' , x, y)



# a python program to accept two integers and find their sum 
# a find sum of two  numbers 
x = int(input('Enter the first number '))
y = (int(input('Enter the second integer ')))

print('The sum of {} and {} is {} '.format(x,y,x+y))



# a python program to find sum and product of two numbers 
# find sum and product of two numbers 

x = int(input('enter the fist integer '))
y = int(input('enter the seond integer '))

# this will diplay the sum of two  integers entered above 

print('The sum of {0} and {1} is {2} '.format(x,y,x+y))

# this will display the product of two integers entered above 

print('the product of {0} and {1} is {2}'.format(x,y,x*y))

# print both sum and produt of both the numbers
print('the sum of {0} and {1} is {2} and product of  {0} and {1} is {3} '.format(x,y,x+y,x*y))


# a python program to convert numbers from one number system to decimal
# input from other number systems 

str = input('Enter hexadecimal number :' ) # accept input as a string 

n = int(str,16) # inform the number is base 16

print('Hexadecimal to decimal number :', n)

str = input('Enter octal number you want to convert :') # accept the number as a string 


# converting the number from octal to decimal 
n  = int (str , 8)

print('Octal to decimal :',n)

# converting the  number from binary to decimal 

str = input('enter the binaray you want to  convert into decimal ')
n = int(str , 2)
print('the converted number from binary to decimal is ', n)


# a python program to accept 3 integers in the same line and display their sum 

# accepting 3 numbers separated by space 

var1 , var2 , var3 = [int(x) for x in input('Enter the three numbers :').split()]

print('sum of the three integers {0} ,{1},{2} is {3} :'.format(var1,var2,var3,var1+var2+var3) )


# accepting three integers from keyboard and displaying there sum 

var1 , var2 , var3 = [int(x) for x in input('Enter the three numbers separated with comma ').split(',')]

print('the sum of {0},{1},{2} is {3}'.format(var1,var2,var3,var1+var2+var3))



# Evaluating a expression from keyboard 
# using eval() along with input() function

x = eval(input('Enter a expression :'))
print('Result of expression is ',x)


# a python program to accept a list from keyboard and display it on the screen

lst = eval(input('Enter a list using [] '))
print('the list you entered is ', lst )

# a python program to acccept a tuple from keyboard 

tpl = eval(input('Enter the data in ()'))
print('the tuple you entered is ',tpl)


# a python program to accept cmd line arguments 

# to display command line arguments .

import sys 

n = len(sys.argv) # n is the number of arguments 

args = sys.argv  # ags list omntains the arguments 

print('No of command line agruments  : ', n)
print('The args one by one ')

for a in args :
	print(a)
print(help(sys.argv))

# a python program to find sum of variables from keyboard 

import sys 

args = sys.argv

print('the sum of {0},{1},{2}'.format(args[1],args[2],int(args[1])+int(args[2])))


# a python program to find sum of even numbers from cmd line 

import sys 

# read arguments from cmd line  excepts the program to name 

args = sys.argv[1:]
print(args)

sum = 0

# find the sum of even arguments 

for i in args :
	x = int(i)
	if x%2 == 0:
		print(x)
		sum+=x

print('sum of even numbers is ', sum )


# a python program parser to find the square of a given  number 
# to find  square of a given number . save this as args.py

import argparse

# create ArgumentParser class object

parser  = argparse.ArgumentParser(description = 'This program displays the square value of a given number :' )

# add one argument with the name and type as integer 

parser.add_argument('num',type = int , help = ' please enter integer type number ')

# retrieve the arguments passed to the program  
args = parser.parse_args()
# find the square of the argument passed 
result = args.num**2
print('square value of = ', result )


# a python program to add numbers using argument parser 

# to find sum of given numbers . 

import argparse 

# create ArgumentParser class object 

parser  = argparse.ArgumentParser(description = ' this program finds the sum of two numbers ')

# add two arguments with names n1 and n2  with data type as floats 

parser.add_argument('n1', type= float,help = ' input first number ' )
parser.add_argument('n2',type =  float , help = 'input second number ')

# retrieve the arguments passed to the program 
args = parser.parse_args()

#  convert the n1 , n2 values into float type then  add them 

print(args )
result = float(args.n1) + float(args.n2)
print('sum of two :' , result )

# a python program to find the power of a number when it is raised to a particular power 

# to find power value of a number 

import argparse 

# call the ArgumentParser()

parser = argparse.ArgumentParser(description = 'this will find the power of the given number ')

# add the arguments to the parser 

parser.add_argument('nums',nargs = 2)

args = parser.parse_args()
# find the power of the given number 
# args is the  tuple which contains the arguments 

print('Number ', args.nums[0])
print('its power ', args.nums[1])

# convert the arguments into float and then find power 

result = float (args.nums[0])**float(args.nums[1])

print('Result ', result )


# a python program to find the power of a number when it is raised to a particular power 

# to find power value of a number 

import argparse 

# call the ArgumentParser()

parser = argparse.ArgumentParser(description = 'this will find the power of the given number ')

# add the arguments to the parser 

parser.add_argument('nums',type =float , nargs = 2)

args = parser.parse_args()
# find the power of the given number 
# args is the  tuple which contains the arguments 

print('Number ', args.nums[0])
print('its power ', args.nums[1])

# convert the arguments into float and then find power 

#result = float (args.nums[0])**float(args.nums[1])
result = args.nums[0]**args.nums[1]
print('Result ', result )


# to accept 1 or more arguments from cmd keyboard 
# to find power value of a number 

import argparse 

# call the ArgumentParser()

parser = argparse.ArgumentParser(description = ' this program will display the argument in a list ')

parser.add_argument('nums' , nargs = '+')

lst = parser.parse_args()

# display the arguments from list 
for i in lst.nums:
	print(i)