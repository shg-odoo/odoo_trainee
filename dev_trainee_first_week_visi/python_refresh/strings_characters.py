# a python program to access each element of  a string in forward and reverse order using while loop 
# indexing on loops 

str = 'Core Python'

# access each character using a while loop

n = len(str) # length of the string 
i = 0 # counter 

while i < n:
	print(str[i],end = ' ')
	i += 1
print()
i = -1 
while i >= -n :
	print(str[i],end=' ')
	i -=1
print()
i  = 1
n = (len(str))

while i <= n:
	print(str[-i],end = ' ')
	i+=1


# a python program to acccess the characters of a string using a for loop
# accessing elements of a string using for loop
str = ' core python'

# access each letter using for loop

for i in str:
	print(i,end = ' ')

print()

# access in reverse order 
for i in str[::-1]:
	print(i,end=' ')


# a python program to know whether a sub string exists in a main string or not 

str = input('enter the main string ')
sub = input('enter the sub string :')


if sub in str:
	print(sub+ ' is found in main string')
else :
	print(sub+'is not ofund in main string ')


# a python program to find the first occurrene off sub string in a given main string 
# to find first occurrence of sub string in a main string 

str = input('enter main string :')
sub = input('enter the sub string :')

# find the position of the sub in str
# search from 0th to last characters in str 

n = str.find(sub,0,len(str))

# find() returns -1 if sub string is not found 
if n == -1:
	print('sub string not found ')
else:
	print('sub string found at position',n+1)

# a python program to find occurrence of sub string  in a given string 
str = input('enter the main string :')
sub = input('enter the sub string you want to search :')

# find position of the sub in str

# search from 0th to last character in str

try :
	n = str.index(sub,0,len(str))
except ValueError :
	print('sub string not found ')
else :
	print('sub string found at position ', n+1 )

# a python program to display all positions of a sub string in a given main string 

# to find all occurrences of sub string in a main string 

str = input('enter the main string')
sub = input('enter the sub string :')


i = 0 
flag = False 
n = len(str)

while i < n:
	pos = str.find(sub,i,n)
	if pos != -1 :
		print('found at position :', pos+1)
		i = pos+1
		flag = True 
	else :
		i = i+1  # search for the next string 
if flag == False :
	print('sub string not found ')

# a python program to display all position of sub string in a given main string - v 2,.0
str = input('enter the  main string ')
sub = input('enter the sub string ')

flag = False 
pos = -1

n =len(str)
while True :
	pos = str.find(sub,pos+1,n)
	if pos == -1 :
		break 
	print('FOund at position ', pos+1)
	flag = True
if flag == False :
	print('Not Found ')

# a python program to accept and display a group of numbers

# to accept a group of numbers and display them

str = input('Enter the numbers separated by sapce :')

# cut the string where a space is found 
lst = str.split(' ')
# display the elements of the list 
for i in lst:
	print(i )

# a python program to know the type of character entered by the user

# to know the nature of a character 

str = input('enter a character ')

ch = str[0]

# test ch

if ch.isalnum():
	print('it is a alphabet or numeric character :')
	if ch.alpha():
		print('the charcter you entered is alphabet')
		if ch.isupper():
			print('the character is capital letter ')
		else:
			print('the character is a small letter')
	else :
		print('it is a numeric digit ')
elif ch.isspace():
		print('it is a space ')
else :
		print('it may be a special character ')

#  a python program to sort a group of strings into alphabetical order 
# sorting a group of strings
str = []

# accept how many characters 
n = int(input('how many charcters do you want to enter'))

# store the elements into a array 

for i in range(n):
	print('Enter string :',end = ' ')
	str.append(input())

# sort the array 
#str.sort()

str1 = sorted(str)

# display the sorted array 

print('sorted list :')
for i in str1:
	print(i)

# a python program to search for the position of a string in a given group of strings 

# searching for a string in a group of strings

str = []

# accept how many strings 

n = int(input('How many strings ?'))

# append method to store the strings in to the list

for i in range(n):
	print('enter the string :', end = ' ')
	str.append(input())

# ask for the string to search 

s = input('Enter the string to search')

# linear search or sequential search 

flag = False 

for i in range(len(str)):
	if s == str[i]:
		print('found at ', i+1 )
		flag = True 
if flag == False :
	print('Not foun1d ')

# a python program to find the length of a string without using len() function

str = input('Enter a string ;')
i = 0 

for s in str :
	print(str[i],end = ' ')
	i+=1
print('\n no. of characters :', i )


# a python program to find the number of words in a string 
# to find no. of words in a string 

str = input('enter a string :')

i=c=0

flag = True 
for s  in str:
	if flag == False and str[i] == ' ':
		c+=1
	if str[i] == ' ':
		flag = True 
	else :
		flag = False 
	i+=1

print('No. of words :', c+1)

# a python program to insert a sub string in a particular position 
# to insert a sub string in a string 

str = input('enter a  string: ')

sub = input('enter a sub string :')
n = int(input('enter the position no.'))

# decrease n by 1  to insert in correct position 
n-=1

# find the number of charcters in str , sub 
l1 = len(str)
l2 = len(sub)


# take another  string as a list 

str1 = []

# append 0 to n-1 characters from str to str1 

for i in range(n):
	str1.append(str[i])

# append sub string to str1
for i in range(l2):
	str1.append(sub[i])

# append the remaining characters from str to str1

for i in range(n,l1):
	str1.append(str[i])
print(str1)
# convert the individual charcters of a list into 
# a string using join() method with empty string as separator
str1 = ''.join(str1)


# display the total string 
print(str1)
