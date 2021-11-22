#list comperhension
print('list comprehnsion')
list1=[0,1,2,3,4,5,6,7,8,9]
new_list=[i+1 for i in list1]
print(new_list)
print('list comprehnsion using range')
print([i+2 for i in range(20)])
print('list comprehnsion using range and with for and if ')
print([i for i in range(20) if (i%2==0)]) # can add multile if and for  if().. if..
print('list comprehnsion  if and else ')
print([i if i%2==0 else 'invalid' for i in range(15)])
a=[[1,2,3,4],[5,6,7,8]]
print('nested')
print([[i*j for j in range(4,7)] for i in range(6,8)])  # outer loop run first
print('set comprehnsion')
sets={1,2,3,4,}
print({i+3 for i in sets })
# all functioanlity same as list
#set can't  be nested

print('dictionary comprehnsion')
dc={'key1':101,'key2':102}
print({n:n*2 for n in dc})
print({n:n*2 for n in range(5)})


