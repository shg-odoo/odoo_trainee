a=[4,6,7,2,6,9,612,98]


a[5]=55
#list method
print(a)
print("count num:",a.count(6))
print(len(a))
a.append(33)
print(a)
print(a.pop())
print(a)
b=a.copy()
print("B    :",b)
a.insert(4,"hello")
print(a)
a.remove("hello")
a.reverse()
print(a)
a.sort()
print("sort",a)
a.sort(reverse=True)
print("desc         :",a)



# list sliceing

print(a[:])
print(a[6])
print(a[2:5])
print(a[-5:-2])
print(a[2:])
print(a[:2])
print(a[::-1])
print(a + ["a","b"])
b=[3,[7,8,9],66]
print(b[1][1])


#list comprehensions
squares = [x**2 for x in range(11)]
print(squares)