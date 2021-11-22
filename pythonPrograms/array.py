#import array as ar
#ar.array('i', [10,22,11,23,45])
#or
from array import*
roll=array('i', [10,22,11,23,45]) # i is type code i->integer,f->float...
print(roll[1])
print('index of 23 : ',roll.index(23))
print('for loop')
for r in roll:
    print(r)
print('while Loop')
tot=len(roll)
i=0
while(i<tot):
    print(roll[i])
    i+=1    
print('Append (60) method in array')
roll.append(60)
print('Insert(80) method in array')
roll.insert(1,80)
for r in roll:
    print(r)

st_roll=array('i',[])    
n=int(input('How many elements '))
for x in range(n):
    st_roll.append(int(input('Enter Element ')))
print("Entered Elements") 
for nr in st_roll:
    print(nr)

print('Pop')
st_roll.pop()
r=st_roll.pop(1)
for nr in st_roll:
    print(nr)
print('Removed Element ',r)


