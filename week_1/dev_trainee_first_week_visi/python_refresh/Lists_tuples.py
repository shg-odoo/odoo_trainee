# a python program to create lists with different types of elements 
# a general way to create lists 
num = [10,20,30,40,50,60]
print('Total list ',num)   # display the list 
print("First = %d , Last = %d" %(num[0], num[4])) # display the first and last element 

# create a list with strings 

names = ['Raju ','Van','Gopal ','Laxmi']
print(names)

print('First = %s , last = %s' % (names[0],names[3]))
# display the first snd last element

# create a list with different elements 
x = [10,20,10.5,25,2.55,'Ganesh','Vishal']
print('The length of the  list is ', len(x))
print('First elemet = %d , last element = %s ' % (x[0],x[5]))


# creating list objets with range function 

list1 = range(10)

for i in list1 :
	print(i , end = ' ')
print()


list2 = range(5,10)

for i in list2 :
	print(i , end = ' ')
print()


list3  = range(1,10,2)

for i in list3:
	print(i , end = ' ')
print()


# a python program to access elements using loops 

list = [1,2,3,4,5,6,7,8,9]


i =  0 

while i < len(list):
	print(list[i])
	i+=1
print()


print('using for loop')

for i in list:
	print(i)
print()

# a python program to display elements of a list in reverse order

days = ['sunday', 'monday','tuesday','wednesday','thursday','friday','saturday']

print('\n In reverse order')

i = len(days)-1 # i will be n-1 
while i>= 0:
	print(days[i]) # display from 4th to 0th elements
	i -= 1


print('\n In reverse order')

i -= 1 

while i >= -len(days):
	print(days[i])
	i -= 1



# a python program to understand list processing methods 
num = [10,20,30,40,50,60]

n = len(num)
print('No. of element of list ', n )

num.append(60)
print('num after appending 60 ', num)

num.insert(0,5)
print('num after inserting 5 at index  0th position  ', num)

num1 = num.copy()
print('newly created list num1 ', num1 )

num.extend(num1)
print('num after extending num1 ',  num )


n = num.count(50)
print('No. of times 50 is found in the list ', n )


num.remove(50)
print('num after removing 50', num)

num.pop()
print('num after removing last element ', num)

num.sort()
print('num after sorting the elements ', num)


num.reverse()
print('num after reversing all the elements ', num)

num.clear()
print('num after removing all elements ', num )

# a python program to  find the maximum and minimum elements in a list of elements 
# finding biggest and smallest numbers in a list of numbers 

x = [ ] # take a an empty list 

print('how many elements :?', end = ' ')
n = int(input())

for i in range(n):
	print('enter element :',end = ' ')
	x.append(input())


print('the list is ', x)

big = x[0]
small = x[0]

for i in range(1,n):
	if x[i] > big : big = x[i]

	if x[i]< small : small = x[i]

	# take it as small 

print('Maxmimum is :', big)
print('minimum is ', small)

# a python program to sort the list elements using bubble sort technique

# creating  an empty list to store integers 

x = []


# store elements into the list  

print('how many elements?', end = ' ')
n = int(input())

for  i in range(n):
	print('enter element  ', end = ' ')
	x.append(int(input()))

print('original list :', x)

# bubble sort 

flag = False 
print(n)

for i in range(n-1):
	for j in range(n-1-i):
		if x[j] > x[j+i]:
		    t = x[j]
		    x[j] = x[j+1]
		    x[j+1] = t 
		    flag = True
		if flag == False :
			break
		else:
			flag = False
print('Sorted list : ', x ) 

# a python program to know how many times an element occurred in the list

# counting how many times an element occurred in the list
x = []

n = int(input('how many elemnet? '))


for i in range(n):
	print('enter element : ' , end = ' ')
	x.append(int(input()))

print('The list is  : ', x ) # display the list 

y = int(input('enter element to count :'))

c = 0 
for i in x:
	if(y == i) : c+=1
print('{} is found {} times '.format(y,c))

#  a python program to find  common elements in two lists 

# finding common elements in two lists 

scholar1 = ['pooja','vivek','divya','pathik']
scholar2 = ['vivek', 'rahul', ' rohit','rohini']

s1 = set(scholar1)
s2 = set(scholar2)


s3 = s1.intersection(s2)

common = list(s3)


# display the  common list

print(common)

# a python program to create a list with employee data and then retrieve a particular employee details 

emp = []

n = int(input('How many employees ?'))


for i in range(n):
	print('Enter id ', end = ' ')
	emp.append(int(input()))
	print('Enter name ', end = ' ')
	emp.append(input())
	print('enter salary ', end = ' ')
	emp.append(float(input()))

print('The list is created with employee details ')

id = int(input('Enter employee id '))


for i in range(len(emp)):
	if id == emp[i]:
		print('Id = {:d}, Name  = {:s}, salary = {:.2f}'.format(emp[i],emp[i+1],emp[i+2]))
		break 


