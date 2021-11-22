#membership operatiors

#in
str="Anamika Gupta"
print('ana' in str)
print('Ana' in str)

#not in 

str="Anamika Gupta"
print('ana' not in str)
print('Ana' not in str)


print('\n')

#bitwise operator
a=10
b=15
print('~a=',~a)
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
print('a>>2=',a>>2)
print('a<<2=',a<<2)

print('\n')

#identity operator
a=20
b=20
c='20'
print(a is b)
print(c is b)
print(a is not b)
print(c is not b)

print('\n')
#type conversion
a=20
b=15
print(a/b)
print(type(a/b))
print(10 + 10.5)

print('\n')
#type conversion explicit

print('type conversion explicit')
str="Anamika"
print(tuple(str))
print(list(str))