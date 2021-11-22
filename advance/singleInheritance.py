class Father:  #parent class
    money=1000
    def __init__(self):
        self.business="Office"
        print("Father Class Constructor")
        
    def show(self):
        print('Parant Class Instance  Method')
    
    @classmethod
    def showmoney(cls):
        print('Parent Class Class Method :',cls.money)

    @staticmethod
    def staticm():
        print('Parent Class Static Method')    

class Son(Father):  #child class
    def disp(self):
        print("Child Class Instance Method")


s=Son()
s.show()
s.showmoney()
s.disp()  
s.staticm()   

print('Constructor')
print(s.business)
