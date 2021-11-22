class Father:
    def __init__(self):
        print("Parent Class Constructor")
    def show(self):
        print("Parent Class Instant Method")


class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Child Class Costructor1 ")
    def disp(self):
        print("Child Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Child Class Costructor2 ")
    def disp(self):
        print("Child Class Method2")        


d=Daughter()
s=Son()
s.show()
d.show()
d.disp()