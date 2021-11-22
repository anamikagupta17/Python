class Mobile:
    fp="Yes I am the Class variable"  # class variable
    def __init__(self):
        self.model="Ream me"

    @classmethod   #class method
    def show_fp(cls,v):
        print('Inside class')
        print(cls.fp) 
        cls.fp="modified by class method" 
        print(v)
        
x=Mobile()
x.show_fp("value")

print('Outside class')
print(Mobile.fp)
Mobile.fp="modified by  class name"
print(Mobile.fp)