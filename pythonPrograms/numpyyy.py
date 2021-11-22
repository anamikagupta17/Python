from numpy import*
roll=array([1,2,3,4,5,6],dtype='float')
for i in roll:
    print(i)
print('With Index')
for i in range(len(roll)):
    print(i,'=',roll[i])
print('linspace')
a =linspace(1,9,num=20)
b =linspace(1,5,num=10,endpoint=False)
print(a)    
print(b)
print('logspace')
c =linspace(1,3,5)
print(c)
print('arange')
print(arange(5))
print(arange(1,10,2))
print('zeros')
print(zeros(5))
print(zeros(5,dtype=int))
print('ones')
print(ones(5))
print(ones(5,dtype=int))

print('all() & any()')
ar=array([100,200,300,400])
ar2=array([100,200,20,30])
ar3=array([100,200,300,400])
ar4=array([100,200,0,300,400,0])
c=ar==ar2
d=ar==ar2
print(any(c))
print(all(d))
print('where in array')
e=where(ar2>ar3,ar2,ar3)
print(e)
print('nonzero')
print(nonzero(ar4))
print('view')
b=ar.view()
b[1]=30
print(b)
print(ar)
print('copy')
a=ar.copy()
ar[3]=90
print(ar)
print(a)

n=int(input('Enter number of elements : '))
nonarr=zeros(n,dtype=int)
for i in range(n):
    x=int(input('Enter Element '))
    nonarr[i]=x
print(nonarr)   
z=0
while(z<n):
    print(nonarr[z])
    z+=1 