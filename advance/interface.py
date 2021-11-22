from abc import ABC,abstractmethod

class Father(ABC):
    @abstractmethod  #abstact method
    def disp(self):
        pass
    def disp2(self):
        pass

class Child(Father):
    def disp(self):
       print("Child Class")
       print("Abstact Method")   

class Grandchild(Child):
    def disp2(self):
       print("Grand Child Class")
       print(" Abstact Method2")              

gc=Grandchild()
gc.disp()  
gc.disp2()  