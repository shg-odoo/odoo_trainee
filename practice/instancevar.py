class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs

print(e.kind)                  # shared by all dogs

print(d.name)                  # unique to d

print(e.name)                  # unique to e


# shared data can have possibly surprising effects with involving 
# mutable objects such as lists and dictionaries.
class Dog:

    # tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks=[]         # creates a new empty list for each dog


    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)