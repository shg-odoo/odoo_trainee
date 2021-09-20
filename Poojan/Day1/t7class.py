# t7class.py

# constructor in class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)#object of class

print(p1.name)
print(p1.age)

del p1 #delete object
del p1.age #del age property



# simple inheritance in oop
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("patel", "poojan", 2021)
x.welcome()





# try except
try:
  print(x)
except:
  print("An exception occurred")

# finally make sure that it will be execute
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")



# raise exception
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")