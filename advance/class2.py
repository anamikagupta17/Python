#namespace
print('namespace')
class Mobile:
    fp="Yes"  # mpping is class namespace

redme=Mobile()    # mapping of object is instance name space
realme=Mobile()     # mapping of object instance name space
print(redme.fp)
print(realme.fp) 

realme.fp="no"
print(redme.fp)
print(realme.fp) 

Mobile.fp="Noo"
realme=Mobile()  
print(redme.fp)
print(realme.fp) 
