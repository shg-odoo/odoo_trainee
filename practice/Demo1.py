print ("hello...")

class A:
    def __init__(self):
        print("init metod...")
    def show1(self):
        print("method of a")   

class B(A):
    def __init__(self):
        super().__init__()
    def show2(self):
        print("method of b")

b1=B()
b1.show1()

