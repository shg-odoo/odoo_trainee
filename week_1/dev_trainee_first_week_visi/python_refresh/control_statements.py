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


# a python program to express a digit  in a word 
num = 1 
if num == 1 :
	print('one')


# a python program to display a group of messages when the condition is true 
str = 'Yes'
if  str == 'Yes':
	print('Yes')
	print('This is what you said ')
	print('your response is good  ')



# a python program to test whether a number is even or odd 
# to know if a given  number is even or odd 
x = 10 
if x % 2 == 0:
	print(x , 'is even number ')
else :
	print(x , 'is odd number ')


# a python program to accept a number from keyboard and test whether it is even or odd 
# to know if a given number is even or odd - v 2.0
x = int (input('Enter a number :'))

if x % 2 == 0 :
	print('the number you entered is even ', x)
else:
	print('the number you entered is odd ',x)

# a python program to test whether a given number is in between 1 and 10
# ysing if ..... else statement 
x = int(input('enter a number :'))

if x >=1 and x<=10:
	print('the number entered', x , 'is between is between 1 and 10')
else:
	print('the number entered ', x,'is below 1 or above 10 ')

# a python program to know if a  given number is zero , positive or negative 
# to know if a given number is zero or +ve or -ve 

num  = 0 
if num == 0:
	print(num , 'is zero ')
elif num > 0 :
	print(num,'is positive ')
else :
	print(num,'is negative')


# a python program to accept a numeric digit from keyboard and display in words 

# to display a numberic digit in words 

x = int(input('enter a digit :'))
if x == 0: print('zero')
elif x ==1 : print('one')
elif x ==2 : print('two')
elif x == 3 : print('three')
elif x == 4 : print('four')
elif x == 5 : print('five')
elif x == 6 : print('six')
elif x == 7 : print('seven')
elif x == 8 : print('eight')
elif x == 9 : print('nine')
else : print('enter a digit between 1 and 9 ')


# a python program to display numbers from 1 to 10 using while loop 
# to display numbers from 1 to 10 
x = 1 
while x <= 10:
	print(x)
	x+=1
print('End')


# a python program to  display  even numbers from 100 to 200 
x = 100 
while x >= 100 and x <= 200 :
	print(x,end =' ')
	x+=2



# a python program to  display even numbers between m and n 
# to display even numbers between m and n
m , n = [int(x) for x in input('enter the minimum and maximum range').split(',')]
x = m
if x % 2 != 0 :
	x +=1
while x >= m and x <= n :
	print(x, end=' ')
	x+=2


# a python program to display characters of a string using for loop 
# to display each charater orm a sting 

st = 'Hello '

for ch in st:
	print(ch)

# a python program to display character from a string using sequence  index 

# to display each character fom a string 

str = ' Hello '

n = len(str)

for i in range(n):
	print(str[i])

# a python program to display  odd numbers from 1  to 10 using range object 

# to display numbers between 1 to 10

for i in range(1,10,2):
	print(i,end='  ')


# a program to display numbers from 10 to 1 in descending order 

# to display numbers in descending order 

for x in range(100,10,-1):
	print(x,end = ' ' )

# a python program to display the elements of a list using for loop

list = [10,20.5,'hello','A']

for i in list:
	print(i)

# a python pogram to display and find the  usm of a list of numbers using for  loop 

# to find  sum of list of numbers using for 

list = [10,20,30,40,50,60]

sum = 0 

# using for loop to find the sum of numbers in list 

for i in list :
	print(i)
	sum += i
print('sum is ', sum)

# a python program to display and sum o al list of numbers using while loop

# to find sum of a list numbers using while loop
# take a list  of numbers 

list = [10,20,3,0,50,60,800]
sum =  0 # initially sum is zero 
i = 0

while i < len(list):
	print(list[i],end = ' ') # display the elements orm list 
	sum += list[i]
	i += 1
print('sum of elements is ', sum)

# a python program that displays stars in right angled triangular  form using nested loop

# to display stars in right angled triangular form

for i in range(1,10):
	for j in range(1 , i+1):
		print('#',end = ' ')
	print()


# a python program that displays stars in right angled triangular from using a single loop

# to display  stars in right angled tiangular form 

for i in range(1,11):
	print('*'*i)

# a python program to display the stars in an equilateral triangular form using a single for loop

# to display stars  in equilateral  triangular  form 

n = 40 
for i in range(1,11):
	print(' '*n, end = '')
	print('* '*(i))
	n-=1

# a python program to  display  numbers from 1 to 100 in a  proper format 

# displaying numbers from 1 to 100 in 10 rows and 10 cols 

for x in range(1,11):
	for y in range(1,11):
		print('{:10}'.format(x*y), end = '')
	print()

# a python program to search for an element in the list of elements 
# searching for an element in a list 

group1 = [1,2,3,4,5,6]
search = int(input('Enter the element to search :'))

for element in group1 :
	if search == element :
		print('Element found in group1 ')
		break # this is will break the loop
else :
	print('Element not found in group1 ') # this is else suite 

# a python program to display  numbers from 10 to 6 and break the loop when the number about to display is 5 
# using break to come  out of while loop
x = 10 
while x >= 1:
	print('x  = ', x)
	x-=1
	if x == 5 : # if x is 5 then come out from while loop
	    break 
print('Out of loop')

# a python program to display numbers from 1 to 5 using  continue statement 

x = 0 

while x <= 10:
	x += 1 
	if x > 5: # if x > 5 then continue next iteration 
	     continue
	print('x :', x)
print('out of the loop ')

# a python program to know that pass does nothing 
# using passs to do nothing 

x = 0 

while x < 10:
	x += 1 
	if x > 5: # if x > 5 then continue next iteration
	    pass 
	print('x = ', x)
print('Out of the loop ')

# a python program to  retrieve only negative  numbers  from list of numbers 

num = [1,2,3,4,5,6,7,8,9,10,-55,-69,-89]

for i in num:
	if (i>0):
		pass  # we are not interested 
	else :
		print(i) # this is what we need 


# a python program to assert that the user enters a number greater then zero

# understanding assert  statement 

x = int(input('Enter the number greater then 0 '))

assert x > 0 ,'wrong input entered '
print('you entered ',x)


# a python porgram to handle the AssertionError exception that is given by assert statement 

# to handle AssertionError raised by assert 

x = int(input('Enter a number  greater than 0 :'))

try :
	assert( x>0 ) # exception may occur here 
	print(' you entered : ', x )
except AssertionError:
	print('Wrong input entered ')
	


# a python program to  function  the sum of two numbers 

# a function to find sum o two numbers 
def sum(a,b):
	print('sum :',a+b)

sum(5,5)
sum(2.5,5.2)


# a python program to write a function that returns the result of sum of two numbers 
def sum(a,b):
	return (a+b) # this function returns the sum of a+b

# call sum() and pass any values that can be added together

res = sum(10,50)
print('the sum of both values is ', res)

