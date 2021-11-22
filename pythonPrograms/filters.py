a=[10,20,40,50,60,70,80,90,5,8,9]
def high_mark(n):
    if n>=60:
        return True

result=filter(high_mark,a)     # high_mark function will call for every element of a     10,20...
print(list(result))  #it will return filter object so need to convert in list or according to need
print('Using lambda function ')
result2=filter(lambda n:(n >=60),a)     # high_mark function will call for every element of a     10,20...
print(list(result2))