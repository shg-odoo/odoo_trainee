thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# length
print(len(thislist))


# datatypes

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# type

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)



# Access Items

thislist1 = ["apple", "banana", "cherry"]
print(thislist1[1])


# Negative Indexing

thislist2 = ["apple", "banana", "cherry"]
print(thislist2[-1])

print(thislist2[1:2]) #Range of Indexes



# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# append an item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# loop in list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]