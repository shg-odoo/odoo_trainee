s ="hello, Welcome to odoo india"
print(s)
print(len(s))
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.title())
print(s.center(80,"-").upper())
print(s.count("o"))
print(s.endswith("dia"))
print(s.find("odoo"))
print(s.index("o",7))
print(s.isalpha())#whitespace not allow
print("sertyhgfds".islower())
print("DHCFHF".isupper())
print(s.split(","))

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
