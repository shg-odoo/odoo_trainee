class Duck:
    def talk(self):
        print("Heloo")
class Dog:
    def Bark(self):
        print("Hiii")
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'Bark'):
        obj.Bark()

d = Duck()
dg = Dog()
f1(d)
f1(dg)