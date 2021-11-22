class Father:
    def __init__(self):
        super().__init__()  #calling Parent class constructor
        print("Father Class Costructor")

    def fshow(slef):
        print("Father Class Method")


class Mother:
    def __init__(self):
        super().__init__()  #calling Parent class constructor
        print("Mother Class Costructor")

    def mshow(slef):
        print("Mother Class Method")        


class Son(Father,Mother):
    def __init__(self):
        super().__init__()  #calling father class constructor
        print("Son Class Costructor")

    def show(slef):
        print("Son Class Method")    

#for costructors first son then father then object, object don't have any costructors so it call mother again mother will goto object, object again dont have any costructors but father already visited so will stop to mother


s=Son()
s.fshow()
s.mshow()      
s.show()      