class Mobile:
    fp="Yes"  #class variable
    @staticmethod   #decorator
    def getvalue(f1,f2):  #static method
        print(f1+f2)
        print(Mobile.fp)

x=Mobile()     
Mobile.getvalue(10,20)     #calling static method
