class Father:
    def __init__(self,m):
        self.money=100
        self.job=m
        print("Parent Class constructor")

    def show(self):
        print("Parent  Class method") 

class Son(Father):
     def __init__(self,m):
        super().__init__(m)
        self.money=2000
        print("Child Class constructor")

     def show(self):
        super().show()  # using super we can get parent class method also
        print("Child  Class method")     
    

 # child class constructor override parent class constructor   

s=Son('developer')
print(s.money)
s.show()
#after using super 
print(s.job)

#super used for using methods and constructor of parent class