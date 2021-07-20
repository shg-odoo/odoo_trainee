# a python program to define student class and create an object to it . also , we will call the method and display the student's details 

# instance variables and instance method 

class Student :
	# this is a special method call constructor
	def __init__(self,name,roll):
		self.name = name
		self.roll = int(roll)

	def talk(self):
		print('my name is ' + self.name )
		print('give me the hall ticket with number ' , self.roll) 


s1 = Student('vishal', 140420111054)

s1.talk()

class Student:
	def __init__(self, n = '',m = 0):
		self.name = n
		self.marks = m 

	def display(self):
		print('Hi' , self.name)
		print('Your marks ', self.marks)


s = Student()
s.display()
print('-----------')

s1 = Student('Lakshmi roy', 900)
s1.display()


# a python program to understand instance variables 
class Sample:
	 # this is a constructor
	 def __init__(self):
	 	self.x = 10

	 # this is an instance method 
	 def modify(self):
	 	self.x+=1


# create 2 instance

s1 = Sample()
s2 = Sample()
print('x in s1 is', s1.x)
print('x in s2 is ', s2.x)


# modify x in s1 
s1.modify()
print('x in s1 is', s1.x)
print('x in s2 is ', s2.x)


# a python program to understand class variables or static variables 

# class vars or static  vars example 

class Sample :
	# this is a class var 
	x = 10

	# this is a class method 
	@classmethod
	def modify(cls):
		cls.x+=1



s1 = Sample()
s2 = Sample()

print('x in s1 = ', s1.x)
print('x in s2 = ' , s2.x)

# modify  x in s1 

s1.modify()
print('x in s1 = ', s1.x)
print('x in s2 =', s2.x)

# a python program using a student class with instance methods to process the data of several students 

# instance methods to process data of the objects 

class Student:
	# this is a constructor
	def __init__(self,n = '',m=0):
		self.name = n
		self.marks = m
	# this is  an instance method 
	def display(self):
		print('hi', self.name)
		print('Your marks ', self.name)

	def calculate(self):
		if(self.marks >= 600 ):
			print('YOu got first grade')
		elif(self.marks  >= 500):
			print('You got second grade')
		elif (self.marks >= 350):
			print('You got third grade')
		else:
			print('you failed ')


# create instance with some data from keyboard 

n = int(input('How Many students ?'))

i = 0

while (i<n):
	name = input('Enter name :')
	marks = int(input('enter the marks '))
	s = Student(name,marks)
	s.display()
	s.calculate()
	i+=1
	print('--------------------------------------------')

for i in range(n):
	name = input('enter the name of student')
	marks = int(input('Enter the marks '))
	s = Student(name,marks)
	s.display()
	s.calculate()



# a python program to store data into instances using mutator methods and to retrieve  data from the instances using accessor methods

# accessor and mutator methods  

class Student:

	# mutator method
	def setName(self,name):
		self.name = name 


	# accessor method 
	def getName(self):
		return self.name

	# mutator method to set marks 
	def setMarks(self,marks):
		self.marks = marks

	# accessor method 
	def getMarks(self):
		return self.marks



# create instances with some data from keyboard 
n = int(input('How Many students ?'))


i = 0 

while(i<n):

	#  create student instance 
	s = Student()
	name = input('Enter the name of the student  ' )
	s.setName(name)
	marks = int(input('Enter marks ?  '))
	s.setMarks(marks)
	i+=1
	# retrieve data from student class instance 
	print('Hi', s.getName())
	print('Marks ', s.getMarks())


# a python program to use class method to handle the common feature all the instance of Bird class 

# understanding class methods 

class Bird:
	# this is a class var 
	wings = 2

	# this is a class method 
	@classmethod
	def fly(cls,name):
		print('{} flies with {} wings '.format(name, cls.wings))

# display information for 2 birds 
Bird.fly('Sparrow')
Bird.fly('Pigeon')


# a python program to create a static method that counts the number of instanes created for a class 

# understanding static methods 

class MyClass:
	# this is class var  or static var
	n = 0 

	# constructor that increments n when an instance is created 
	def __int__(self):
		MyClass.n = MyClass.n + 1


	@staticmethod
	def noObjects():
		print('No. of instances created ' , MyClass.n)

# create 3 objects 
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
MyClass.noObjects()

#  a python program to create a Bank class where deposits and withdrawals can be handled by using instance methods

#  A class to handle deposits and withdrawls in a bank
import sys 
class Bank(object):
	''' Bank related transactions '''
	# to initialize name and balance instance vars 
	def __init__(self,name,balance = 0.0):
		self.name = name 
		self.balance = balance

	# to add deposit amount to balance 
	def deposit(self,amount):
		self.balance += amount
		return self.balance

	# to deduct withdrawal amount from balance

	def withdraw(self , amount):
		if amount >= self.balance :
			print('the amount is more then your account balance')
		else :
			self.balance -= amount
		return self.balance


# using the Bank class 

# create an account with the given name and balance 0.00

name = input('Enter the account holder name ')
b = Bank(name)

# repeat till choice is e or E

while(True):
	print(' d - Deposit , w -Withdraw , e -Exit')
	choice = input('Your choice  ')
	if choice == 'e'   or choice == 'E' :
		sys.exit()
		# amount for deposit or withdraw 
	amt = float(input('Enter the amount'))\
	# do the transaction
	if choice == 'd' or choice == 'D':
		print('Balance after deposit is ', b.deposit(amt))
	elif choice == 'w' or choice == 'W':
		print('Balance after withdrawal :' , b.withdraw(amt))


# a python program to create Emp class and make all the the members of the Emp class available to another class . i.e MyClass 

# this class contains employee details 

class Emp :
	# this ia constructor 
	def __init__(self,id,name,salary):
		self.id = id 
		self.name= name 
		self.salary = salary 

	# this is an instance method 

	def display (self):
		print('Id :', self.id)
		print('Name :',self.name)
		print('salary :', self.salary)

#this class displays employee details 
class MyClass:
	# method to recieve Emp class instance 
	# and display employee details 
	@staticmethod 
	def mymethod(e):
		# increment salary of e by 10000
		e.salary+=10000
		e.display()

# create Emp class instance e 
e = Emp(10,'Raj Kumar ',15000.50)

# call static method 
MyClass.mymethod(e)

# a python program to calculate power value of a member with help of a static method

class MyClass :
	# method to calculate x to the power of n 
	@staticmethod 
	def mymethod(x,n):
		result = x**n
		print('{} to the power of {} is {}'.format(x,n,result))


# call the static method 

MyClass.mymethod(5,3)
MyClass.mymethod(5,4)


# a python program to create Dob class within Person class 

class Person:
	def __init__(self):
		self.name = 'Charles'
		self.db = self.Dob()


	def display(self):
		print('Name = ', self.name)

	# this is inner class 
	class Dob :
		def __init__(self):
			self.dd = 10
			self.mm = 5
			self.year = 1988

		def display(self):
			print('Dob = {}/{}/{}'.format(self.dd,self.mm,self.year))

# creating Person class object 
p = Person()
p.display()

# create inner class object 

x = p.db
x.display()


# a python program to create another version of Dob class within Person class

# inner class example - v2.0

class Person:
	def __init__(self):
		self.name = 'vishal'
		self.dd = self.Dob()

	def display(self):
		print('Name :', self.name)

	# this is inner class 
	class Dob():
		def __init__(self):
			self.dd = 24
			self.mm = 10
			self.yy = 1996

		def display(self):
			print('{}-{}-{}'.format(self.dd,self.mm,self.yy))



# creating Person class object 

p = Person()

p.display()

# create Dob object as sub to person class object 

x = Person().dd
x.display()
print(x.yy)



# a python program to to create Teacher class and store it into teacher.py module

class Teacher:
	def Setid(self,id):
		self.id = id

	def Getid(self):
		return self.id
	def Setname(self,name):
		self.name = name

	def Getname(self):
		return sel.name

	def Setaddress(self,address):
		self.address = address
	def Getaddress(self):
		return self.address
	def Setsalary(self,salary):
		self.salary = salary
	def Getsalary(self):
		return self.salary

# save this is  as inh.py file

# using Teacher class 
from teacher import Teacher 

t = Teacher()

# store data into the instance

t.Setid(10)
t.Setname('vishal')
t.Setaddress('surat')
t.Setsalary(10000)


# retrieve the data from the object 

print('Id ' , t.Getid())
print('Name of the employee ' , t.Getname())
print('Address ' ,t.Getaddress())
print('Salary ',t.Getsalary())

# a python program to create student class and store it into student.py module

# this is student class - V1.0 save it as student.py

class Student:
	def Setid(self,id):
		self.id = id 
	def Getid(self):
		return self.id


	def Setname(self,name):
		self.name = name
	def Getname(self):
		return self.name


	def Setaddress(self,address):
		self.address = address
	def Getaddress(self):
		return self.address

	def Setmarks(self,marks):
		self.marks = marks
	def Getmarks(self):
		return self.marks


# a python program to use the students class which is already available in student.py

# save this code inh.py
# using student class 
from student import Student

# create instance 

s  = Student()

# store data into the instance
s.Setid(100)
s.Setname('vishal')
s.Setaddress('H no - 60 , surat ')
s.Setmarks(990)


# retrieve the data from the class 

print('Id of the student ' , s.Getid())
print('Name of the student ' , s.Getname())
print('Address of the student ', s.Getaddress())
print('Marks secured by student ',s.Getmarks())

# a python program to create student class by deriving it from the Teacher class 
# student class - V2.0 . save it as student .py
from teacher import Teacher

class Student(Teacher):
	def Setmarks(self,marks):
		self.marks = marks

	def Getmarks(self):
		return self.marks


# a python program to access the base class constructor  from sub class 
# base class constructor is available to sub class 

class Father:
	def __init__(self):
		self.property = 800000.00

	def display_property(self):
		print('Father\'s property = ', self.property)

class Son(Father):
	pass # we don't want to write in the son class 

# create sub class instance and display father's property
s = Son()

s.display_property()

# a python program to override super class constructor and method in sub class 

# overriding the base class constructor and  method in the sub class 

class Father():
	def __init__(self):
		self.property = 8000000.00

	def display_property(self):
		print('Fathe\'s property  :' , self.property )


class Son(Father):
	def __init__(self):
		self.property = 200000.00

	def display_property(self):
		print('Child\'s property :',self.property)

# create sub class instance and display father's property
s = Son()
s.display_property()

# a python porgram to call the super class constuctor in the sub class using super()

# accessing base Class constructor in sub class

class Father:
	def __init__(self,property = 0):
		self.property = property

	def display_property(self):
		print('Father\'s property ', self.property)


class Son(Father):
	def __init__(self,property1 = 0 , property = 0):
		super().__init__(property)
		self.property1 = property1
	def display_property(self):
		print('Total property of child :  ', self.property1 + self.property)

# create sub  class instance and display father's property 

s = Son(200000,800000)
s.display_property()

# a python program to access base class constructor and method in the sub class using super()

# accessing base class class constructor and method in the sub class 

class Square():
	def __init__(self,x):
		self.x = x

	def area(self):
		print('Area of square  :', self.x*self.x)

class Rectangle(Square):
	def __init__(self,x,y):
		super().__init__(x)
		self.y = y
	def area(self):
		super().area()
		print('Area of rectangle  :', self.x*self.y)


# find areas of square and rectangle 
a , b = [float(x) for x in input('Enter two measurement :').split()]

r = Rectangle(a,b)
r.area()

# a python program showing single inheritance in which two sub classes are derived from a single base class 

# single inheritance

class Bank(object):
	cash = 1000000000
	@classmethod
	def available_cash(cls):
		print(cls.cash)


class AndhraBank(Bank):
	pass

class StateBank(Bank):
	cash = 2000000
	@classmethod
	def available_cash(cls):
		print(cls.cash+Bank.cash)

a = AndhraBank()
a.available_cash()

s = StateBank()
s.available_cash()

# a python program to implement multiple inheritance using two base classes 

# multiple inheritance 

class Father():
	def height(self):
		print('Height is 6.0 foot')


class Mother():
	def color(self):
		print('Color is brown')


class Child(Father,Mother):
	pass


c = Child()

print('child\'s inherited qualities :')

c.height()
c.color()


# a python program to prove that only one class constructor is available to sub class in multiple inheritance

# when super classes have constructors

class A(object):
	def __init__(self):
		self.a = 'a'
		print(self.a)
		super().__init__()

class B(object):
	def __init__(self):
		self.b = 'b'
		print(self.b)


class C(A,B):
	def __init__(self):
		self.c= 'c'
		print(self.c)
		super().__init__()

# access the super class instane vars from c 

o = C()  # o is object of class C

# a python program to access all the instance variables of both the base classes in multiple inheritance 

# when super classes have construtors - V2.0

class A(object):
	def __init__(self):
		self.a = 'a'
		print(self.a)
		super().__init__()


class B(object):
	def __init__(self):
		self.b = 'b'
		print(self.b)
		super().__init__()


class C(A,B):
	def __init__(self):
		self.c = 'c'
		print(self.c)
		super().__init__()


# access the super class instance  vars from  c

o = C()

# a python program to understand the order of execution of methods in several base classes according 

class A(object):
	def method(self):
		print('A class method ')
		super().method()


class B(object):
	def method(self):
		print('B class method ')
		super().method()


class C(object):
	def method(self):
		print('C class method')
		 

class X(A,B):
	def method(self):
		print('X self method ')
		super().method()

class Y(B,C):
	def method(self):
		print('Y Class method')
		super().method()


class P(X,Y,C):
	def method(self):
		print('P class method')
		super().method()

p = P()
p.method()

# a python porgam to invoke a method on an object without knowing the  type (or class ) of the object 

# duck typing example 
# Duck class contains talk() method

class Duck():
	def talk(self):
		print('Quack ,Quack ')


# huamn class 
class Human():
	def talk (self):
		print('Hello , hi')


# this method accepts an object and calls talk() method
def call_talk(obj):
	obj.talk()




# call  call_talk() method and pass an object
# depending on type of object , talk () method is executed 

x = Duck()

call_talk(x)

x = Human()

call_talk(x)

# a python program to call a method that does not appear in the object passed to the method

#duck typing example - V 2.0
# Dog class contains bark() method

class Dog :
	def bark(self):
		print('Bow , Bow!')

# Duck class contains talk()

class Duck():
	def talk(self):
		print('Quack , quack !')



# human class contains talk()

class Human():
	def talk():
		print('Hello ,hi ')


# this method accepts an object and calls talk () method

def call_talk(k):
	k.talk()


# call call_talk() method and pass an object
# depending on type o object , talk () method is executed 

x = Duck()
call_talk(x)

x = Human()


x = Dog()
call_talk(x)

# a python progam to check the object type to know whether the method exists in the object or not 

# strong typing example 

class Dog :
	def bark(self):
		print('Bow , Wow!')


# Duck class contains talk()  method 

class Duck:
	def talk(self):
		print('Quack , quack !')

# human class 

class Human():
	def talk(self):
		print('Hello , hi ')


# this method accepts an object and calls talk() method
def call_talk(obj):
	if hasattr(obj , 'talk'):
		obj.talk()
	elif hasattr(obj , 'bark'):
		obj.bark()
	else:
		print('Wrong object passed ...')


# call call_talk() method and passed an object
# depending on type of object , talk() method is executed

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x)



#  A python program to understand that MyClass method is shared by all of its objects

# A class with a method

class MyClass():
	def calculate(self,x):
		print('Square value' , x*x)

# all objects share same calculate method

obj1 = MyClass()
obj1.calculate(2)

obj2 = MyClass()
obj2.calculate(3)

obj3 = MyClass()
obj3.calculate(4)

# a python program to  create abstract class and sub classes with which implement the abstract method of the abstract class 

# abstract class example 

from abc import ABC , abstractmethod

class MyClass(ABC):
	@abstractmethod
	def calculate(self,x):
		pass # empty body , no code

# this is sub class of MyClass
class sub1(MyClass):
	def calculate(self,x):
		print('Square value :', x*x )


# this is another sub class for MyClass

import math
class sub2(MyClass):
	def calculate(self,x):
		print('Square root :' , math.sqrt(x))

class sub3(MyClass):
	def calculate(self,x):
		print('Cube root :', x**3)


obj1 = sub1()
obj1.calculate(16)

obj2 = sub2()
obj2.calculate(16)

obj3 = sub3()
obj3.calculate(16)


# a python porgram to create a Car abstract that  contains an instance variable , a concrete method and two abstact methods 

from abc import *

class Car(ABC):
	def __init__(self,regno):
		self.regno = regno
	def openTank(self):
		print('Fill the fuel into the Tank')
		print('for the car with regno ', self.regno)
	@abstractmethod
	def steering(self):
		pass

	@abstractmethod
	def braking(self):
		pass



# a python program to in which maruti sub class implements the abstract methods of the super class , car

# this is a sub class for abstract car class 

from abs import Car 

class Maruti(Car):
	def steering(self):
		print('Maruti uses manual steering ')
		print('Drive the car ')

	def braking(self):
		print('Maruti uses hydraulic brakes ')
		print('Apply brakes and stop it')

# create object to Maruti and use its features 

m = Maruti(1001)
m.openTank()
m.steering()
m.braking()

# a python program to in which santro sub class implements the abstract methods of the super class , car

# this is sub class for abstract Car class 
from abs import Car

class Santro(Car):

	def steering(self):
		print('Santro uses power steering ')
		print('Drive the car')

	def braking(self):
		print('Santro uses gas brakes ')
		print('Apply brakes and stop it')


# create object to santro and use its features 

s = Santro(7878)
s.openTank()
s.steering()
s.braking()

# a python program to develop an interface that connects to any database

# abstract class works like an interface 

from  abc import *

class MyClass(ABC):
	def connect(self):
		pass 
	def disconnect(self):
		pass



# this is a sub class 

class Oracle(MyClass):
	def connect(self):
		print('Connecting to Oracle database')
	def disconnect(self):
		print('Disconnected from Oracle')


# this is another sub class 

class Sybase(MyClass):
	def connect(self):
		print('Connecting to Sybase datbase...')

	def disconnect(self):
		print('Disconnected from Sybase')


class Database:
	str = input('Enter datbase name')
	
	classname = globals() [str]
	x = classname()

	x.connect()
	x.disconnect()

# a python program which contains printer interface and its sub classes to send text to any printer 

# An interface to send text to any printer

from abc import *

# create an interface

class Printer(ABC):
	def printit(self,text):
		pass
	def disconnect(self):
		pass

class IBM(Printer):
	def printit(self,text):
		print(text)

	def disconnect(self):
		print('Printing completed on IBM printer ')

# this is sub class for Epson printer 
class Epson(Printer):
	def printit(self,text):
		print(text)

	def disconnect(self):
		print('Printing completed on Epson printer ')

class UsePrinter():
	#accept printer name as string from configuation file
	#f = open('config' , 'w')
	#f.write('Epson')
	#f.close()

	#with open('config', 'r') as f :
	#	str = f.readline()
	

	# convert the string into classname 
	classname = 'Epson' #globals() [str]

	# create an object to that class 


	x = classname()
	#
	#call the print() and disconnect() methods 
	x.print('Hello , this is sent to printer')
	x.disconnect()

# a python program to develop an interface that connects to any database

# abstract class works like an interface 

from  abc import *

class MyClass(ABC):
	def connect(self):
		pass 
	def disconnect(self):
		pass



# this is a sub class 

class Oracle(MyClass):
	def connect(self):
		print('Connecting to Oracle database')
	def disconnect(self):
		print('Disconnected from Oracle')


# this is another sub class 

class Sybase(MyClass):
	def connect(self):
		print('Connecting to Sybase datbase...')

	def disconnect(self):
		print('Disconnected from Sybase')


class Database:
	str = input('Enter datbase name')
	
	classname = globals() [str]
	x = classname()

	x.connect()
	x.disconnect()

# a python porgram to create a Car abstract that  contains an instance variable , a concrete method and two abstact methods 

from abc import *

class Car(ABC):
	def __init__(self,regno):
		self.regno = regno
	def openTank(self):
		print('Fill the fuel into the Tank')
		print('for the car with regno ', self.regno)
	@abstractmethod
	def steering(self):
		pass

	@abstractmethod
	def braking(self):
		pass
