from array import*
ar1=array('i', [10,22,11,23,45])
ar2=array('i', [1,2,3,4,5])
print("Array apter reverse")
ar1.reverse()
for nr in ar1:
    print(nr)
print("extend method")   
ar1.extend(ar2)
for x in ar1:
    print(x)
print("***Slicing***")
ar3=array('i', [10,22,11,23,45])
a=ar3[1:4]
for i in a:
    print(i)
print('Slicing setpwise')    
b=ar3[0:5:2]   
for j in b:
    print(j)