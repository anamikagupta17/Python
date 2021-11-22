from numpy import*
a=array([[10,20,30,40],[1,2,3,4]])
print(a[0][1])
for r in a:
    for c in r:
        print(c)
    print()
print('with index')
n=len(a)
k=0
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print() 
print('while loop')
while(k<n):
    j=0
    while(j<len(a[i])):
        print(a[k][j])
        j+=1
    k+=1   
print() 

print('rshape')
ar=array([1,2,3,4,5,6])
print(ar)
print(reshape(ar,(2,3)))

print('input from user')
r=int(input('Enter Number of Rows : '))
c=int(input('Enter Number of Columns : '))
a=zeros((r,c))
l=len(a)
for i in range(l):
    for j in range(len(a[i])):
        a[i][j]=int(input('Enter Element '))
print(a)
print('input from user using while loop')
r=int(input('Enter Number of Rows : '))
c=int(input('Enter Number of Columns : '))
a=zeros((r,c),dtype=int)
l=len(a)
m=0
while(m<l):
    n=0
    while(n<len(a[m])):
        a[m][n]=int(input('Enter Element '))
        n+=1
    m+=1
print(a) 



print('ndim')
print(a.ndim)
print('shape')
print(a.shape)
print('size')
print(a.size)
print('itemsize')
print(a.itemsize)
print('nbytes')
print(a.nbytes)


print('slicing')  
print(a[0,:])   
print( a[:,0])  
print( a[0:1,0:1])  # arrary[0][0] value2