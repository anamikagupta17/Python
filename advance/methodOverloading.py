class Myclas:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
             s=a+b+c
        elif a!=None and b!=None:
             s=a+b   
        else:
            s=a       
        return s

s=Myclas()

print(s.sum(3,4,5))
print(s.sum(4,5))
print(s.sum(10))