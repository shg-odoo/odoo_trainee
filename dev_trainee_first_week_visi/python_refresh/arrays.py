# a python program to create an integer type array 
# creating an a array 
import array 

a = array.array('i',[5,6,-7,-9,8])

print('The array elements are :')

for i in a :
	print(i)


# a python porgram to create an integer type array 

# creating an array -v 2.0

from array import *

a = array('i',[5,4,6,8,-89,-98])

for i in a :
	print(i)

# a python program to create array  with characters 

# creating array program with characters 
from array import *

a = array('u',['a','b','g','f' ])

for i in a :
	print(i)

# a python program to create one array from another array 

# creating one array  from another array 

from array import *

arr1 = array('d',[2,3,4,5,6,7,8,9])

# use same type code and multiply 
arr2 = array(arr1.typecode,(a*2 for a in arr1))

print('printing each element from arr2')

for i in arr2:
	print(i)

# a python program to retrieve elements from array using array indexing 

# accessing elements from array using array indexing 

from array  import *
arr1 = array('i',[10,20,30,50,60,980])

# taking a  variable to store the length of the array
n = len(arr1)

# display array elements using indexing 

for i in range(n):
	print(arr1[i])
for i in range(n):
	print(arr1[i],end = ' ')

# a python program to retrieve elements using while loop 
# accessing elements using while loop

from array import *

x = array('i',[20,52,62,32,62,85])

n = len(x)

i = 0
while i < n:
	print(x[i],end=' ')
	i+=1

# a python program to see effect of slicing operations on an array 


from array import *
x = array ('i',[10,20,30,50,60,40,500,600,700,800,900])
# create array y with elements from  

y = x[1:4]
print(y)

# creating a array  with elements from 1st to  last element 

y = x[0:]
print(y)


# creating a array with elements from 1st to 3rd element

y = x[0:4]
print(y)


#create a rray with elements from last four elements 

y = x[-4:]
print(y)


# creating y with last 4th element and 3 elements towards right 

y = x [-4:-1]
print(y)

# creating y with zeroth to 7th element from x
y = x[0:8]
print(y)


# a python program to retrieve and display only a rnage of elements from an array using slicing operation 

from array import *

x = array('i',[10,20,30,50,60,40])


# display elements from 2nd to 4th elements only

y = x[1:5]
print(y)
for i in y:
	print(i,end=' ')

# a python program to understand various methods of array slicing 

from array import *

# create an with int values 

x = array('i',[10,20,30,60,80,90,850,789,985,8956])

print('Original array :',x)

# appending 30 to array x with method append
x.append(30)
print('array after appe 30 see the last element :',x)

# insert 99 at position 1 
x[1] = 99
x.insert(2,88)
print('array after modifing the value at position 1 ',x) 

# remove element from array using remove method 
x.append(850)
x.remove(850)
print('array after removing the 850 ',x)

# removing element from last position using pop()

x.pop()
print('array after removing the last element using pop() method ',x)

# finding position of position of an element using index method

f = x.index(90)
print('position of the element at which 90 is found ',f)

# converting array into a list using list method 
lst =x.tolist()
print('created list ',lst)
print('original array ', x)

# a python program to store students marks into an array  and finding total marks and percentage of marks 

from array import *

str = input('enter marks ').split(' ')

# store marks into marks list 
marks = [int(num) for num in str]

# display the marks and find the sum of marks 

sum = 0 

for i in marks :
	print(i)
	sum +=i
print('Total marks :', sum)

# display percentage 
n = len(marks)

percent = sum/n
print('percentage of :',percent)


# a python program to sort the array elements using bubble sort technique 
# sorting an array using bubble sort technique 

from array import *

# create a  an empty array 
x = array('i',[])

# store elements into array x 

print('how many elements ?',end = ' ')
n = int(input()) # accept input into n 
for i in range(n): # repeat for n times 
    print('enter element :',end = ' ')
    x.append(int(input())) # add the element to the array 

print('original array ',x)

# bubble sort 
flag = False  # when done swaping this will set to True 

for i in range(n-1): # i is from 0 to n-1
    for j in range(n-1-i): # j is from 0 to one element lesser then i 
        if x[j] > x [j+1]: # if 1st element is bigger then second element 
            t = x [j]
            x[j] = x[j+1]
            x[j+1]  = t 
            flag = True 
    if flag == False :
    	break
    else :
    	flag = False # assign initial value to flag 
print('sorrted array ',x)

# a python program to sort the array elements using bubble sort technique 
# sorting an array using bubble sort technique 

from array import *

# create a  an empty array 
x = array('i',[])

# store elements into array x 

print('how many elements ?',end = ' ')
n = int(input()) # accept input into n 
for i in range(n): # repeat for n times 
    print('enter element :',end = ' ')
    x.append(int(input())) # add the element to the array 

print('original array ',x)

# bubble sort 
flag = False  # when done swaping this will set to True 

for i in range(n-1): # i is from 0 to n-1
    for j in range(n-1-i): # j is from 0 to one element lesser then i 
        if x[j] > x [j+1]: # if 1st element is bigger then second element 
            t = x [j]
            x[j] = x[j+1]
            x[j+1]  = t 
            flag = True 
    if flag == False :
    	break
    else :
    	flag = False # assign initial value to flag 
print('sorrted array ',x)
 
# a python program to search for the position of an element in an array using sequential search 
# searching an array for an element 
from array  import *

# create an empty array to store integers 

x = array('i',[])

# store elements into an array x 
print('How many elements do you want in this array ..',end = ' ')
n = int(input()) # accept input into n 

for i in range(n):
	print('enter element :',end = ' ') # add one element at time to this list 
	x.append(int(input()))

print('original array ', x)

print('element you want  to search :', end = ' ')

s = int(input()) #accept element to be searched 

# linear search or sequential search 

flag = False # this becomes true if element is found 

for i in range(len(x)):
	if s == x[i]:
		print('found at position ',i+1)
		flag =True 
if flag == False :
	print('the element is not there in the array ')

