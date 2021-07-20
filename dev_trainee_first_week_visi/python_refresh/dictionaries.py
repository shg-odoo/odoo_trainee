# a python program to create a dictionary with employee details  and retrieve the values upon giving keys 

# creating ditionary with keys - value pairs 

''' 
create a dictionary with employee  details .
here 'Name '  is key and 'Chandra ' is its value .
'Id ' is key and 200 is its value 
'Salary ' is key and 9080.50 is its value 
'''

dict = {'Name ': 'Chandra', 'Id ':200 , 'Salary' : 9080.50 }

# access value by giving key 

print('Name of the employee ', dict['Name '])
print('Id number ', dict['Id '])
print('Salary of the employee ', dict['Salary'])

# a python program to retrieve keys ,values and key -value pairs from a dictionary

# dictionary methods 
# create a dcitionary with employee details 

dict = {'Name':'Vishal','Id':1,'Salary': 9080.50}

# print entire dictionary 
print(dict)


# display only keys  
print('Keys in dict :',dict.keys())

# display only value
print('Values in dict :', dict.values())

# display the items in the dict 

print('Items in dict :',dict.items())



# a python program to create a dictionary and find the sum of values 
# a program to create a dictionary  and find the sum of values 

# program to find sum of values in a dictionary

dict = eval(input('Enter the elements in {}'))

# find the sum of values 
s = sum(dict.values())

print('Sum of values in the dictionary ', s)


# a python program to create a dictionary from keyboard and display the elements 

# creating a dictionary

x = {}

print('How many elements ? ', end =' ')
n = int(input()) # n indicates no. of key-value pairs 

for i in range(n):
	print('Enter key :', end = ' ')
	k = input() # key is string 
	print('Enter its value :' , end = ' ')
	v = int(input()) # value is integer
	x.update({k:v})

# display the dictionary 
print('The dictionary is :' , x )


# a python program to create a dictionary with cricket players names and scores in a match . also we are retrieving runs by entering the player's names 

# creating a dictionary with cricket players names and scores

x = {}

print('How many players ?', end = ' ')
n = int(input()) # n indicates no. of key-value pairs 

for i in range(n):
	print('Enter the player name :', end = ' ')
	k = input() # key is string 
	print('Enter runs ', end = ' ')
	v = int(input())
	x.update({k:v})

# display only players name 
print('\n players in this match ')
for pname in x.keys():
	print(pname)


# accept a player name from keyboard 
print('Enter a player name ', end =' ')
name = input()

# find the runds done by the player 

runs = x.get(name, -1)

if(runs == -1):
	print('Player not found ')
else :
	print('{} made runs {}'.format(name,runs ) )


# a python program to show the usage of for loop to retrieve elements of dictionaries

# take a dicttionary 

colors = {'r':'Red', 'y':'Yellow', 'b':'Blue', 'w':'White'}

# display only keys 

for k in colors:
	print(k)

# pass keys to dictionary and display the values 
for k in colors:
	print(colors[k])

# items () method returns key and value pair into k ,v 
for k , v in colors.items():
	print('Key = {} Value = {} '.format(k,v))	


# a python program to find the number of occurrences of each letter in a string using dictionary 

# finding how many times eahc letter is repeated in a string 

# take a string with some letters 

str = 'Book'

# take an empty dictionary
dict = {}

# store into dict each letter as key  and its 

for x in str:
	dict[x] = dict.get(x,0) + 1

# display key and value pairs of dict

for k ,v in dict.items():
	print('Key = {} \t its occurrences = {} '.format(k,v))


# a python program to sort the elements of a dictionary based on a key or value 
# sorting a dictionary by key and value 

# take a dictionary 

colors = {10:'Red',20:'Green',30 : 'Yellow', 40 : 'White', 50 : 'Black'}
print(colors)
# sort the dictionary by keys 
C1 = sorted(colors.items() , key = lambda t: t[0])
print(C1)
# sort the dictionary by values 
C2 = sorted(colors.items() , key = lambda t:t[1])
print(C2)


# a python program to convert the elements  of two lists into key- value pairs of a dictionary 
# take twwo separate lists with elements 

countries = ['India','USA','Germany','France']
cities = ['Delhi','Washington','Berlin','Paris']

# make  a dictionary 

z = zip(countries,cities)
d = dict(z)

# display key - value  paris from dictionary d 
print('{:15s} --- {:15s}'.format('COUNTRY','CAPITAL'))

for k in d:
	print('{:15s}  --- {:15s}'.format(k,d[k]))


# a python program to convert a string into key-value  pairs and store them into a dictionary 

# converting a string into a dictionary 

# take a string 

str = 'Vijay=23,Ganesh=50,Lakshmi=89,Nikhil=97'

# brake the string ar ' '  and then at  '='

# store the pieces into a list 

lst = []
for x in str.split(','):
	#print(x)
	y = x.split('=')
	#print(y)
	lst.append(y)
	#print(lst)


# convert the list into dictionary ' d'

# but this 'd ' will have both name and age as strings 
d = dict(lst)
print(d)

# create a new dictionary 'd1' with name as string  and age as integer 
d1 = {}
for k ,v in d.items():
	d1[k] = int(v)

# display the final dictionary 
print(d1)

# a python program to accept a dictionary and display its element
# A function that takes  a dictionary as a parmeter

def funt(dictionary):
	for i , j in dictionary.items():
		print(i,' --- ', j)
	# take a dictionary
d = {'a':'Apple','b':'Book','c':'Cook'}

#call the function and pass the dictionary
funt(d)

# a python program to create a dictionary that does not change the order of elements 

# create an ordered dictionary 
from collections import OrderedDict
d = OrderedDict() # d is ordered dictionary 

d[10] = 'A'
d[11] = 'B'
d[12] = 'C'
d[13] = 'D'

# display the elements from dictionary 

for i , j in d.items():
	print(i, j)

