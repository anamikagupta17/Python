class Mobile:
    varr="class Variable" #class /static variable
    def __init__(self,m):
        self.model="Realme"  # instance variable
        self.year=m
    def show(self,p):  #instance method
        print("first class method")
        print("my model",self.model)
        print("year",self.year,"price",p)
#create separate memory of each object
x=Mobile(2000)
x.show(500)   
print(id(x))
y=Mobile(5000)
y.show(100)   
print(id(y))
print('Access variable')  
print(x.model)

