import json
from werkzeug.wrappers import Request, Response

with open('outputFile.json') as kishan:
  data = json.load(kishan)

  for i in data['firstName']: 
    print(i) 

print(data)
print(data['address'])
