import json

data={
    "firstName": "kishan",
    "lastName": "Rathod",
    "gender": "male",
    "age": 23,
    "address": {
        "streetAddress": "126 Raval Street",
        "city": "Botad",
        "state": "MCA",
        "postalCode": "364710"
    },
    "phoneNumbers": [
        { "type": "home", "number": "9574231635" }
    ]
}

output= open('outputFile.json', 'w')
json.dump(data, output)
