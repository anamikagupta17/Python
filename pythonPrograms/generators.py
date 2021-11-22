def disp(a,b):
    yield a
    yield b

x,y=disp(10,20)
print(x)
print(y)
result=disp(10,20)
print(result)
print(type(result))
print(next(result))
print(next(result))
print("More Example")
def show(a,b):
    while(a<=b):
        yield a
        a=a+1

rs=show(1,5) 
print(rs)
print(type(rs))   
print(next(rs))    
print(next(rs))   
print(next(rs))   
print(next(rs))   
print(next(rs))   



