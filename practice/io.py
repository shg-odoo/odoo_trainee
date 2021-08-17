# open() returns a file object, and is most commonly used with two arguments: 
# pen(filename, mode).

""" It is good practice to use the with keyword when dealing with file objects. 
he advantage is that the file is properly closed after its suite finishes, 
even if an exception is raised at some point. Using with is also much shorter 
han writing equivalent try-finally blocks:"""
with open('workfile',"w+") as f:
	f.write("hello everyone !!!!!!!!!")
	value = ('the answer', 42)
	s = str(value)  # convert the tuple to string
	f.write(s)
	for l in f:
		print(l)
	# r=f.readline()

	# print(r)
	# read_data = f.read()
	# print(read_data)

# We can check that the file has been automatically closed.

