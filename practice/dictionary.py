tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel.items())
print(tel.keys())
print(tel.values())
print(tel.popitem())

print(tel['jack'])

del tel['sape']
print(tel)
d={"a":55,"b":767}
tel.update(d)

print(tel)
tel['irv'] = 4127

x={'jack': 4098, 'guido': 4127, 'irv': 4127}
print(list(tel))

print('guido' in tel)

print('jack' not in tel)


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')