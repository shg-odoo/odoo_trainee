#fibonacci
def fib(n):
	a,b=0,1
	while a<n:
		print(a,end=" ")
		a,b=b,a+b
	print()

fib(400)# calling function



#argument type
print("1.default or Positional\n2.keyword\n3.Arbitary argument")
def defaultarg(a,b=6,c=7,d=8):
	print(a,b,c,d)
defaultarg(5)

def keyarg(x=1,y=2):
	print("x : ",x,"y : ",y)

keyarg(x=10,y=20)


def arbiarg(*a,**ab):
	print("A",a,"B",ab)

arbiarg(3,5,4,51,33,a=44,b=55,c=66)


def standard_arg(arg):
	print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only:int, /, standard, *, kwd_only):
	print("annotation",combined_example.__annotations__)
	print(pos_only, standard, kwd_only)
standard_arg(5)  # we can put both the arguments default or keyword
pos_only_arg(6) #we can't arg put like this : arg=6
kwd_only_arg(arg=7) #we can't put areg like this : 7
combined_example(8,standard=9,kwd_only=10)




	
