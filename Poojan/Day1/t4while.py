
# while 
i = 1
while i < 6:
  print(i)
  i += 1


# break state

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue state
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else in while
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")