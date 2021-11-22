str1='Hello Anamika '
str2="Hello Parul "
str3='''Hello Anamika
How are you?
hope you are fine
Thank You'''
print(str1)
print(str2)
print(str3)
print(len(str1))
print(str1*7)
print(str1[0:5]*7)
print(str1 + str2)
print("Hello "+str1)
print('hello %s'%('anamika'))
print('hello %(nm)s' % {'nm':'anamika'})
print('my age is {}'.format(25))
print("{}   {}  ".format(10,12))
print("{num1}   {num2}  ".format(num2=10,num1=12))
q=10
p=20
print(f"{q}       {p}")
print (str1.upper())
print (str1.lower())
print (str1.swapcase())
print (str3.title())
print (str1.isupper()) # true if all character shoud be caps
print (str1.islower()) # true if all character shoud be lower
print (str3.istitle()) # true if first letter of all word showd be caps

name='3125325236'
name2="ewtwet5346347347"
print(name.isdigit())
print(name2.isalnum())
print(name.isalpha())

strrr="   "
print(strrr.isspace())
ana="  Anamika Gupta "
print(ana.lstrip())
print(ana.rstrip())
print(ana.strip())

print(ana.replace("Anamika","Parul"))
print(ana.split(' '))
print('_'.join(name2))

strr="Hi Anamika Gupta"
print('startswith & endswith method')
print(strr.startswith('Hi'))
print(strr.startswith('an'))
print(strr.endswith('Gupta'))