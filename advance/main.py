import cal  #import module cal

print("cal module's variable:",cal.a)
cal.name()

print(cal.add(10,20))
print(cal.sub(20,10))
add=cal.add
print(add(40,30))
c=cal.Myclass()  # class
c.myname()   #class method

#from cal import a
#from cal import*
#print(a)

import cal2
print("second Module value:",cal2.a)
cal2.name()
print(cal2.mul(10,20))
print(cal2.div(20,2))