l=[1,2,3,'shv']

print(len(l))

print(l[2])

l[2]='abc'

print("after update=",l)

del l[0]
# l.clear()
# print(l)

print(l)

# Practise of tuples....

t=('abc','xyz',67,54)
print(t)


print(t[1])


x=list(t)
x.append(6454)
print(x)

t=tuple(t)

#Practise of sets....

s={5,67,'ghf'}
print(s)

y=tuple(s)
print("tuple= ",y)

p=set()
print(type(p))

q={}
print(type(q))