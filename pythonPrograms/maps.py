a=[10,20,30,40,50]
b=[1,2,3,4,5]
def inc(n):
    return n+5

result=map(inc,a) # return map object so need to convert in list .inc will callfor every element of a
print(list(result))

print('Using lambda function ')
result=map(lambda n:n+2,a)
print(list(result))
print('Add 2 list')
lst=list(map(lambda m,n:m+n,a,b)) # it will pass elemetns of a,b together but lenth of all list shoud be smae 
print(lst)