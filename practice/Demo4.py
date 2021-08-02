d={'1':'shv','2':'abc','3':'pqr'}

print(d)

d[4]='lmn'
print(d)

x=d.keys
print(x)

del d['3']
print(d)


student_info = {'id1': 
   {'name': ['ABC'], 
    'class': ['5'], 
   },
 'id2': 
  {'name': ['XYZ'], 
    'class': ['4'], 
    },
 'id3': 
    {'name': ['ABC'], 
    'class': ['5'], 
    
   },
 'id4': 
   {'name': ['PQR'], 
    'class': ['2'], 
   },
}

result = {}

for key,value in student_info.items():
    if value not in result.values():
        result[key] = value

print(result)