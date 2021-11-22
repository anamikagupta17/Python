def add(a,b):
    print(a+b)
def sub(a,b):
    return a-b    

add(4,6)
add(41,16)
add(14,16)
print(sub(10,2))

def function1():
    print('Function 1')
    def function2():
        print('Function 2')
    function2()    

function1()       

def desp(sh):
    print("Desp Function "+sh())
def show():
    return "Show FUnction"    

desp(show)    
print('Lambda function')
z=lambda x,y:print(x+y)
z(4,5)
show=lambda x,y=2:(x+y,x-y)
a,b=show(6,4)
print(a)
print(b)

add=lambda x:lambda y:x+y
a=add(12)
print(a(7))

def sh(x):
    print(x(10))

sh(lambda x:x)    
print("IIFE function")
(lambda z :print( z + 2))(4)
