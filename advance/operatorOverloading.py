class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other):  # we can write this function in B also
        return self.x+other.x 


class B:
    def __init__(self,x):
        self.x=x          


a=A(100)
b=B(200)
print(a+b)   #will call A.__add__(100,200) adding 2 objects this is not define so we created we can createany function like this