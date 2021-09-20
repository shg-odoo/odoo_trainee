thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# all keys
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y= car.values() #all values

print(x)



# change value

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


# print only keys
for x in thisdict:
  print(x)
  print(thisdict[x]) #print values

# nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
