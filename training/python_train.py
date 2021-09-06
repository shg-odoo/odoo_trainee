print("Hello, World", end="!")
print("yay!" if 0 > 1 else "nay!" )

print("LIST")

l=[1,2,3,4,5]
l.append(6)
print(l)
a=l.pop()
print(l)
print(l[3])
print(l[1:4])
del l[3]
a=["a","b"]
l.extend(a)
print(l)

for i in l:
	print(i)
print(len(l))

print("TUPLE")
print(type(2))

t=(1,2,3,4,5,6)
print(t)
print(len(t))
print(t+(7,8,9))
print("DICTIONARY")
d={"a":1,"b":2,"c":3}
print(d)
print(d.keys())
print(d.values())
d.update({"d":4,"e":5})
print(d)

print("SET")
print({1,2,3,4,6} > {3,4,5,6,7,8,9})
print({1,2,3,4,5,6} < {3,4,5,6,7,8,9})
print({1,2,3,4,5,6} == {3,4,5,6,7,8,9})
print({1,2,3,5,6} >= {3,4,5,6,7,8,9})
print({1,2,3,4,5,6} ^ {3,4,5,6,7,9})
print({1,2,3,4,5,6} - {3,4,5,6,7,8,9})

print("CONDITIONAL AND LOOPS")
for i in range(4,8,2):
	print(i)
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))

l=iter(l)
print(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))


def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y
sum=add(1,3)
print(sum)

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)           
all_the_args(**kwargs)         
all_the_args(*args, **kwargs)

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_20 = create_adder(20)
print(add_20(4))

print({x for x in 'abcdcbaefgh' if x not in 'abc'})

import math
print(math.sqrt(25))
print(math.ceil(25.345))
print(math.floor(25.567))


class Human:

	species = "H. sapiens"
	def __init__(self, name):
		self.name=name
		self.age=0

	def say(self,msg):
	    print("{name}: {message}".format(name=self.name,message=msg))
			
	def sing(self):
	    return ('hello')

	@classmethod
	def get_species(cls):
		return cls.species
			
	@staticmethod
	def grunt():
		return "*grunt*"
			
	@property
	def age(self):
		return self._age
			
	@age.setter
	def age(self, age):
		self._age = age
			
	@age.deleter
	def age(self):
		del self._age
			
if __name__ == '__main__':
		   # Instantiate a class
	i = Human(name="Ian")
	i.say("hi")                    
	j = Human("Joel")
	j.say("hello")                  
			   
	i.say(i.get_species())
	Human.species = "H. neanderthalensis"
	i.say(i.get_species())
	j.say(j.get_species())
	
	print(Human.grunt())     
	print(i.grunt())         
	i.age = 42
	
	i.say(i.age)
	j.say(j.age)
	del i.age
			



#Generators
def double_numbers(iterable):
    for i in iterable:
        yield i + i
a=[1,2,3,4,5]
for j in double_numbers(a):
	print(j)

#Decorators

from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())                
print(say(say_please=True))