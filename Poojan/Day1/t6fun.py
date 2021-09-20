
# simple fun in py'

def my_function():
  print("Hello from a function")

# fun calling
my_function()

# fun with arguments
def my_function1(fname):
  print(fname + " Refsnes")

my_function1("Emil")
my_function1("Tobias")

# maultiple argu
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("poojan", "patel")


# multiple args using *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# multiple args using **kwrgs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



# default name
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India")



# recursion fun

def factorial_n(n):
   if n == 1:
       return n
   else:
       return n*factorial_n(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", factorial_n(num))


# simple lambda fun
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))