try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    
    print(inst.args)     
    print(inst)          
                         
    x, y = inst.args     
    print('x =', x)
    print('y =', y)


def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

def func():
    raise IOError

try:
    func()
except IOError as exc:
	print(exc)
    # raise RuntimeError('Failed to open database') from exc
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
