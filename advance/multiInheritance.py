class Father:
    def __init__(self):
        print("Parent Class Constructor")
    def show(self):
        print("Parent Class")
    def desp(self):
        print("Instance method of Parent class")    

    def multi(self):
        print("Multi level Inheritance")       


class Son(Father):
    def __init__(self):
        super().__init__()
        print('Child class constructor')
    def sondesp(self):
        print("Child Class")     

class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print('Grand Child class constructor')
    def grandson(self):
        print("Grand son class")    

            


g=GrandSon()
g.show()
g.multi()
g.grandson()
g.sondesp()
