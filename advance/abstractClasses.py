from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod  #abstact method
    def disp(self):
        pass

    def show(self):  #concrete method
        print('Concrete Method')

class Child(Father):
    def disp(self):
       print("Child Class")
       print("Abstact Method")       

c=Child()
c.disp()
c.show()       

print()
class Defence(ABC):
    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun= AK47")

class Army(Defence):
    def area(self):
        print("Army Area =Land")

class AirForce(Defence):
    def area(self):
        print("AirForce Area =Sky")

class Navy(Defence):
    def area(self):
        print("Navy Area =Sea")       


a=Army()
af=AirForce()
n=Navy()

a.gun()
a.area()

af.gun()
af.area()

n.gun()
n.area()