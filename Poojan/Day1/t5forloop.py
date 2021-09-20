# t5forloop.py


# simple loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)

for x in "banana":
 	print(x)


# break continue same as while

# loop range
for x in range(6):
  print(x)

# range with else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

 # condition match break

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
