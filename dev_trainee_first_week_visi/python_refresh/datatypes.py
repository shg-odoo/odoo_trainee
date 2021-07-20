# a python program to display the sum of two complex numbers 
# c1 = 2.5+2.5J
# c2 = 3.0+0.5J
# c3 = c1+c2

# print('sum =',c3)

c1 = 2.5+2.5J

c2 = 3.0+0.5J

c3 = c1+c2

print(c3)


# a python program to converrt numbers from octal , binary and hexadecimal sysytems into decimal number system

# a python program to convert into  decimal number system 


n1 = 0o17
n2 = 0b1110010
n3 = 0X1c2

n = int(n1)
print('octal 17 is ' , n)
n =  int(n2)
print('Binary 1110010',n)
n = int(n3)
print('Hexadecimal 1c2',n)




# a python program to convert into decimal number system - v2.0

s1 = '17'
s2  = '1110010'
s3 = '1c2'

n = int(s1,8)
print('Octal of 17 is', n)
n = int(s2 , 2)
print('binary of 1110010 is ', n)

n = int(s3 , 16)
print('hexadecimal of 1c2' , n)

# program to understand bytes type array 
# create a list of byte numbers 

elements = [10,20,30,0,55,48]

# convert the list into bytes type array 

x = bytes(elements)

# retrieve each element from x using for loop and display 

for i in x : print(i)
print(type(x))


# a python program to create bytearray type array 

# create = [10,20,30,40,50]

elements = [10,20,30,50,60,89]

print(elements)

X = bytearray(elements)

X[3] = 96
X[2] = 56

for i in X : print(i) 


