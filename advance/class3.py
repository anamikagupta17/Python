print('Passing member of one classs to another class')
class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    def disp(self):
        print("Name ",self.name)
        print("Roll ",self.roll)


class User:
    @staticmethod
    def show(s):
        print("User Name ",s.name) 
        print("User Roll ",s.roll)    
        s.disp()

stu=Student('Anamika',101) 
User.show(stu)             