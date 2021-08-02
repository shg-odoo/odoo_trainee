from abc import ABC  

class A(ABC):
    def show(self):
        print("class A..")
        

class B(A):
    def print():
        pass


a=B()
a.show()