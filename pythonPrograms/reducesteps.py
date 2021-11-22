from functools import*

a=[10,20,30,40,50]
result=reduce(lambda n,m:n+m,a) # take 2-2 elements eg: 10+20=30,30+30=60,60+40=100,100+50=150
print(result)
print(type(result))