class Army:
    def __init__(self):
        self.name="Anamika"
        self.gn=self.Gun()  # inner class object
    def show(self):
        print("Name :",self.name)  

    class Gun:
        def __init__(self):
            self.name="AK47"  
            self.capacity="75 rounds"
            self.length='34.3 In'

        def disp(self):
            print("Gun Name :",self.name)
            print("Gun Capacity :",self.capacity)
            print("Gun Length :",self.length)

a=Army()
print('Outer Class variable and method')
print(a.name)
a.show()
print('Inner Class variable and method')
print(a.gn.name)
a.gn.disp()
g=a.gn
print(g.capacity)

# we can also crete object of inner class
g=Army().Gun()
print(g.length)