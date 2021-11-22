class Duck:
    def walk(self):
        print("thapak thapak thapak thapak ")

class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak ")

class Cat:
    def talk(self):
        print("Meow Meow")
def myFunction(obj):
    #strong typing
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()    

d=Duck()
myFunction(d)    
h=Horse()
myFunction(h)  
c=Cat()
myFunction(c)  

