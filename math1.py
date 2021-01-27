import math 
def display():
	print("hi there ")

class demo:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		c = self.a+self.b
		return c
d = demo(10,20)
print("sum is = ",d.add())
	
